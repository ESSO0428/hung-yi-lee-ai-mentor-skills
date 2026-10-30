"""Read-only PyTorch diagnostics for models supplied by a mentor caller.

This module never constructs, trains, downloads, or mutates a model.  A caller
provides a ``torch.nn.Module``, attaches hooks, runs its own forward/backward
pass, and then asks for a provenance-friendly snapshot.
"""

from __future__ import annotations

import argparse
import importlib
import math
from typing import Any


TOOL_VERSION = "1.1.0"


class OptionalDependencyError(RuntimeError):
    """Raised when the torch extra is not installed."""


def require_torch():
    try:
        return importlib.import_module("torch")
    except ImportError as exc:
        raise OptionalDependencyError(
            "Torch diagnostics require the mentor skill's torch extra; "
            "install it with 'uv sync --extra torch'."
        ) from exc


def _tensor_stats(tensor: Any, *, max_elements: int = 1_000_000) -> dict[str, Any]:
    if max_elements < 1:
        raise ValueError("max_elements must be positive")
    torch = require_torch()
    detached = tensor.detach().float()
    original_shape = list(detached.shape)
    original_count = int(detached.numel())
    sampled = original_count > max_elements
    if sampled:
        flat = detached.reshape(-1)
        indices = torch.linspace(0, original_count - 1, max_elements, device=flat.device).long()
        detached = flat.index_select(0, indices)
    detached = detached.cpu()
    finite = torch.isfinite(detached)
    finite_values = detached[finite]
    finite_count = int(finite_values.numel())
    return {
        "shape": original_shape,
        "count": original_count,
        "sampled": sampled,
        "sampled_count": int(detached.numel()),
        "finite_count": finite_count,
        "mean": float(finite_values.mean().item()) if finite_count else None,
        "std": float(finite_values.std(unbiased=False).item()) if finite_count else None,
        "min": float(finite_values.min().item()) if finite_count else None,
        "max": float(finite_values.max().item()) if finite_count else None,
        "l2_norm": float(finite_values.norm().item()) if finite_count else None,
        "nan_fraction": float(torch.isnan(detached).float().mean().item()) if detached.numel() else 0.0,
        "inf_fraction": float(torch.isinf(detached).float().mean().item()) if detached.numel() else 0.0,
        "nonfinite_fraction": float((~finite).float().mean().item()) if detached.numel() else 0.0,
    }


class TorchDiagnostics:
    """Collect parameter, gradient, and activation health after a caller run."""

    def __init__(self, model: Any, *, max_tensor_elements: int = 1_000_000) -> None:
        torch = require_torch()
        if not isinstance(model, torch.nn.Module):
            raise TypeError("model must be a torch.nn.Module")
        if max_tensor_elements < 1:
            raise ValueError("max_tensor_elements must be positive")
        self.model = model
        self.max_tensor_elements = max_tensor_elements
        self._handles: list[Any] = []
        self._activations: dict[str, dict[str, Any]] = {}

    def attach_activation_hooks(self) -> None:
        for name, module in self.model.named_modules():
            if not name:
                continue

            def hook(_module: Any, _inputs: Any, output: Any, module_name: str = name) -> None:
                tensor = output
                if isinstance(output, (tuple, list)):
                    tensor = next((item for item in output if hasattr(item, "detach")), None)
                if tensor is not None and hasattr(tensor, "detach"):
                    self._activations[module_name] = _tensor_stats(tensor, max_elements=self.max_tensor_elements)

            self._handles.append(module.register_forward_hook(hook))

    def close(self) -> None:
        for handle in self._handles:
            handle.remove()
        self._handles.clear()

    def parameter_stats(self) -> list[dict[str, Any]]:
        rows = []
        for name, parameter in self.model.named_parameters():
            row: dict[str, Any] = {
                "name": name,
                "shape": list(parameter.shape),
                "numel": int(parameter.numel()),
                "trainable": bool(parameter.requires_grad),
                "value": _tensor_stats(parameter, max_elements=self.max_tensor_elements),
            }
            if parameter.grad is not None:
                row["gradient"] = _tensor_stats(parameter.grad, max_elements=self.max_tensor_elements)
                row["gradient_norm"] = row["gradient"]["l2_norm"]
                row["gradient_norm_sampled"] = row["gradient"]["sampled"]
            else:
                row["gradient"] = None
                row["gradient_norm"] = None
            rows.append(row)
        return rows

    def snapshot(self) -> dict[str, Any]:
        parameters = self.parameter_stats()
        total = sum(item["numel"] for item in parameters)
        trainable = sum(item["numel"] for item in parameters if item["trainable"])
        return {
            "schema_version": "torch-diagnostics.v2",
            "tool": "torch_diagnostics",
            "tool_version": TOOL_VERSION,
            "model_class": f"{self.model.__class__.__module__}.{self.model.__class__.__qualname__}",
            "parameter_count": total,
            "trainable_parameter_count": trainable,
            "parameters": parameters,
            "activations": dict(self._activations),
            "policy": "read-only diagnostics; caller owns forward/backward and intervention choice",
        }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", action="version", version=TOOL_VERSION)
    parser.parse_args()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

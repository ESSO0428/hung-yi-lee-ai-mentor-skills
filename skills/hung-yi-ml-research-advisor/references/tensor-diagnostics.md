# Tensor 診斷（torch profile）

只在競爭假設涉及模型內部時用：參數量級、gradient 健康度、activation 飽和、dead unit、NaN/Inf。前置：`uv sync --extra torch`；缺 torch 就回報這個命令。

`tools/torch_diagnostics.py` 是函式庫，沒有 `--input` CLI。由呼叫端自己的 Python 載入模型並做 forward／backward：

```python
import sys; sys.path.insert(0, "<skill>/tools")
from torch_diagnostics import TorchDiagnostics
d = TorchDiagnostics(model); d.attach_activation_hooks()
model(x).sum().backward()          # 呼叫端負責
snap = d.snapshot(); d.close()
```

`snapshot()` 回 `parameter_count`、各參數的 gradient 統計、各層 activation 統計。唯讀，不訓練、不改 checkpoint。大模型可能要抽樣或更多記憶體；掃描不完整就明說，不假裝完整。

這些數字是診斷證據，不是因果：要搭配 metrics、切分完整性與一個受控實驗，才能建議改 recipe。對應 optimization.md 的「gradient norm 與 loss 不降」。

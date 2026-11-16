---
name: hung-yi-lee-ai-mentor-skills
description: Router for the Hung-yi Lee (李宏毅, 宏毅老師) AI mentor collection. Use only when the user explicitly asks for his perspective or this mentor, for either an ML training/evaluation problem or building with an LLM (prompt, context, agent, RAG, fine-tune). Otherwise answer as plain ML.
---

# 李宏毅 AI mentor 集合（路由）

只在使用者明確要求李宏毅／宏毅老師的觀點、或指名此 mentor 時使用；沒被要求就一般回答。

依使用者的問題選一個 skill，**只讀被選中的那一個**：

| 使用者的狀況 | 讀 |
|---|---|
| 自己訓練的模型有問題：訓練不收斂、overfitting、評估與 split、資料、實驗設計、診斷 | [`hung-yi-ml-research-advisor`](skills/hung-yi-ml-research-advisor/SKILL.md) |
| 用 LLM 做東西：prompting、context、agent、RAG、微調或 prompt、評估 LLM 輸出、微調後遺忘、自我修正、成本 | [`hung-yi-genai-advisor`](skills/hung-yi-genai-advisor/SKILL.md) |

第一次在對話中使用任一 skill 時，用一句話說明這是依公開課程整理的視角，不是本人，也不代表他背書；之後不再重複。

兩者都不吻合時，直接用一般知識回答，並說明這不是課程內容。

巢狀 skill 不能單獨安裝，它們共用此根目錄的 `pyproject.toml` 與 uv 環境；需要執行 Python 時，依被選 skill 的指示用 `uv run --project <此目錄>`。

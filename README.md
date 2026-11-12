# Luigi's Agent

Personal agent built on [Google ADK](https://google.github.io/adk-docs/) (Python).

## Setup
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env   # add your API key
```

## Run
```
adk web .        # dev UI (select luigis_agent)
adk run luigis_agent
pytest
```

## Layout
- `luigis_agent/` – agent package (`agent.py` exposes `root_agent`, `tools.py`, `prompts.py`)
- `tests/` – pytest; `evals/` – ADK eval sets; `scripts/`, `data/` – helpers & data
- `.mcp.json` – registers the ADK docs MCP server for Claude Code

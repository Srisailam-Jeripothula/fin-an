# Financial Document Analyzer - Debug Assignment

## Project Overview
A comprehensive financial document analysis system that processes corporate reports, financial statements, and investment documents using AI-powered analysis agents.

## Getting Started

# Financial Document Analyzer API

## Bugs Fixed
| Bug | Fix |
|-----|-----|
| `llm = llm` undefined | Set `llm = LLM(model="openai/gpt-4o")` with imports |
| Wrong CrewAI imports | `from crewai import Agent, LLM` |
| `tool=[...]` attribute | Changed to `tools=[...]` |
| `@staticmethod + @tool` conflict in tools.py | Rewrote as standalone `@tool`-decorated `read_financial_document(path: str)` |
| Agent goals/backstories hallucinated | Professional goals/backstories for all 4 agents |
| `max_iter=1, max_rpm=1` too restrictive | Set `max_iter=5, max_rpm=10` |
| `from crewai_tools import tools` invalid | `from crewai_tools import SerperDevTool` |
| `Pdf(file_path=path).load()` doesn't exist | `PyPDFLoader` from `langchain_community` |
| Tool methods missing `self` | `@staticmethod` + `@tool()` decorators |
| Task descriptions "make up URLs" | Factual descriptions tied to `{query}` |
| Verification used wrong agent | Fixed `agent=verifier` |
| Function name collision | Renamed endpoint to `analyze_document()` |
| Query validation wrong order | `if not query or query.strip() == ""` |
| `uvicorn.run(..., reload=True)` invalid | Removed `reload=True` |
| Missing deps (uvicorn, python-dotenv, python-multipart) | Added to requirements.txt |

## Setup Instructions
1. Clone repo: `git clone <your-repo-url>`
2. Install: `pip install -r requirements.txt`
3. Create `.env`: `OPENAI_API_KEY=your_key`
4. Run: `uvicorn main:app --reload`
5. Test at http://localhost:8000/docs (Swagger UI)

## API Documentation
- **POST /analyze**: Upload PDF + query → AI analysis via CrewAI agents.
  - Body: Form-data `file` (PDF), `query` (str).
  - Response: JSON analysis (revenue, margins, recommendations).

**Example curl:**
```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "accept: application/json" \
  -F "file=@financial_report.pdf;type=application/pdf" \
  -F "query=What are key revenue trends and investment recommendations?"

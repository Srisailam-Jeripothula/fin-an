# Financial Document Analyzer - Debug Assignment

## Project Overview
A comprehensive financial document analysis system that processes corporate reports, financial statements, and investment documents using AI-powered analysis agents.


# Financial Document Analyzer API

## Bugs Fixed
| Bug | Fix |
|-----|-----|
| `llm = llm` undefined | Set `llm = LLM(model="openai/gpt-4o")` with imports |
| Wrong CrewAI imports | `from crewai import Agent, LLM`  |
| `tool=[...]` attribute | Changed to `tools=[...]`  |
| `@staticmethod + @tool` conflict in tools.py | Rewrote as standalone `@tool`-decorated `read_financial_document(path: str)` |
| Missing deps (uvicorn, python-dotenv, python-multipart) | Added to requirements.txt|

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
- Example curl:

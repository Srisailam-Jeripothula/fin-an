import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import SerperDevTool
from langchain_community.document_loaders import PyPDFLoader
from crewai.tools import tool

## Creating search tool
search_tool = SerperDevTool()

@tool("Read Financial Document")
def read_financial_document(path: str) -> str:
    """Reads and returns the full text content of a PDF financial document.
    Use this tool to read the financial document before analyzing it.
    Args:
        path: The file path to the PDF document to read.
    Returns:
        The full text content of the financial document.
    """
    try:
        loader = PyPDFLoader(file_path=path)
        docs = loader.load()
        full_report = ""
        for data in docs:
            content = data.page_content
            while "\n\n" in content:
                content = content.replace("\n\n", "\n")
            full_report += content + "\n"
        return full_report
    except Exception as e:
        return f"Error reading document at {path}: {str(e)}"

class FinancialDocumentTool:
    read_data_tool = read_financial_document


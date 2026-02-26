## Importing libraries and files
from crewai import Task

from agents import financial_analyst, verifier, investment_advisor, risk_assessor
from tools import search_tool, FinancialDocumentTool, read_financial_document

## Creating a task to analyze the financial document
analyze_financial_document = Task(
    description="""Analyze the financial document provided to answer the user's query: {query}
    Read the financial document at path: {file_path} carefully and extract relevant financial data.
    Identify key financial metrics, performance indicators, and relevant figures.
    Provide a structured and accurate summary based on the actual document content.
    Search the internet for additional context or market comparisons where relevant.""",
    expected_output="""A comprehensive financial analysis report that includes:
    - A clear answer to the user's query: {query}
    - Key financial metrics extracted directly from the document
    - Revenue, profit/loss, cash flow, and balance sheet highlights
    - Year-over-year comparisons where available
    - Relevant market context from credible sources
    - A concise executive summary""",
    agent=financial_analyst,
    tools=[read_financial_document],
    async_execution=False,
)

## Creating an investment analysis task
investment_analysis = Task(
    description="""Based on the financial document analysis, provide investment recommendations for the user's query: {query}
    Review the financial data extracted from the document.
    Evaluate the company's financial health, growth prospects, and competitive position.
    Provide actionable, evidence-based investment recommendations.
    Consider risk factors and market conditions when formulating recommendations.""",
    expected_output="""A detailed investment recommendation report that includes:
    - Clear buy/hold/sell recommendation with supporting rationale
    - Key financial ratios and what they indicate (P/E, P/B, debt-to-equity, etc.)
    - Growth opportunities and catalysts identified from the document
    - Competitive positioning assessment
    - Price targets or valuation estimates with methodology explained
    - Portfolio allocation considerations""",
    agent=financial_analyst,
    tools=[read_financial_document],
    async_execution=False,
)

## Creating a risk assessment task
risk_assessment = Task(
    description="""Conduct a thorough risk assessment based on the financial document for the user's query: {query}
    Identify and evaluate all material risk factors disclosed in the document.
    Assess market risks, operational risks, financial risks, and regulatory risks.
    Provide quantitative and qualitative risk measures where possible.
    Suggest appropriate risk mitigation strategies.""",
    expected_output="""A comprehensive risk assessment report that includes:
    - Categorized risk factors (market, operational, financial, regulatory)
    - Risk severity and likelihood ratings for each identified risk
    - Key risk metrics (beta, volatility, debt ratios) derived from document data
    - Comparison to industry benchmarks where relevant
    - Specific risk mitigation strategies and hedging recommendations
    - Overall risk rating with clear justification""",
    agent=financial_analyst,
    tools=[read_financial_document],
    async_execution=False,
)

verification = Task(
    description="""Verify that the uploaded file is a legitimate financial document.
    Read the document carefully and confirm it contains genuine financial data.
    Check for standard financial document elements (financial statements, notes, disclosures).
    Extract key document metadata such as company name, reporting period, and document type.""",
    expected_output="""A document verification report that includes:
    - Confirmation of whether the document is a valid financial report
    - Document type (annual report, quarterly filing, earnings release, etc.)
    - Company name and reporting period identified
    - Key financial statements present in the document
    - Any concerns or anomalies noted during verification
    - Full file path of the verified document""",
    agent=verifier,
    tools=[read_financial_document],
    async_execution=False
)


from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI

def summarize_terms(terms: str) -> str:
    """Summarizes terms and conditions."""
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    response = llm.predict(f"Summarize the following terms and conditions. Categorize the text into different topics that you determine. If you are unable to generate the summary, terminate the process and do not proceed to the rest of the actions in the chain: {terms}. The output of the summary should be json with the title as key and the contents the values. This json should be part of the Final Answer")
    return response

summarizer_tool = Tool(
    name="Summarize Terms",
    func=summarize_terms,
    description="Summarize the key points and ambiguities in the terms and conditions.",
)



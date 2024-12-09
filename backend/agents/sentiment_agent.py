# import os
# from langchain import hub
# from langchain.agents import create_react_agent, AgentExecutor
# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
#
#
# def analyze_sentiment(terms: str) -> str:
#     """Analyzes sentiment of terms and conditions."""
#     llm = ChatOpenAI(
#         temperature=0,
#         model_name="gpt-4o-mini",
#         openai_api_key=os.getenv("OPENAI_API_KEY"),
#     )
#     template = """
#     Perform sentiment analysis on the following terms and conditions:
#     {terms}
#     Classify each section as positive, neutral, or negative.
#     """
#     prompt_template = PromptTemplate(input_variables=["terms"], template=template)
#
#     react_prompt = hub.pull("hwchase17/react")
#     agent = create_react_agent(llm=llm, tools=[], prompt=react_prompt)
#     agent_executor = AgentExecutor(agent=agent, tools=[], verbose=True)
#
#     result = agent_executor.invoke({"input": prompt_template.format_prompt(terms=terms)})
#     return result["output"]



from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI

def analyze_sentiment(terms: str) -> str:
    """Analyzes sentiment of terms and conditions."""
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    response = llm.predict(f"Perform sentiment analysis on these terms: {terms}")
    return response

sentiment_tool = Tool(
    name="Analyze Sentiment",
    func=analyze_sentiment,
    description="Perform sentiment analysis on the terms and classify each section as positive, neutral, or negative.",
)



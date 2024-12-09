# import os
# from langchain import hub
# from langchain.agents import create_react_agent, AgentExecutor
# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
#
#
# def analyze_risks(terms: str) -> str:
#     """Analyzes risks in terms and conditions."""
#     llm = ChatOpenAI(
#         temperature=0,
#         model_name="gpt-4o-mini",
#         openai_api_key=os.getenv("OPENAI_API_KEY"),
#     )
#     template = """
#     Identify and classify risks in the following terms and conditions:
#     {terms}
#     Classify risks as high, medium, or low, and suggest mitigations.
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

def analyze_risks(terms: str) -> str:
    """Analyzes risks in terms and conditions."""
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    response = llm.predict(f"Analyze risks that are in the summarized terms and conditions. Identify any specific red flags from the content that has been scraped. Then Categorize the text into different topics that you determine. Identify only three risks. If you are unable to generate the specific risks, terminate the process and do not proceed to the rest of the actions in the chain: {terms}. The output of the risk analyzer should be json with the title as key and the contents the values. This json should be part of the Final Answer")
    return response

risk_analyzer_tool = Tool(
    name="Analyze Risks",
    func=analyze_risks,
    description="Identify risks in the terms and classify them as high, medium, or low.",
)



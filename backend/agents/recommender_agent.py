# import os
# from langchain import hub
# from langchain.agents import create_react_agent, AgentExecutor
# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
#
#
# def generate_recommendations(risks: str) -> str:
#     """Generates actionable recommendations based on risks."""
#     llm = ChatOpenAI(
#         temperature=0,
#         model_name="gpt-4o-mini",
#         openai_api_key=os.getenv("OPENAI_API_KEY"),
#     )
#     template = """
#     Based on the following risks, provide actionable recommendations:
#     {risks}
#     """
#     prompt_template = PromptTemplate(input_variables=["risks"], template=template)
#
#     react_prompt = hub.pull("hwchase17/react")
#     agent = create_react_agent(llm=llm, tools=[], prompt=react_prompt)
#     agent_executor = AgentExecutor(agent=agent, tools=[], verbose=True)
#
#     result = agent_executor.invoke({"input": prompt_template.format_prompt(risks=risks)})
#     return result["output"]


from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI

def generate_recommendations(risks: str) -> str:
    """Generates recommendations based on risks."""
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    response = llm.predict(f"Generate recommendations based on these risks. The recommendations need to be specific and related to the risks. The recommendations should be on what the user can do to protect themselves, not the company. Generate a maximum of three recommendations. Each recommendation should have a title : {risks}. The output of the recommender should be json with the title as key and the contents the values. This json should be part of the Final Answer")
    return response

recommender_tool = Tool(
    name="Generate Recommendations",
    func=generate_recommendations,
    description="Provide actionable recommendations based on identified risks.",
)



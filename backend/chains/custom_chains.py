


# from langchain.agents import create_react_agent, AgentExecutor
# from langchain_openai import ChatOpenAI
# from langchain import hub

# from agents.scraper_agent import scraper_tool
# from agents.summarizer_agent import summarizer_tool
# from agents.risk_analyzer_agent import risk_analyzer_tool
# from agents.recommender_agent import recommender_tool

# def build_custom_chain():
#     """
#     Builds a custom chain combining all tools for the T&C analysis pipeline using ReAct prompting.
#     """
#     llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

#     # List of tools to use
#     tools = [
#         scraper_tool,
#         summarizer_tool,
#         risk_analyzer_tool,
#         recommender_tool,
#     ]

#     # Use the hwchase17/react prompt
#     react_prompt = hub.pull("hwchase17/react")
   


#     # Create the ReAct agent
#     agent = create_react_agent(llm=llm, tools=tools, prompt=react_prompt)

#     # Wrap it in an executor
#     return AgentExecutor(agent=agent, tools=tools, verbose=True, return_intermediate_steps=True)



from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain import hub

from agents.scraper_agent import scraper_tool
from agents.summarizer_agent import summarizer_tool
from agents.risk_analyzer_agent import risk_analyzer_tool
from agents.recommender_agent import recommender_tool

def build_custom_chain():
    """
    Builds a custom chain combining all tools for the T&C analysis pipeline using ReAct prompting.
    """
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    # List of tools to use
    tools = [
        scraper_tool,
        summarizer_tool,
        risk_analyzer_tool,
        recommender_tool,
    ]

    # Use the hwchase17/react prompt
    react_prompt = hub.pull("hwchase17/react")

    # Create the ReAct agent
    agent = create_react_agent(llm=llm, tools=tools, prompt=react_prompt)

    # Wrap it in an executor
    return AgentExecutor(agent=agent, tools=tools, verbose=True, return_intermediate_steps=True)

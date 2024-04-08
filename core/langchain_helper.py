from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type, animal_color):
    llm = OpenAI(temperature=0.7)
    
    PROMPT = """
    I have a {animal_color} {animal_type} pet and want to give it a name.
    Can you suggest five cool names for my {animal_color} {animal_type}?
    """
    
    promtp_template = PromptTemplate(
        template=PROMPT,
        input_variables=["animal_type", "animal_color"]
    )
    pet_name_chain = LLMChain(llm=llm, 
        prompt=promtp_template, 
        output_key="pet_name"
    )
    chain_kwargs = {
        "animal_type": animal_type, 
        "animal_color": animal_color
    }
    pet_name = pet_name_chain(chain_kwargs)
    
    return pet_name

def langchain_agent():
    llm = OpenAI(temperature=0.7)
    
    tool_set = ['wikipedia', 'llm-math']
    tools = load_tools(tool_names=tool_set, llm=llm)
    
    agent = initialize_agent(
        tools=tools, 
        llm=llm, 
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, 
        verbose=True
    )
    result = agent.run("What is the average age of a dog? Multiply the result by 3")
    
    return result
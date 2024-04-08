from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

def generate_pet_name(animal_type, animal_color):
    llm = OpenAI(temperature=0.5)
    
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


if __name__ == '__main__':
    print(generate_pet_name(animal_type="bear", animal_color="white"))
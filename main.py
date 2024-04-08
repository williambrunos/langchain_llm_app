from core.langchain_helper import generate_pet_name
import streamlit as st


st.title("Pets name generator")

animal_type = st.sidebar.selectbox(
    label="Select animal type", 
    options=["dog", "cat", "bear"]
)

if animal_type.lower() == 'cat':
    animal_color = st.sidebar.text_area(
        label="What color is your cat?", 
        max_chars=10
    )
elif animal_type.lower() == 'dog':
    animal_color = st.sidebar.text_area(
        label="What color is your dog?", 
        max_chars=10
    )
else:
    animal_color = st.sidebar.text_area(
        label="What color is your cow?", 
        max_chars=10
    )

if animal_color:
    response = generate_pet_name(animal_type=animal_type, animal_color=animal_color)
    st.text(response['pet_name'])
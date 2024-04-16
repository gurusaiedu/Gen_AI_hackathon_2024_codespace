from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_core.messages import HumanMessage

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate


import os

os.environ['GOOGLE_API_KEY'] = "AIzaSyB_VtaStDXRpaGqdahwYv-8ys-ZXHITd4s"

llm=ChatGoogleGenerativeAI(model='gemini-pro-vision')
from memory import add_to_memory

ingredient_list=None
def load_img(img):

    prompt2="Identify the ingredients in the image for cooking. If no ingredients are present, state 'No ingredients are present for cooking in this image.'"
    message=HumanMessage(
        content=[
            {'type':'text','text':prompt2},
            {'type':'image_url','image_url':img}
        ]
    )
    reponse=llm.invoke([message])
    ingredient_list=reponse.content
    list_of_recipe=list_of_recipe_generation(ingredient_list)
    
    reponsef=ingredient_list+"\n\n With the ingredients above, here are some recommended recipes \n\n"+list_of_recipe
    print(reponsef)
    add_to_memory(response=reponsef)



def list_of_recipe_generation(ingredient_list):
    prompt_templet_string="""Based on the following list of ingredients:

    {ingredient_list}

    Generate a list of recipes that can be made using these ingredients. Please prioritize recipes that utilize a high percentage of the provided ingredients.

    For each recipe, provide:

    * Recipe title
    * A brief description of the recipe
    * A link to the recipe website (if available)
    """
    prompt=ChatPromptTemplate.from_template(prompt_templet_string)
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)

   
    chain=LLMChain(llm=model,prompt=prompt)

    reponse=chain.run(ingredient_list)
    return reponse




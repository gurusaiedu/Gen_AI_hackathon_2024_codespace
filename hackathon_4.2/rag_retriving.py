from operator import itemgetter
import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

import base64
import io
from io import BytesIO

import numpy as np
from PIL import Image


def resize_base64_image(base64_string, size=(128, 128)):
    """
    Resize an image encoded as a Base64 string.

    Args:
    base64_string (str): Base64 string of the original image.
    size (tuple): Desired size of the image as (width, height).

    Returns:
    str: Base64 string of the resized image.
    """
    # Decode the Base64 string
    img_data = base64.b64decode(base64_string)
    img = Image.open(io.BytesIO(img_data))

    # Resize the image
    resized_img = img.resize(size, Image.LANCZOS)

    # Save the resized image to a bytes buffer
    buffered = io.BytesIO()
    resized_img.save(buffered, format=img.format)

    # Encode the resized image to Base64
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def is_base64(s):
    """Check if a string is Base64 encoded"""
    try:
        return base64.b64encode(base64.b64decode(s)) == s.encode()
    except Exception:
        return False


def split_image_text_types(docs):
    """Split numpy array images and texts"""
    images = []
    text = []
    for doc in docs:
        doc = doc.page_content  # Extract Document contents
        if is_base64(doc):
            # Resize image to avoid OAI server error
            images.append(
                resize_base64_image(doc, size=(250, 250))
            )  # base64 encoded str
        else:
            text.append(doc)
    return {"images": images, "texts": text}




def prompt_func(data_dict):
    # Joining the context texts into a single string
    formatted_texts = "\n".join(data_dict["context"]["texts"])
    messages = []

    # Adding image(s) to the messages if present
    if data_dict["context"]["images"]:
        image_message = {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{data_dict['context']['images'][0]}"
            },
        }
        messages.append(image_message)

    # Adding the text message for analysis
    text_message = {
        "type": "text",
            "text": (
                "As a recipe creation expert, your task is to analyze the user's keywords "
                "and any related images to generate a delicious recipe. \n\n"
                f"User-provided keywords: {data_dict['question']}\n\n"
                "Analyze the keywords and any retrieved images to identify potential ingredients. "
                "Based on your findings, create a recipe that includes:\n"
                "- A list of ingredients and their quantities.\n"
                "- Clear and concise cooking instructions.\n"
                "- Optional: Nutritional information (calories, fat, protein, etc.).\n"
                "Text and / or tables:\n"
                f"{formatted_texts}"
            ),
    }
    messages.append(text_message)

    return [HumanMessage(content=messages)]


import os
os.environ['GOOGLE_API_KEY'] = "AIzaSyB_VtaStDXRpaGqdahwYv-8ys-ZXHITd4s"

from langchain_google_genai import ChatGoogleGenerativeAI  # Assuming this is the correct import
llm=ChatGoogleGenerativeAI(model='gemini-pro')
model = llm  #ChatOpenAI(temperature=0, model="gpt-4-vision-preview", max_tokens=1024)
from rag_preprocess import vectorDB_reference

def Recipe_generation(user_input):
    print("in method")
    retriever=vectorDB_reference()
    print("yes db")
    # RAG pipeline
    chain = (
        {
            "context": retriever | RunnableLambda(split_image_text_types),
            "question": RunnablePassthrough(),
        }
        | RunnableLambda(prompt_func)
        | model
        | StrOutputParser()
    )
    print("in llm hand")
    Recipe_generation_process=chain.invoke(user_input)
    print(Recipe_generation_process)
    return Recipe_generation_process

# print("helo")
# Recipe_generation("tea")
# print(">>>>>>>>>>>>> end")
import streamlit as st
import time as time
from img_preprocess import load_img
from PIL import Image

from memory import chat_memory
from rag_retriving import Recipe_generation
uploadedImage=None
uploaded_file=None
promts = []
from memory import add_to_memory

def main():
    cssCodeExecution() 
    col1,col2=st.columns([1,4])
    col1.markdown("<div class='header'><h1 style=color:darkblue;>Multimodal RAG Application</h1></div>", unsafe_allow_html=True)

    userPrompt=st.chat_input(placeholder="Please Enter Your promt")
    
    selected_option=st.sidebar.selectbox("Choose an Option:",options=["Recipe generation", "Chat with PDF"])
    # Display the selected option
    if selected_option == "Recipe generation":
        uploadedImage = st.sidebar.file_uploader("Choose Image",type="jpg")
        if userPrompt:
            imageExtractionProcess(None)
        else:
            imageExtractionProcess(uploadedImage)

    elif selected_option == "Chat with PDF":
        uploaded_file = st.sidebar.file_uploader("Choose a PDF or Doc file:", type=["pdf", "docx"])
            
        if userPrompt:
            multiModuleRagProcess(None)
            pdf_chain(userPrompt)
            raw_memory_history=pdf_chat_memory()
            human_strings,ai_strings=formatAIResponse(raw_memory_history)
            printUi(human_strings,ai_strings)
        else:
            multiModuleRagProcess(uploaded_file)
        
        
    if selected_option == "Recipe generation":
        if userPrompt:
            answer=Recipe_generation(userPrompt)
            print("-------------->",userPrompt)
            print("-------------->",answer)
            add_to_memory(response=answer,user_input= userPrompt)
        
        raw_memory_history=chat_memory()
        human_strings,ai_strings=formatAIResponse(raw_memory_history)
        printUi(human_strings,ai_strings)

    
from pdf_memory import pdf_chat_memory
from pdf_control import pdf_chain
# Function to display Status message as toast on Sidebar
def toastForSidebar(statusMessage):
    toast_message=statusMessage
    time.sleep(1)  
    toast_message.empty()  

# Function to display Status message as toast on MainScreen
def toastForMainScreen(message):
    toast_message=message
    time.sleep(1)  
    toast_message.empty()  

def cssCodeExecution():
    st.markdown("""
    <style>
        .header
        {
            background-color: white; /* Light grey background for header */
            padding: 5px;
            color: aqua;
            position: fixed; /* Fix the header to the top */
            top: 0; /* Position it at the top of the viewport */
            width: 100%; /* Make it span the entire width */
            z-index: 5; /* Ensure the header stays on top during scrolling */
        }
        .question-container 
        {
            border-radius: 10px; /* Round corners */
            overflow-y: auto; /* Enable scrolling for content within */
        }
        .human 
        {
            background-color: #e0e0e0; /* Light grey background for question */
            padding: 5px; /* Add some padding for better separation */
            border-radius: 5px; /* Round corners for the question paragraph */
            font-weight: bold; /* Bold text for question */
        }
        .st-emotion-cache-18ni7ap.ezrtsby2
        {
            visibility:hidden;
        }
    </style>
    """,unsafe_allow_html=True)
def imageExtractionProcess(image):
    if image is not None: 
         toastForSidebar(st.sidebar.success("File uploaded successfully!"))
         st.sidebar.image(image)
             
         img=Image.open(image)
         load_img(img)

from pdf_control import controller
import os
def multiModuleRagProcess(file):  
    if file is not None: 
         
         toastForSidebar(st.sidebar.success("File uploaded successfully!"))
         path = file.name
         local_folder = "pdf"
         print(local_folder+path)
         print(local_folder+"\\"+path)
         file1=local_folder+"\\"+path
         with open(os.path.join(local_folder, path), "wb") as f:
            f.write(file.read())
        
         controller(file1)

def printUi(human,AI):
    for i in range(len(human)):
        with st.container():
            st.markdown(f"<div class='question-container'><div class='text-container'><p class='human'>{human[i]}</p ><p class='ai'>{AI[i]}</p></div></div>", unsafe_allow_html=True)

def formatAIResponse(raw_memory_history):
    full_string = raw_memory_history['history'] 
    human_strings, ai_strings = [], []
    current_speaker = None  
    for line in full_string.splitlines():  
        if line.startswith('Human:'):
            current_speaker = 'Human'
            human_strings.append(line.replace('Human:', '', 1).strip())  
        elif line.startswith('AI:'):
            current_speaker = 'AI'
            ai_strings.append(line.replace('AI:', '', 1).strip())  
        elif current_speaker:  
            human_strings[-1] += '\n' + line if current_speaker == 'Human' else ''
            ai_strings[-1] += '\n' + line if current_speaker == 'AI' else ''
    return human_strings,ai_strings   

                 
if __name__ == "__main__":
    main()
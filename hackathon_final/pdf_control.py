
from pdf_loading import extract_pdf_elements
from pdf_loading import categorize_elements
from pdf_loading import chunking

from pdf_summaries import generate_text_summaries
from pdf_summaries import generate_img_summaries

from pdf_vectorstore import create_multi_vector_retriever

from pdf_chain import multi_modal_rag_chain



from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")

# The vectorstore to use to index the summaries
vectorstore = Chroma(
    collection_name="mm_rag_cj_blog", embedding_function=embeddings
)

path = "/pdf_img/"
def controller(fname):
    print("i  controll")
    raw_pdf_elements=extract_pdf_elements(path,fname)
    print("exteaction done")
    texts, tables=categorize_elements(raw_pdf_elements)
    print("categorization done")
    texts_4k_token=chunking(texts)
    print("tokenization done")

    text_summaries, table_summaries=generate_text_summaries(texts_4k_token, tables, summarize_texts=False)
    print("table & text summarization done")
    img_base64_list, image_summaries = generate_img_summaries(path="figures")
    print("img summarization done")
    retriever_multi_vector_img = create_multi_vector_retriever(
        vectorstore,
        text_summaries,texts,
        table_summaries,tables,
        image_summaries,img_base64_list,)
    print("successfull add in DB")
    global chain_multimodal_rag  #= multi_modal_rag_chain(retriever_multi_vector_img)
    chain_multimodal_rag = multi_modal_rag_chain(retriever_multi_vector_img)
    print("chain created ")
    # return chain_multimodal_rag
    
    # print("Enter the user queation :")
    # query=input("enter ::: ")
    # response=chain_multimodal_rag.invoke(query)
    # print(response)


# fname="fess101.pdf"
# controller(fname)
from pdf_memory import add_to_pdf_memory

def pdf_chain(query):
    response=chain_multimodal_rag.invoke(query)
    add_to_pdf_memory(response,query)
    # return response

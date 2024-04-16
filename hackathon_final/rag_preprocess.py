from unstructured.partition.pdf import partition_pdf

import os
from langchain_community.vectorstores import Chroma
from langchain_experimental.open_clip import OpenCLIPEmbeddings


def load_pdf():
    print("in pdf loading method")
    rpe=partition_pdf(filename="Indian_Cushine-2.pdf",
                  extract_images_in_pdf=True,
                  infer_table_structure=True,
                  chunking_strategy="by_title",
                  max_characters=4000,
                  new_after_n_chhars=3800,
                  combine_text_under_n_chars=2000,
                  extract_image_block_output_dir="/imgs")
    return rpe


def extract_pdf_elements(rpe):

    tables = []
    texts = []
    
    for element in rpe:
        if "unstructured.documents.elements.Table" in str(type(element)):
            tables.append(str(element))
        elif "unstructured.documents.elements.CompositeElement" in str(type(element)):
            texts.append(str(element))
    
    path="/imgs"
    image_uris = sorted(
        [
            os.path.join(path, image_name)
            for image_name in os.listdir(path)
            if image_name.endswith(".jpg")
        ]
    )
    return texts,tables,image_uris

vectorstore = Chroma(
    collection_name="mm_rag_clip_photos", embedding_function=OpenCLIPEmbeddings()
)
def storing_in_vectorDB(texts,tables,image_uris):

    vectorstore.add_texts(texts=texts)
    vectorstore.add_texts(texts=tables)
    vectorstore.add_images(uris=image_uris)

def vectorDB_reference():
    retriever = vectorstore.as_retriever()
    return retriever


if __name__ == "__main__":
    print("RAG process started...")
    rpe=load_pdf()
    print("Extracting elements from PDF is done")
    texts,tables,image_uris=extract_pdf_elements(rpe)
    print("classification of extracted elements is done")
    storing_in_vectorDB(texts,tables,image_uris)
    print("All elements are stored in chormaDB")

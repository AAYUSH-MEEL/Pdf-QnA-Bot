import streamlit as st
from PyPDF2 import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA



os.environ["GROQ_API_KEY"] = "YOUR_GROQ_API_KEY"

st.header(" AI Chatbot")


with st.sidebar:
    st.title("Your Document")
    file=st.file_uploader("Upload your pdf", type="pdf")
    
if file is not None:
    pdf_pages = PdfReader(file)
    text=""
    for page in pdf_pages.pages:
        text+=page.extract_text()
        
    
    text_splitter = RecursiveCharacterTextSplitter(
        separators="\n",
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks=text_splitter.split_text(text)
    
    
    model_name = "sentence-transformers/all-mpnet-base-v2"
    embaddings = HuggingFaceEmbeddings(
        model_name=model_name,
    )
    
    
    
    vector_store = FAISS.from_texts(chunks,embaddings)
    
    
    user_query=st.text_input("Enter your query")
    
    if user_query:
       llm=ChatGroq(
           model="llama-3.1-8b-instant",
           temperature=0.0,
           max_retries=2,
       )
       chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vector_store.as_retriever())
       response = chain.run(user_query)
       
       st.subheader("Answer")
       st.write(response)
       
       
       

    

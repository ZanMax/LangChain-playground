import os

import pinecone
from dotenv import load_dotenv
from langchain.document_loaders import ReadTheDocsLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Pinecone


def read_docs():
    loader = ReadTheDocsLoader(path=os.getenv("PATH_TO_DATA"), features='html.parser')
    docs_to_load = loader.load()
    return docs_to_load


def split_docs(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100,
                                                   separators=["\n\n", "\n", " ", ""])
    splitted_chunks = text_splitter.split_documents(docs)
    return splitted_chunks


if __name__ == "__main__":
    load_dotenv()
    pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENVIRONMENT_REGION"))
    raw_docs = read_docs()
    chunks = split_docs(raw_docs)

    embeddings = OpenAIEmbeddings()
    Pinecone.from_documents(chunks, embeddings, index_name=os.getenv("PINECONE_INDEX"), overwrite=True)

    print("Uploaded docs to Pinecone!")

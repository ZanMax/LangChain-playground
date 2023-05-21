import os

from langchain.document_loaders import DirectoryLoader, UnstructuredHTMLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS
from dotenv import load_dotenv
from langchain.embeddings import LlamaCppEmbeddings

load_dotenv()

llama_path = os.getenv("LLAMA_PATH")
print(llama_path)

embeddings = LlamaCppEmbeddings(model_path=llama_path)


def read_docs():
    loader = DirectoryLoader(path=os.getenv("PATH_TO_DATA"), loader_cls=UnstructuredHTMLLoader)
    docs_to_load = loader.load()
    return docs_to_load


def split_docs(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100,
                                                   separators=["\n\n", "\n", " ", ""])
    splitted_chunks = text_splitter.split_documents(docs)
    return splitted_chunks


if __name__ == "__main__":
    raw_docs = read_docs()
    chunks = split_docs(raw_docs)
    print("Docs", len(raw_docs))
    print("Chunks", len(chunks))
    print(chunks[0])

    db = FAISS.from_documents(chunks, embeddings)
    db.save_local("db/docker")

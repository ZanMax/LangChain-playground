import os
import pinecone
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone

load_dotenv()
pinecone.init(api_key=os.getenv("PINECONE_API_KEY"), environment=os.getenv("PINECONE_ENVIRONMENT_REGION"))


def run_llm(query: str):
    embeddings = OpenAIEmbeddings()
    search_doc = Pinecone.from_existing_index(index_name=os.getenv("PINECONE_INDEX"), embedding=embeddings)
    chat = ChatOpenAI(temperature=0, verbose=True)
    qa = RetrievalQA.from_chain_type(llm=chat, chain_type="stuff", retriever=search_doc.as_retriever())
    return qa({"query": query})


if __name__ == "__main__":
    res = run_llm("What is LangChain?")
    print(res)

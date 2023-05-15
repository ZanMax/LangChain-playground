import os
from dotenv import load_dotenv
from langchain.document_loaders import ReadTheDocsLoader


def read_docs():
    loader = ReadTheDocsLoader(path=os.getenv("PATH_TO_DATA"), features='html.parser')
    docs_to_load = loader.load()
    return docs_to_load


if __name__ == "__main__":
    load_dotenv()
    print(os.getenv("PATH_TO_DATA"))
    print(len(read_docs()))

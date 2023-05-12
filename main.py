import os

from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from wiki import get_wiki_info

if __name__ == "__main__":
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    model_name = os.getenv("MODEL_NAME")

    print("LongChain Test")

    input_information = get_wiki_info("Albert Einstein", length=1000)
    some_template = """
    Given the information {information} about a person from I want you to create:
    1. a short summary of the person
    2. interesting facts about the person
    """

    prompt_template = PromptTemplate(input_variables=["information"], template=some_template)
    llm = ChatOpenAI(temperature=0, model_name=model_name)
    chain = LLMChain(prompt=prompt_template, llm=llm)
    res = chain.run(information=input_information)

    print(res)

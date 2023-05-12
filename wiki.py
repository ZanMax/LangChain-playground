import wikipedia


def get_wiki_info(topic: str):
    result = wikipedia.search(topic, results=1)

    page = wikipedia.page(result[0])
    return page.content

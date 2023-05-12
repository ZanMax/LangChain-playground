import wikipedia


def get_wiki_info(topic: str, length: int = 0):
    result = wikipedia.search(topic, results=1)

    page = wikipedia.page(result[0])
    if length > 0:
        return page.content[:length]
    return page.content

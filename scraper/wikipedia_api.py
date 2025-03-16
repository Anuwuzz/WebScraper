import wikipediaapi

def get_wikipedia_summary(topic):
    wiki_wiki = wikipediaapi.Wikipedia(
        language="en",
        user_agent="MyWebScraper/1.0 (omniman.irl@gmail.com)"  
    )
    page = wiki_wiki.page(topic)
    return page.summary if page.exists() else "Page does not exist."

def get_wikipedia_sections(topic):
    def extract_sections(sections):
        titles = []
        for section in sections:
            titles.append(section.title)
            titles.extend(extract_sections(section.sections))
        return titles

    wiki_wiki = wikipediaapi.Wikipedia(
        language="en",
        user_agent="MyWebScraper/1.0 (omniman.irl@gmail.com)"
    )
    page = wiki_wiki.page(topic)
    return extract_sections(page.sections) if page.exists() else ["Page does not exist."]

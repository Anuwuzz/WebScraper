from scraper.wikipedia_api import get_wikipedia_summary, get_wikipedia_sections
from scraper.wikipedia_html import scrape_wikipedia_content
from scraper.save_data import save_to_csv

def main():
    topic = "Web scraping" 
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"

    summary = get_wikipedia_summary(topic)
    print("\nSummary:\n", summary)

    sections = get_wikipedia_sections(topic)
    print("\nSections:")
    for section in sections:
        print("-", section)

    content = scrape_wikipedia_content(url)
    print("\nFirst Paragraph:\n", content[0] if content else "No content available.")

    data = {
        "Title": [topic],
        "Summary": [summary],
        "Sections": [", ".join(sections)],
        "Content": [" ".join(content)]
    }
    save_to_csv(data, "wikipedia_scraped_data.csv")

if __name__ == "__main__":
    main()

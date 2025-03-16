**Web Scraper**

## Overview

This project is a **Wikipedia Scraper** designed to extract structured data from Wikipedia efficiently. It utilizes the following technologies:

- **Wikipedia API** – Retrieves article summaries and sections.
- **BeautifulSoup** – Parses and extracts full article content from Wikipedia.
- **Pandas** – Stores extracted data in a structured format (CSV).

The script is built to fetch Wikipedia article summaries, section headings, and full text, organizing the information for further analysis or use.

---

## Installation & Setup

### Step 1: Install Dependencies

Ensure Python 3.7+ is installed, then execute:

```bash
pip install -r requirements.txt
```

---

## Execution Instructions

Run the main script using:

```bash
python main.py
```

## Code Functionality

### `main.py` - Execution Entry Point

This script:
- Retrieves article summaries and sections via the Wikipedia API.
- Extracts full article content using BeautifulSoup.
- Saves the structured data to a CSV file.

#### Sample Output:
```
Summary:
Web scraping is a technique used to extract data from websites...

Sections:
- Introduction
- Techniques
- Uses
- Challenges

First Paragraph:
Web scraping is the process of extracting data from websites...
```

---

### `scraper/wikipedia_api.py` - API-Based Data Retrieval

This module enables programmatic access to Wikipedia’s structured data.

#### Usage Example:
```python
from scraper.wikipedia_api import get_wikipedia_summary, get_wikipedia_sections

topic = "Web scraping"
print(get_wikipedia_summary(topic))
print(get_wikipedia_sections(topic))
```

---

### `scraper/wikipedia_html.py` - Web Scraping Using BeautifulSoup

Extracts detailed content directly from Wikipedia pages.

#### Usage Example:
```python
from scraper.wikipedia_html import scrape_wikipedia_content

url = "https://en.wikipedia.org/wiki/Web_scraping"
content = scrape_wikipedia_content(url)
print(content[:2])  # Displays first two paragraphs
```

---

### `scraper/save_data.py` - Data Storage and Export

Saves extracted information in CSV format for easy access and analysis.

#### Usage Example:
```python
from scraper.save_data import save_to_csv

data = {
    "Title": ["Web Scraping"],
    "Summary": ["Web scraping is the process of extracting data..."],
    "Sections": ["Introduction, Techniques, Uses, Challenges"],
    "Content": ["Web scraping allows automation of data collection..."]
}
save_to_csv(data, "wikipedia_scraped_data.csv")
```

---

## Expected CSV Output

| Title        | Summary                                   | Sections                                   | Content                                   |
| ------------ | ----------------------------------------- | ------------------------------------------ | ----------------------------------------- |
| Web Scraping | Web scraping is a technique to extract... | Introduction, Techniques, Uses, Challenges | Web scraping automates data collection... |

---

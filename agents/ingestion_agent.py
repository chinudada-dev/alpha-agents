from datetime import datetime, timezone
from pathlib import Path
import sys

import feedparser

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config import COMPANIES
from rag.rag_store import get_vector_store

vectordb = get_vector_store()


def fetch_news(company, max_articles=5):
    query = company.replace(" ", "+")
    url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"

    feed = feedparser.parse(url)
    articles = []

    for entry in feed.entries[:max_articles]:
        articles.append(
            {
                "title": entry.get("title", ""),
                "link": entry.get("link", ""),
                "published": entry.get("published", ""),
                "source": entry.get("source", {}).get("title", "Unknown"),
                "summary": entry.get("summary", "")[:300],
            }
        )

    return articles


def store_articles(company, articles):
    texts = []
    metadatas = []

    for article in articles:
        content = f"""
        Company: {company}
        Title: {article['title']}
        Summary: {article['summary']}
        Source: {article['source']}
        """

        texts.append(content)
        metadatas.append(
            {
                "company": company,
                "published": article["published"],
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
        )

    vectordb.add_texts(texts=texts, metadatas=metadatas)
    vectordb.persist()


def run_ingestion():
    print("Starting ingestion...")

    for company in COMPANIES:
        print(f"Fetching: {company}")
        articles = fetch_news(company)

        if not articles:
            print(f"No articles found for {company}")
            continue

        store_articles(company, articles)

    print("Ingestion complete!")


if __name__ == "__main__":
    run_ingestion()

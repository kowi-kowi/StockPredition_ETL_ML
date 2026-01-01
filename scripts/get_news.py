from newsapi import NewsApiClient
import conf
from datetime import datetime, timedelta
import sys

newsapi = NewsApiClient(api_key=conf.NEWS_API_KEY)

# Use a recent window (last 30 days) to avoid requesting data outside your plan limits
now = datetime.utcnow()
to_date = now.strftime("%Y-%m-%d")
from_date = (now - timedelta(days=30)).strftime("%Y-%m-%d")

response = newsapi.get_everything(
    q="S&P 500 OR stock market",
    language="en",
    sort_by="relevancy",
    from_param=from_date,
    to=to_date
)

# Validate response
if not isinstance(response, dict) or response.get("status") != "ok":
    print("Error fetching articles:", response)
    sys.exit(1)

articles = response.get("articles", [])

with open("./data/raw/news_articles.txt", "w", encoding="utf-8") as f:
    for article in articles:
        published = article.get("publishedAt", "")
        title = (article.get("title") or "").replace("\t", " ").replace("\n", " ")
        description = (article.get("description") or "").replace("\t", " ").replace("\n", " ")
        f.write(f"{published}\t{title}\t{description}\n")

print(f"Fetched {len(articles)} articles.")
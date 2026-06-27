import feedparser
from filter_engine import filter_articles

# RSS feed resource

FEEDS = [
    "https://feeds.feedburner.com/TheHackersNews",
    "https://www.bleepingcomputer.com/feed/",
    "https://krebsonsecurity.com/feed/",
    "https://www.darkreading.com/rss.xml",
    "https://www.securityweek.com/feed/"
]


def fetch_news():
    articles = []

    for feed_url in FEEDS:
        print(f"\nFetching news from: {feed_url}")
        feed = feedparser.parse(feed_url)

        for entry in feed.entries[:10]:  #top 10 from each source
            article = {
                "title": entry.get("title", "No Title"),
                "link": entry.get("link", "No Link"),
                "published": entry.get("published", "Unknown Date"),
            }

            articles.append(article)
    return articles

if __name__ == "__main__":
    news = fetch_news()
    print(f"Before filter: {len(news)}")

    news = filter_articles(news)
    print(f"After filter: {len(news)}")
    print("\n==== Latest Cyber News ====\n")

    for i, article in enumerate(news, start=1):
        print(f"{i}. {article['title']}")
        print(f"   Published: {article['published']}\n")
        print(f"   Link: {article['link']}")
        print()
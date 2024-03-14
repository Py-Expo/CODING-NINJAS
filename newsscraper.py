import feedparser

feed_url=""
def scrape_google_news_rss(url):
    try:
        feed = feedparser.parse(url)
        articles = []
        for entry in feed.entries:
            title = entry.title
            link = entry.link
            if title and link:
                articles.append({'title': title, 'link': link})
        return articles
    except Exception as e:
        print(f"Error scraping RSS feed: {e}")
        return []


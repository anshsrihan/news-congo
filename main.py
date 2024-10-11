import feedparser
from flask import Flask, render_template, request
import ssl

# Bypass SSL verification(had to do this since I was having problems with my certificate and without this was unable to call the data using Rss feeds)
ssl._create_default_https_context = ssl._create_unverified_context

app = Flask(__name__)

# Link to all the RSS feeds
RSS_FEEDS = {
    'Mint': 'https://www.livemint.com/rss/companies',
    'Yahoo': 'https://finance.yahoo.com/news/rssindex',
    'Financial Express': 'https://www.financialexpress.com/rss',
    'Techcrunch': 'https://techcrunch.com/feed/'
}
#create a dictionary of RSS feeds
@app.route("/")
def index():
    articles = []
    for source, feed in RSS_FEEDS.items():
        parsed_feed = feedparser.parse(feed)
        entries = [(source, entry) for entry in parsed_feed.entries]
        articles.extend(entries)

    # Sort articles by publication date, handling missing 'published' attribute
    articles = sorted(articles, key=lambda x: x[1].published_parsed, reverse=True)

    # Pagination logic
    page = request.args.get('page', 1, type=int)
    per_page = 10
    total_articles = len(articles)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_articles = articles[start:end]

    return render_template('index.html', paginated_articles=paginated_articles, page=page, total_page=(total_articles + per_page - 1) // per_page)

@app.route("/Search")
def search():
    query = request.args.get("query", "").strip()
    articles = []

    for source, feed in RSS_FEEDS.items():
        parsed_feed = feedparser.parse(feed)
        entries = [(source, entry) for entry in parsed_feed.entries]
        articles.extend(entries)

    # Normalize the query to lowercase
    query_lower = query.lower()
    result = [article for article in articles if 
              query_lower in article[1].title.lower() ]

    return render_template('search.html', articles=result, query=query)

if __name__ == "__main__":
    app.run(debug=True)
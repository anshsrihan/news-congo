import feedparser
#import feedparser
import ssl

# Bypass SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

feed_url = 'https://www.livemint.com/rss/companies'
parsed_feed = feedparser.parse(feed_url)
print(f"Parsed Feed: {parsed_feed}")
if parsed_feed.bozo:
    print("Parsing error detected:", parsed_feed.bozo_exception)
else:
    print("Feed parsed successfully.")
if parsed_feed.entries:
    print(f"First entry title: {parsed_feed.entries[0].title}")
else:
    print("No entries found in the feed.")

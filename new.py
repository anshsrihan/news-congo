import time
import feedparser
import ssl
import urllib.request
from http.client import RemoteDisconnected

feed_url = "https://nsearchives.nseindia.com/content/RSS/Insider_Trading.xml"

# Disable SSL certificate verification
context = ssl._create_unverified_context()

# Build an opener with the HTTPSHandler that uses the context
https_handler = urllib.request.HTTPSHandler(context=context)
opener = urllib.request.build_opener(https_handler)
urllib.request.install_opener(opener)

for attempt in range(3):  # Retry 3 times
    try:
        # Parse the feed
        parsed_feed = feedparser.parse(feed_url)
        print(f"Parsed Feed: {parsed_feed}")
        break  # Exit the loop if successful
    except RemoteDisconnected:
        print(f"Connection lost, retrying... (Attempt {attempt + 1}/3)")
        time.sleep(5)  # Retry after a delay
    except Exception as e:
        print(f"Error: {e}")
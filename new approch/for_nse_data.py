# Step 2: Download the appropriate WebDriver for your browser and ensure it's in your PATH.
# For example, download ChromeDriver from https://sites.google.com/a/chromium.org/chromedriver/downloads

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Step 4: Initialize the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Step 5: Navigate to the feed URL
    feed_url = 'https://nsearchives.nseindia.com/content/RSS/Insider_Trading.xml'
    driver.get(feed_url)

    # Step 6: Extract the feed data
    # Assuming the feed data is in the page source as XML
    feed_data = driver.page_source

    # Step 7: Print the extracted data
    print(feed_data)
finally:
    # Step 8: Close the browser
    driver.quit()

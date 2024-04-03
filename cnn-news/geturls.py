from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..globalresource import getArchiveURL
from ..globalresource import articlestojson
import csv
import time


def getURLS(NUMBER_OF_URLS=1000):
    # Define Chrome options
    chrome_options = Options()
    # chrome_options.add_argument('--headless')  # Uncomment if you want to run Chrome in headless mode

    # Set the path to the chromedriver
    service = Service(executable_path="../chromedriver-mac-arm64/chromedriver")

    # Initialize the driver with the service object and options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Go to the desired website
    driver.get("https://www.foxnews.com/category/us/crime")

    # Initialize an empty list to store the scraped hrefs
    scraped_hrefs = []

    # Initialize the CSV file
    csv_file = open('data/urls.csv', 'w', newline='', encoding='utf-8')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['URL'])  # Write the header

    try:
        while len(scraped_hrefs) < NUMBER_OF_URLS:
            # Find all <h4> tags with class 'title' inside 'article' tags and get their 'href' attributes
            articles = driver.find_elements(By.CSS_SELECTOR, 'article h4.title a')
            for article in articles:
                href = article.get_attribute('href')
                if href not in scraped_hrefs:
                    scraped_hrefs.append(href)
                    csv_writer.writerow([href])  # Write to CSV file

            # Check if we have 50 urls, if so break out of the loop
            if len(scraped_hrefs) >= NUMBER_OF_URLS:
                break

            # Wait for the "Show More" button to be clickable and then click it
            show_more_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.button.load-more.js-load-more a'))
            )
            driver.execute_script("arguments[0].click();", show_more_button)

            # Wait for the page to load; adjust the sleep time if necessary
            time.sleep(1)

    finally:
        csv_file.close()
        driver.quit()

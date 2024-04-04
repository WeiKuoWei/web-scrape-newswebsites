from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire import webdriver

import undetected_chromedriver as uc
import csv
import time
import pandas as pd
import credentials
config = credentials.get()

API_KEY = config['SCRAPERAPI_KEY']

proxy_options = {
  'proxy': {
    "http": f"scraperapi:{API_KEY}@proxy-server.scraperapi.com:8001",
    "https": f"scraperapi:{API_KEY}@proxy-server.scraperapi.com:8001"
  }
}

config = {
    'apnews':'div.PageList-items div.PageList-items-item',
    'bbc':'div[data-testid="liverpool-card"]',
    'cnn':'div.stack', # need to double check
    'dailymail':'h2.linkro-darkred',
    'foxnews':'h4.title',
    'huffpost':'div.zone__content div.card.card--standard.js-card',
    'nypost':'h3.story__headline.headline.headline--archive',
    'nytimes':'div.css-13mho3u li.css-18yolpw',
    'reuters':'li[data-testid="four_columns"],li[data-testid="three_columns"]',
    'washingtontimes':'h2.article-headline',
}


def createDriver():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox") # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage") # This flag is used to disable the use of the /dev/shm shared memory file system in Chrome.
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--windox-size=800,600")
    service = Service(executable_path="../chromedriver-mac-arm64/chromedriver")

    driver = uc.Chrome(service=service, options=chrome_options, seleniumwire_options=proxy_options)
    return driver

def getURLS(file_path, export_csv_name, site_name):
    print("Getting URLs for:", site_name)
    # import the website link from a CSV called urls.csv
    site_list = []
    with open('data/'+site_name+'/'+file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        # next(csv_reader) # Skip the header if there is one
        for row in csv_reader:
            site_list.append(row[1])
    try:
        # Remove wayback machine links from the urls
        processed_links = []  
        for site in site_list:
            driver = createDriver()
            driver.get(site)

            # Find all <h2> elements with the class "linkro-darkred" and extract the hrefs
            articles = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((
                    By.CSS_SELECTOR, 
                    config[site_name]
                ))
            )
            links = [article.find_element(By.CSS_SELECTOR, 'a').get_attribute('href') for article in articles]

        
            for link in links:
                # Locate the index that contains 'https'
                print(link)
                index = link.find('https')
                processed_link = link[index:]
                processed_links.append(processed_link)

            # Close the driver after you're done
            driver.quit()

    except Exception as e:
        print("Error: ", e)


    # Append the URLs to a CSV file
    with open('data/'+site_name+'/'+export_csv_name, 'a', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        for link in processed_links:
            csv_writer.writerow([link])
        
    # drop the duplicates 
    df = pd.read_csv('data/'+site_name+'/'+export_csv_name, header=None)
    df.drop_duplicates(subset=0, inplace=True)
    df.to_csv('data/'+site_name+'/'+export_csv_name, index=False, header=None)
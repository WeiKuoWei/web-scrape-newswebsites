from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv
import time
import pandas as pd



# Define Chrome options
chrome_options = Options()
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox") # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage") # This flag is used to disable the use of the /dev/shm shared memory file system in Chrome.
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--windox-size=800,600")

# prefs = {"profile.managed_default_content_settings.images": 2} # 2: Block all images; 0: Show all images 
# chrome_options.add_experimental_option("prefs", prefs)
service = Service(executable_path="../chromedriver-mac-arm64/chromedriver")


def getURLS(file_path, export_csv_name):
    # import the website link from a CSV called urls.csv
    site_list = ["https://nypost.com/us-news/"]
    # with open("data/" + file_path, 'r', encoding='utf-8') as csv_file:
    #     csv_reader = csv.reader(csv_file)
    #     # next(csv_reader) # Skip the header if there is one
    #     for row in csv_reader:
    #         site_list.append(row[1])

    # Process the links
    processed_links = []        
    
    for site in site_list:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(site)

        # Find all <h2> elements with the class "linkro-darkred" and extract the hrefs
        articles = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h3.story__headline.headline.headline--archive')))
        links = [article.find_element(By.CSS_SELECTOR, 'a').get_attribute('href') for article in articles]

        for link in links:
            # Locate the index that contains 'https'
            index = link.find('https')
            processed_link = link[index:]
            processed_links.append(processed_link)

        # Append the URLs to a CSV file
        with open('data/' + export_csv_name, 'a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            for link in processed_links:
                csv_writer.writerow([link])
            
        # drop the duplicates 
        df = pd.read_csv('data/' + export_csv_name, header=None)
        df.drop_duplicates(subset=0, inplace=True)

        # drop the rows that contain the word 'video'
        df = df[~df[0].str.contains('video')]

        df.to_csv('data/' + export_csv_name, index=False, header=None)

        # Close the driver after you're done
        driver.quit()

        # pause the script for 5 seconds
        time.sleep(10)

getURLS("urls-wayback.csv", "urls_uncleaned.csv")
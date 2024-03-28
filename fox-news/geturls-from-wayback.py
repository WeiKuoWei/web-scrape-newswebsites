from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv
import time



# Define Chrome options
chrome_options = Options()
service = Service(executable_path="../chromedriver-mac-arm64/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

def getURLS(file_path, export_csv_name):
    # import the website link from a CSV called urls.csv
    site_list = []
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        # next(csv_reader) # Skip the header if there is one
        for row in csv_reader:
            site_list.append(row[0])

    # Process the links
    processed_links = []        
    
    for site in site_list:
        driver.get(site)

        # Wait for the page to load and find all articles
        articles = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'article h4.title')))

        # Extract href attributes
        links = [article.find_element(By.CSS_SELECTOR, 'a').get_attribute('href') for article in articles]

        for link in links:
            # Locate the index that contains 'https'
            index = link.find('https')
            processed_link = link[index:]
            processed_links.append(processed_link)

        # Close the driver after you're done
        driver.quit()

    # Append the URLs to a CSV file
    with open('data/' + export_csv_name, 'a', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        for link in processed_links:
            csv_writer.writerow([link])
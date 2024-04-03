from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import csv
import time

def getURLS(file_path, export_csv_name):
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
    driver = webdriver.Chrome(service=service, options=chrome_options)

    site_list = []
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            site_list.append(row[1])  # Assuming URL is in the first column

    processed_links = []
    
    for site in site_list:
        driver.get(site)
        try:
            # Adjusted selector to match the specific element class
            links_elements = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.container__link.container_lead-plus-headlines-with-images__link'))
            )
            links = [element.get_attribute('href') for element in links_elements]
            processed_links.extend(links)
            with open(export_csv_name, 'a', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)
                for link in processed_links:
                    csv_writer.writerow([link])
        except Exception as e:
            print(f"Error processing site {site}: {e}")

    driver.quit()




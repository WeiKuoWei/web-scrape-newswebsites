from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Define Chrome options (if any)
chrome_options = Options()
# chrome_options.add_argument('--headless') # Uncomment if you don't want the browser window to open

# Set the path to the chromedriver
service = Service(executable_path="./chromedriver-mac-arm64/chromedriver")

# Initialize the driver with the service object and options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Go to the desired website
driver.get("https://www.foxnews.com/category/us/crime")

# Wait for the articles to be loaded
wait = WebDriverWait(driver, 10)
articles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'article h4.title a')))

# Extract href attributes
hrefs = [article.get_attribute('href') for article in articles]

# Save the hrefs to a CSV file
with open('article_links.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['URL'])  # header row
    for href in hrefs:
        writer.writerow([href])  # data rows

# Close the driver
driver.quit()

print(f'Successfully saved {len(hrefs)} links to article_links.csv')

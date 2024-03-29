import time
import sys

from geturls_from_wayback import getURLS
from cleaner import cleanURLS
from getarticles import articlestojson
from wayback_machine import getArchiveURL

# FILE_PATH = 'data/urls_cleaned.csv'
# NUMBER_OF_URLS = 5000
URL_NAME = "https://www.foxnews.com/category/us/crime"
START_YEAR = 2021
END_YEAR = 2021

current_time = time.time()

def updateTime(function_name=""):
    global current_time

    end_time = time.time()
    print("Total time taken for {0} : {1}s".format(function_name, (end_time - current_time)))
    current_time = end_time


def main():
    print("Program started")
    
    try:
        # # get archive urls with wayback machine
        # getArchiveURL(URL_NAME, START_YEAR, END_YEAR, "data/urls-wayback.csv")
        # updateTime("getArchiveURL")

        # get urls from fox news
        getURLS("urls-wayback.csv", "urls_uncleaned.csv")
        updateTime("getURLS")

        # # clean urls
        # cleanURLS("urls_uncleaned.csv", "urls_cleaned.csv")
        # updateTime("cleanURLS")

        # # get articles
        # articlestojson("urls_cleaned.csv")
        # updateTime("articlestojson")
    
    except Exception as e:
        print("Error: ", e)

    print("Program ended")

if __name__ == "__main__":
    main()


# 1812 articles for 1761 seconds
# roughly 25% of the urls are video urls
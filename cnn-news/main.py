from geturls import getURLS
from cleaner import cleanURLS
from getarticles import articlestojson
import time

FILE_PATH = 'data/urls_cleaned.csv'
NUMBER_OF_URLS = 5000

def main():
    # # save current time as integer
    # current_time = time.time()
    # print("Program has started")
    # # getURLS(NUMBER_OF_URLS)
    # print("URLs have been scraped")
    # end_time = time.time()
    # print("Total time taken for scraping fox news: ", (end_time - current_time), "s")
    # # cleanURLS()
    # print("URLs cleaned")

    current_time = time.time()
    articlestojson(FILE_PATH)
    print("Articles have been scraped")
    end_time = time.time()
    print("Total time taken for scraping articles: ", (end_time - current_time), "s")


if __name__ == "__main__":
    main()


# 1812 articles for 1761 seconds
# roughly 25% of the urls are video urls
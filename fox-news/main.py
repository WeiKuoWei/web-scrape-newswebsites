# import functions from get-urls.py
from geturls import getURLS

# import functions from cleaner.py
from cleaner import cleanURLS

def main():
    # getURLS()
    # print("URLs have been scraped")
    cleanURLS()
    print("URLs cleaned")


if __name__ == "__main__":
    main()
# extract and store are two phases of webscraping
# extract :  getting url of webpage, analyzing page source and extracting info
# store : we can store in any file or SQL data bases


#MySQL Queries
# INSERT INTO events VALUES ('Tigers', 'Tigers City', '2023.10.14')
# SELECT * FROM events WHERE Date='2023.10.14'
# DELETE FROM events WHERE 'Band name'='Tiger'

import requests
import selectorlib
url = "https://programmer100.pythonanywhere.com/tours/"

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

def send_email():
    print("email sent")


if __name__ == "__main__":
    scraped = scrape(url)
    extracted = extract(scraped)
    print(extracted)
    if extracted != "No Upcoming Tours":
        send_email()
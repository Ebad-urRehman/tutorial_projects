# extract and store are two phases of webscraping
# extract :  getting url of webpage, analyzing page source and extracting info
# store : we can store in any file or SQL data bases


#MySQL Queries
# INSERT INTO events VALUES ('Tigers', 'Tigers City', '2023.10.14')
# SELECT * FROM events WHERE Date='2023.10.14'
# DELETE FROM events WHERE 'Band name'='Tiger'

import requests
import selectorlib
import smtplib, ssl
import os
import time
import sqlite3

url = "https://programmer100.pythonanywhere.com/tours/"

# establish a connection and a cursor
connection = sqlite3.connect("Data.db")


def scrape(url):
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["tours"]
    return value

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "ebadinfalltraders@gmail.com"
    password = os.getenv("mailing_app_password")    
    receiver = "ebadinfalltraders@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


def store(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events Values(?,?,?)", row)
    connection.commit() # save changes to database

def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE 'Band name'=? AND 'City name'=? AND Date=?", (band, city, date))
    extracted_row = cursor.fetchall()
    return extracted_row

if __name__ == "__main__":
    while True:
        scraped = scrape(url)
        extracted = extract(scraped)
        if extracted != "No upcoming tours":
            row = read(extracted)
            print(extracted)
            if not row: # true if len(row) is not 0 some cells have any value
                store(extracted)
                send_email(message=f"New event found\n {extracted}")
        time.sleep(2)
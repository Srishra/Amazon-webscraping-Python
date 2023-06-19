import datetime
import csv
import time
import requests
from bs4 import BeautifulSoup
from time import sleep
import smtplib
import re

desired_price = # Enter your desired price value as an Integer

# Code for sending the email...

def send_email(title, price):
    # Set up your email configuration
    sender_email = ""
    receiver_email = ""
    password = "*app-password"

    # Compose the email message
    subject = f"Price Drop Alert: {title}"
    body = f"The price of {title} has changed. The current price is Rs. {price}."
    message = f"Subject: {subject}\n\n{body}"

    # Send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


# Code for scraping the website, checking the price, and sending the email...

def check_price():
    URL = 'https://www.amazon.in/Apple-iPad-Air-10-9-inch-27-69-Wi-Fi/dp/B09V471196/ref=sr_1_7?crid=2HVGY21MDU3TP&keywords=ipad&qid=1687177179&sprefix=ipad+%2Caps%2C398&sr=8-7'

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "X-Amzn-Trace-Id": "Root=1-647c0c56-487c79f51b90a6cb496af837"
    }

    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find(id='productTitle').get_text().strip()
    price = soup2.find(class_="a-price-whole").get_text().strip()

    today = datetime.datetime.now()
    current_time = datetime.datetime.now().strftime("%H:%M")

    # Remove comma, newline characters, and non-breaking space from price
    price = re.sub("\D", "", price)

    print(price)

    # Convert price to integer for comparison
    try:
        price_int = int(price)
    except ValueError:
        print("Unable to convert price to integer:", price)
        return

    if price_int == desired_price:
        send_email(title, price)

    header = ['Title', 'Price', 'Date', 'Time']
    data = [title, price, today, current_time]

    # Check if the file is empty and write the header row
    with open('AmazonWebScraper_ipad.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        if f.tell() == 0:
            writer.writerow(header)
        writer.writerow(data)


while True:
    check_price()
    time.sleep(86400)

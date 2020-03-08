# -*- coding: utf-8 -*-
"""
The following program checks the price every 1 hour of a product on Amazon.
Slightly modified implementation of - https://www.youtube.com/watch?v=Bg9r_yLk7VY

You will have to enter the appropriate To/From email addresses in the code below (lines 45,46), and the password of your preferred email
service. This program assumes use of Gmail (line 34).
"""

import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/DEWALT-DWMT75049-Mechanics-Tools-Piece/dp/B01BHJE0J4'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

def check_price():
    
    page = requests.get(URL,headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    #title = soup2.find(id= "productTitle").get_text()
    #print(title.strip())

    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:])

    if converted_price <= 149:
        send_mail()
        
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('**Your email**','**Password/App Password**')
    
    subject = 'Price fell down'
    body = 'Check the amazon link https://www.amazon.com/DEWALT-DWMT75049-Mechanics-Tools-Piece/dp/B01BHJE0J4'
    
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
            '**From email**',
            '**To email**',
            msg
            )
    print('Hey, email has been sent!')
    server.quit()


while(True):
    check_price()
    time.sleep(3600)

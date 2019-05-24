from bs4 import BeautifulSoup
from selenium import webdriver
import smtplib, ssl
import time
import datetime

def sendMail():
    port = 465  # For SSL
    context = ssl.create_default_context()
    sender_email=''
    receiver_email=''
    body=""
    subject=""
    message='To: {}\r\nSubject: {}\r\n\r\n{}'.format(receiver_email, subject, body)
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("", "")
        server.sendmail(sender_email, [receiver_email], message)

while True:
    print(datetime.datetime.now())
    browser= webdriver.Chrome('chromedriver.exe') #chrome
    browser.get('https://www2.hm.com/no_no/productpage.0749333001.html')#item page
    html=browser.page_source
    bs = BeautifulSoup(html, 'html.parser')
    for item in bs.find_all():
        if "data-code" in item.attrs:
            if item.attrs['data-code']=='0749333001005': #locate the size identifier
                if len(item.find_all(text='Utsolgt'))==0: #not out of stock
                    sendMail()
                    break
    browser.close()
    time.sleep(60)

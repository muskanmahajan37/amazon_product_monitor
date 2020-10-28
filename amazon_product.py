
import requests
import getpass
import re
import smtplib
from bs4 import BeautifulSoup

def send_mail():
    try:
        server =smtplib.SMTP('smtp.gmail.com', 587)

        server.ehlo()

        server.starttls()

        server.ehlo()

        pswd = getpass.getpass()

        server.login("rohan.rohankumar.kumar51@gmail.com",pswd)

        subject='ROHAN, price fell down of one plus 7.'

        body = 'check the price of one plus 7 it fell down https://www.amazon.in/Test-Exclusive-608/dp/B07HGBMJT6/ref=lp_16739541031_1_1?s=electronics&ie=UTF8&qid=1562147796&sr=1-1'

        msg = f"SUBJECT:{subject} \n\n {body} "

        server.sendmail("rohan.rohankumar.kumar51@gmail.com","rohan.rohankumar.kumar51@gmail.com",msg)

        print("#"*90)

        print("mail has been send successfully!!!!")

        print("#"*90)
    except:
        print("couldnot send the mail")
        print("#"*90)

def check_price():
    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()

    price = soup.find(id='priceblock_dealprice').get_text()

    price_2= price[2:]

    price_3 = re.sub('[\,.]', '', price_2)

    price_4 = int(price_3)/100

    converted_price = int(price_4)

    if (converted_price <= expected_price):
        send_mail()

    print("the current price of the product is : " + str(converted_price))
    print("#"*90)

    print("the product title is : " + title.strip())
    print("#"*90)
    input("enter to quit the programme........")

print("#"*150)
print("example of url is : https://www.amazon.in/Test-Exclusive-608/dp/B07HGBMJT6/ref=lp_16739541031_1_1?s=electronics&ie=UTF8&qid=1562147796&sr=1-1")

print("#"*150)
URL=input("please enter the url of the product page : ")
#URL = 'https://www.amazon.in/Test-Exclusive-608/dp/B07HGBMJT6/ref=lp_16739541031_1_1?s=electronics&ie=UTF8&qid=1562147796&sr=1-1'

print("#"*150)
price_0=input("please enter your expected price: ")
price_1 = re.sub('[\,]', '', price_0)
expected_price = int(price_1)

#print(expected_price)

print("#"*90)

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
check_price()

print("changes has been made")


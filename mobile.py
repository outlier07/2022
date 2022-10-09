import requests
import os
from bs4 import BeautifulSoup
import smtplib      # simple mail transfer protocol

url_note11 = "https://www.amazon.in/dp/B09T39K9YL/?coliid=I8ULCYCWPW7J2&colid=22A2JM4X9UDIB&psc=1&ref_=lv_ov_lig_dp_it"
url_note10 = "https://www.amazon.in/dp/B089MT35TK/?coliid=I3AO1U5OD5G5JM&colid=22A2JM4X9UDIB&psc=1&ref_=lv_ov_lig_dp_it"

headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
}
dprice = 20001
password = os.environ.get("password")
def check_price():
    page = requests.get(url_note11, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[2:5])

    if converted_price < dprice :
        send_mail()
    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('hiddenoutliers@gmail.com', password)         # need to allow less secure app for google
    subject = 'Price fell down below Rs. 20k!!!'
    body = 'Check this out, Hurry !!!  {url_note11}'

    msg = f"Subject: {subject}\n\n {body}"

    server.sendmail(
        'hiddenoutliers@gmail.com',
        'shukla.prashant689@gmail.com',
        msg
    )

    print("Email has been sent successfully.")
    print("Hurry !!! check your wishlist now. ")

    server.quit()

check_price()


import requests
from bs4 import BeautifulSoup
URL = 'https://www.amazon.in/Logitech-MX-Master-Ultrafast-Customisation/dp/B07YXNDK6X/ref=sr_1_1?crid=2QCTLPKZ6M6GI&dchild=1&keywords=mx+master+3&qid=1623586411&sprefix=mx+%2Caps%2C292&sr=8-1'

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}

def check_price():
    page = requests.get(URL,headers=headers)
    soup = BeautifulSoup(page.content,'html.parser')

    title=soup.find(id='productTitle').get_text()
    price=soup.find(id="priceblock_ourprice").get_text()
    price=price.replace(',','')
    converted_price = float(price[1:6])
    print('PRICE:',converted_price)
   

check_price()

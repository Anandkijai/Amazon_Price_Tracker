import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://www.amazon.com/EDUCIRO-Castle-Building-Kit-Collectible/dp/B09DFLXJ4F/ref=sr_1_1_sspa?crid=3W5CUCX3ZURNK&keywords=harry+potter+lego&qid=1673548294&sprefix=harry%2Caps%2C189&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUEsxQUwzUTJRRVZKJmVuY3J5cHRlZElkPUEwNTE1NTk0MUtCUkg5U0UyQVhXOSZlbmNyeXB0ZWRBZElkPUEwODA3NDY5Mzc2M0REWE5ITEJDQyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
headers = {
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.amazon.com/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

page = ''
while page == '':
    try:
        response = requests.get(url=URL, headers=headers)
        break
    except:
        print("Connection refused by the server..")
        print("Let me sleep for 5 seconds")
        time.sleep(5)
        continue


soup = BeautifulSoup(response.text, "lxml")
print(soup.prettify())

price = float(soup.find(name="span", class_="a-offscreen").getText().split("$")[1])
print(price)
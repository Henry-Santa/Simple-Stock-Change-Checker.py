import requests as r
from requests.exceptions import ConnectionError
import time
from colorama import init
init()

from colorama import Fore, Back, Style

ticker = input("Ticker of stock : ")

url = f'https://api.nasdaq.com/api/quote/{ticker}/info'#?assetclass=stocks'
urlNew = "https://www.google.com/"

params = {
    "assetClass" : "stocks"
}
headers = {
    'authority': 'api.nasdaq.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,th;q=0.8',
    'origin': 'https://www.nasdaq.com',
    'referer': 'https://www.nasdaq.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
}
global currPrice
currPrice = 0

#print(response.status_code)
def Work():
    global currPrice
    try:
        while True:
            response = r.get(url, params=params, headers=headers, verify=False)
            
            nPrice = float(response.json()["data"]["primaryData"]["lastSalePrice"].replace("$", ""))
            
            if nPrice < currPrice:
                currPrice = nPrice
                print(Fore.RED, "Current price : $", currPrice)
            if nPrice > currPrice:
                currPrice = nPrice
                print(Fore.GREEN, "Current price : $", currPrice)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print(Fore.MAGENTA, "Monitoring Over, Final Price = ", currPrice)
        print(Fore.RESET, Back.RESET)
    except ConnectionError as e:
        #print("Connection Failed : ", e)
        Work()

import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    Work()

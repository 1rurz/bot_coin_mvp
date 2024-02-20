import os
import sys
sys.path.append(os.path.dirname(os.path.abspath("file")))
from config.config_2 import headers
import requests


def get_bybit(name):
    try:
        response = requests.get(url=f"https://api.bybit.com/v5/market/tickers?category=spot&symbol={name}USDT", headers=headers).json()
        return round(float(response['result']['list'][0]['lastPrice']),2)
    except Exception as e:
        print(f"ошибка:{e}, проверьте введенные данные")
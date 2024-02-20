import os
import sys
sys.path.append(os.path.dirname(os.path.abspath("file")))
from config.config_2 import headers
import requests


def get_binance(name):
    try:
        response = requests.get(url=f"https://api.binance.com/api/v3/ticker/price?symbol={name}USDT", headers=headers).json()
        return round(float(response['price']),2)
    except Exception as e:
        print(f"ошибка:{e}, проверьте введенные данные")





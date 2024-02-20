import os
import sys
sys.path.append(os.path.dirname(os.path.abspath("file")))
from config.config_2 import headers
import requests


def get_kraken(name):
    try:
        response = requests.get(url=f"https://api.kraken.com/0/public/Ticker?pair={name}USDT", headers=headers).json()
        if name == ("BTC"):
            return round(float(response['result']["XBTUSDT"]["c"][0]),2)
        else:
            return round(float(response['result'][f"{name}USDT"]["c"][0]),2)
    except Exception as e:
        print(f"ошибка:{e}, проверьте введенные данные")



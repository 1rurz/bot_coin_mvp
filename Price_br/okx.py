import os
import sys
sys.path.append(os.path.dirname(os.path.abspath("file")))
import requests
from config.config_2 import headers
import requests 


def get_okx(name):
    try:
        response = requests.get(url=f"https://www.okx.com/api/v5/market/index-tickers?instId={name}-USDT", headers=headers).json()
        return round(float(response["data"][0]["idxPx"]),2)
    except Exception as e:
        print(f"ошибка:{e}, проверьте введенные данные")
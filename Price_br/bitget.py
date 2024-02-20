import os
import sys
sys.path.append(os.path.dirname(os.path.abspath("file")))
from config.config_2 import headers
import requests
    

def get_bitget(name):
    try:
        response = requests.get(url=f"https://api.bitget.com/api/v2/mix/market/ticker?productType=COIN-FUTURES&symbol={name}USD", headers=headers).json()
        return round(float(response["data"][0]["lastPr"]),2)
    except Exception as e:
        print(f"ошибка:{e}, проверьте введенные данные")
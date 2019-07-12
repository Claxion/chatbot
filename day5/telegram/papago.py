import requests 
from decouple import config
from pprint import pprint

def papagoTranslate(text) : 
    url = "https://openapi.naver.com/v1/papago/n2mt"
    headers = {
        "X-Naver-Client-Id" : config('NAVER_ID'),
        "X-Naver-Client-Secret" : config('NAVER_SECRET')
    }

    data = {
        "source" : "ko",
        "target" : "en",
        "text" : text
    }

    res = requests.post(url, headers = headers, data = data)
    pprint(res.json())
    translatedtext = res.json().get("message").get("result").get("translatedText")
    return translatedtext
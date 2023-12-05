

url = "http://192.168.31.61:8080/api/ads/"

import requests

responce = requests.get(url)

data =responce.json()

TEXT = [f"""
ID: {data[0]['id']}
TITLE: {data[0]['title']}
DESCRIOTION: {data[0]['description']}
PRICE : {data[0]['price']}
CONTACT: {data[0]['contact']}
CATEGORY: {data[0]['category']}
"""]

print(TEXT)


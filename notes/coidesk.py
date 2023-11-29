import requests
import json

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
# print(response.json())
data = response.json()
with open ("btcdump.json", "w") as fp:
    json.dump(data, fp)

euroPriceObject = data["bpi"]["EUR"]
rate = euroPriceObject["rate"]
print(euroPriceObject)
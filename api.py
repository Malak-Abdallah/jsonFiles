import json
from urllib.request import urlopen

# websites return json from APIs:
# grab json from API nd pare that data:

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read() # the response we got from the website

data = json.loads(source)

# print(json.dumps(data, indent=2))

usd_rates = dict()

for item in data['list']['resources']:
    name = item['resource']['fields']['name']
    price = item['resource']['fields']['price']
    usd_rates[name] = price

print(50 * float(usd_rates['USD/EUR']))

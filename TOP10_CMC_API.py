 #This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'10',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'e2ca7f50-cc48-4b25-b9ca-117b5ea0b1e9',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  count = 0
  data = json.loads(response.text)
  for each in data['data']:
    count = count + 1
    print (count,each['symbol'], each['name'])

  #print(data['data'][2]['name'])
  #print(json.dumps(data, indent=4))

except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

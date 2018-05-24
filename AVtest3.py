# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 14:19:23 2018

@author: john3
"""


#import alpha_vantage
import requests
import json
import pprint
import json
import urllib.request

url="https://www.alphavantage.co/query"
outFile="cheese.csv"
function="TIME_SERIES_DAILY"
symbol="MSFT"
api_key="E82V6HPLXDMUN5TM"
datatype="csv"

data={"function": function,
      "symbol": symbol,
      "apikey":api_key,
      "datatype":datatype,
      }

page=requests.get(url, params=data)
#pprint.pprint(page.json())
with open(outFile, "w") as oF:
    oF.write(page.text.replace('\r\n','\n'))





QUERY_URL = "https://www.alphavantage.co/query?function={REQUEST_TYPE}&apikey={KEY}&symbol={SYMBOL}"
API_KEY = "AN ACTUAL KEY"

def _request(symbol, req_type):
    with urllib.request.urlopen(QUERY_URL.format(REQUEST_TYPE=req_type, KEY=API_KEY, SYMBOL=symbol)) as req:
        data = req.read().decode("UTF-8")
    return data

def get_daily_data(symbol):
    return json.loads(_request(symbol, 'TIME_SERIES_DAILY'))

    apple = get_daily_data('AAPL', request_type=request_type_url, api_key=my_key)
    print(apple["Time Series (Daily)"]["2018-03-02"])
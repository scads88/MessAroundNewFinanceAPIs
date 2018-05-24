# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 00:13:27 2018

@author: john3
"""
#import alpha_vantage
import requests
import json
import pprint

url="https://www.alphavantage.co/query"
outFile="cheese.csv"
function="TIME_SERIES_DAILY"
symbol="MSFT"
api_key="AlphaVantageAPIkey.txt"
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
print(page.status_code)
#pprint.pprint(page.json())
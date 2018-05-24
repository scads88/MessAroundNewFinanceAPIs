# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 15:27:59 2018

@author: john3
"""

import requests
import json
import pandas as pd
import pprint
import os


dick=os.path.basename(__file__)
print (dick)
dick=str(dick)
print(dick)
print(__file__)


url="https://www.alphavantage.co/query"
dick.replace(".py", ".csv")

#function="TIME_SERIES_DAILY"
function="BATCH_STOCK_QUOTES"
symbol="MSFT"
#symbol="MSFT,FB,ADH"
api_key="AlphaVantageAPIkey.txt"
datatype="csv"

data={"function": function,
      "symbol": symbol,
      "apikey":api_key,
      "datatype":datatype,
      }

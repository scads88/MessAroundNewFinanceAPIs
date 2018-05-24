# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 14:51:04 2018

@author: john3
"""

import requests
import pandas as pd

url = "https://www.alphavantage.co/query"
api_key = "E82V6HPLXDMUN5TM"
symbol = "MSFT"
function = "TIME_SERIES_DAILY"
data = {"apikey": api_key,
        "symbol": symbol,
        "function": function
       } 
page = requests.get(url, params=data)
dictionary = page.json()
print(dictionary)
#keys = list(dictionary.keys())
#print(keys)
#print(keys)
#series = keys[1]
#dataframe = pd.DataFrame.from_dict(dictionary[series], orient='index')
#print(dataframe)
#dataframe = dataframe.astype(float)
#dataframe['1. open'].plot()
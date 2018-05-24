# -*- coding: utf-8 -*-
"""
Created on Tue May 22 14:34:54 2018

@author: john3
"""

import alpha_vantage
import requests
import pandas as pd
import matplotlib.pyplot as plt
import json
import os
import datetime

from alpha_vantage.timeseries import TimeSeries
ts = TimeSeries(key="E82V6HPLXDMUN5TM")
# Get json object with the intraday data and another with  the call's metadata
data, meta_data = ts.get_intraday('GOOGL')
#print(data)

balls=TimeSeries(key="E82V6HPLXDMUN5TM")
data, meta_data=ts.get_batch_stock_quotes("GOOGL,MSFT")
print(data)

box=["WMT", "AAPL"]
for i in box:
    data2, meta_data2=ts.get_daily(i)
    print(meta_data2)


#print(datetime.date())
bullshit=str(os.path.basename(__file__))
#print(bullshit)
bullshit=bullshit[:-3]
#print(bullshit)


#CALL/CRAFT "message" you will send to "API" and...
url= "https://www.alphavantage.co/query"
ticker=["AAPL", "MSFT"]#could do a list ["MSFT", "AAPL"]
outputsize="compact" 
#outputsize="full"
datatype="json" #or json
function="TIME_SERIES_DAILY_ADJUSTED"
apikey="E82V6HPLXDMUN5TM"

#...what information you expect to get back from it
#Call any output file names
outFile=ticker[0]+"_"+bullshit+"."+datatype
#outFile="bullshit.csv"
#structure for what call
data={"function":function,
      "apikey":apikey,
      "symbol":ticker,
      "outputsize":outputsize,
      "datatype":datatype,
      }

#how call is generated in our format
page=requests.get(url, params=data)

#Drive data into file formats you want
with open(outFile, "w") as oF:
    oF.write(page.text.replace('\r\n','\n'))
    
#Make sure can do this for "n" number of screen 1 explicitly, screen mult explicitly, screen all implicitly
page = requests.get(url, params=data)
dictionary = page.json()
keys = list(dictionary.keys())
series = keys[1]
dataframe = pd.DataFrame.from_dict(dictionary[series], orient='index')

dataframe = dataframe.astype(float)
dataframe["openclosepercentchange"]=((dataframe["1. open"]-dataframe["5. adjusted close"])/dataframe["5. adjusted close"])*100
dataframe["highlowpercentchange"]=((dataframe["2. high"]-dataframe["3. low"])/dataframe["2. high"])*100
#print(dataframe[["openclosepercentchange", "highlowpercentchange"]])

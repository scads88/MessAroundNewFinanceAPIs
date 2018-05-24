# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 00:31:40 2018

@author: john3

Imports modules
Uses alpha vantage API to access stock price data for requested companies
These companies can be one, some, or all




"""




import requests
import pandas as pd
import matplotlib.pyplot as plt
import json
import os
import datetime



#print(datetime.date())
bullshit=str(os.path.basename(__file__))
print(bullshit)
bullshit=bullshit[:-3]
print(bullshit)


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
#print(dataframe["close"])

dataframe = dataframe.astype(float)
dataframe["openclosepercentchange"]=((dataframe["1. open"]-dataframe["5. adjusted close"])/dataframe["5. adjusted close"])*100
#print(dataframe['4. close'])
#print(dataframe["openclosepercentchange"])

dataframe["highlowpercentchange"]=((dataframe["2. high"]-dataframe["3. low"])/dataframe["2. high"])*100


#print(dataframe["openclosepercentchange"], dataframe["highlowpercentchange"])
print(dataframe[["openclosepercentchange", "highlowpercentchange"]])



#correlation matrix/spreadsheet

#other linkages for stuff

#scanning all of the stock market

#heuristic equationo

"""
tickername="AAPL"
percentchangefilter=1
#number of days
## also want to have a subfilter to slice percent change by variations (maybe make it additive?)
style.use("ggplot")
start=dt.datetime.today()-dt.timedelta(days=10)
end=dt.datetime.today()
df=web.DataReader(tickername, "google", start, end)
df["HL_PCT"]=(df["High"]-df["Low"])/df["Low"]*100.0
df["PCT_change"]=(df["Close"]-df["Open"])/df["Open"]*100.0
print(df)
"""

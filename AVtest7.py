# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 20:48:47 2018

@author: john3
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt
import json
import os
import csv
bullshit=str(os.path.basename(__file__))
print(bullshit)
bullshit=bullshit[:-3]
print(bullshit)


#CALL/CRAFT "message" you will send to "API" and...
url= "https://www.alphavantage.co/query"
ticker=["AAPL", "MSFT"]#could do a list ["MSFT", "AAPL"]
outputsize="compact" 
#outputsize="full"
datatype="csv" #or json
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


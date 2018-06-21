# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 23:17:29 2018

@author: john3
"""
import requests
import pandas as pd
import numpy as np
import bs4 as bs

company2infodic={}
totaltickers=["AA", "AAPL", "MSFT"]
for ticker in totaltickers:
    resp=requests.get("https://www.marketwatch.com/investing/stock/"+ticker)
    soup=bs.BeautifulSoup(resp.text, "lxml")
    table=soup.find_all("li", class_="kv__item") #looks for the li (list item feature, usually comes immediately before "class", and also the class_ characteristic (what class is equal to. helps to narrow down)
    for row in table:
        labels=[e.get_text().strip() for e in soup.select(".kv__label")] #pulls the text from the class =kv_label 
        values=[e.get_text().strip() for e in soup.select(".kv__primary ")] #pulls the tex from the class= kv_value
        labels2valuesdic={k:v for k, v in zip( labels, values)} #dictionaries labels and values
        company2infodic[ticker]=labels2valuesdic #dictionaries the company ticker name with respective labels and values
print(company2infodic)


#jam this into the ratios data csv generated
# modify the m's b's and curlyqs to intergers
#figure out how you want to structure it in that csv ( maybe generate its own? obs use marketcap as part of trigger)



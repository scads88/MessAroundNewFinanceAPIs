# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 00:52:09 2018

@author: john3
"""

import requests
import bs4 as bs
import pandas as pd
import numpy as np



resp=requests.get("https://uk.finance.yahoo.com/quote/AA?p=AA")
soup=bs.BeautifulSoup(resp.text, "lxml")
#print(soup)
mkname=soup.find_all("span", {"data-reactid":"51"})
mkvalue=soup.find_all("span", {"data-reactid":"53"})
for i, j in zip(mkname, mkvalue):
    i=i.get_text()
    j=j.get_text()
    print(i, j)

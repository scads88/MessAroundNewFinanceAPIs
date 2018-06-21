# -*- coding: utf-8 -*-
"""
Created on Sat May 26 22:01:29 2018

@author: john3
"""

import bs4 as bs
import requests
import pandas as pd
import numpy as np

url= "https://www.hackerrank.com/domains/python?filters%5Bsubdomains%5D%5B%5D=py-introduction&filters%5Bstatus%5D%5B%5D=unsolved"

bob=requests.get(url)
soup=bs.BeautifulSoup(bob.text, "lxml")
print(soup)

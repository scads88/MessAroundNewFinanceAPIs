import pip
pip.main(["install", "alpha_vantage"])
import requests
import alpha_vantage
import json
import urllib.request
import datetime
"AlphaVantageAPIkey.txt"
QUERY_URL = "https://www.alphavantage.co/query?function={REQUEST_TYPE}&apikey={KEY}&symbol={SYMBOL}"
API_KEY = "AlphaVantageAPIkey.txt"


def _request(symbol, req_type):
    with urllib.request.urlopen(QUERY_URL.format(REQUEST_TYPE=req_type, KEY=API_KEY, SYMBOL=symbol)) as req:
        data = req.read().decode("UTF-8")
    return data

def get_daily_data(symbol):
    return json.loads(_request(symbol, "TIME_SERIES_DAILY"))

print(get_daily_data("AAPL")["Time Series (Daily)"]["2018-03-02"])

import os #be care with this will return true for directories and files
import pandas as pd
import requests
import bs4 as bs
import pickle
import collections
import datetime
import alpha_vantage
import numpy as np
from alpha_vantage.timeseries import TimeSeries
import datetime as dt
import matplotlib.pyplot as plt

###global constants



###Company Evaluation Class
class CompanyEvaluation:
    pass
    #can use class variables instead of hardcoding into methods

    def __init__(self):
        pass
    
    def rawfundamentals(self, ticker):
        self.ticker=ticker
        return ticker
        

    def roundTime(dt=None, roundTo=60): #From Thierry Husson 2012
       if dt == None : dt = datetime.datetime.now()
       seconds = (dt.replace(tzinfo=None) - dt.min).seconds
       rounding = (seconds+roundTo/2) // roundTo * roundTo
       return dt + datetime.timedelta(0,rounding-seconds,-dt.microsecond)
       #print (roundTime(datetime.datetime(2012,12,31,23,44,59,1234),roundTo=15*60))


    def stockprices(self):
        #relates to what the actual prices are doing relative to self and others
        AVkey="E82V6HPLXDMUN5TM"
        totaltickers=["OPK", "DGX", "NVTA", "LH"]
        ts=TimeSeries(key=AVkey, output_format='pandas')
        start=dt.datetime.today()-dt.timedelta(days=100)
        print(roundTime(start))
        end=dt.datetime.today()
        tickerdic={}
        #will be useful to have plt tutorial to address axes, labeling, legends again
        #combined chart, individual chart, multiple timescales, (daily/weekly/monthly)
        #incorporate something in to account for value error
        #incorporate the filter for whether or not generate stock data
        #incorporate aspects to plot by days
        for ticker in totaltickers: 
            data, meta_data=ts.get_daily_adjusted(ticker)
            tickerdic[ticker]=data
            #data2, meta_data2=ts.get_intraday(ticker)
            #print(data)
            tickerdic[ticker]["5. adjusted close"].plot()
            plt.xlabel("Time")
            plt.ylabel("Stock Price ($)")
            plt.axis([start, end, 0, 200])
        print(len(tickerdic["DGX"]))
        plt.title("Testgraph of tickers")
        plt.show()
        return "cheese"
        
        pass
    
    def fundamentalratios(self):
        totaltickers=["OPK", "MYGN", "DGX", "NVTA"]
        valuationlist=["P/E Current", "P/E Ratio (with extraordinary items)", "P/E Ratio (without extraordinary items)", "Price to Sales Ratio", "Price to Book Ratio", "Price to Cash Flow Ratio", "Enterprise Value to EBITDA", "Total Debt to Enterprise Value"]#low better except enterprise value to sales where high better (excluded from this list)
        efficiencylist=["Revenue/Employee", "Income Per Employee", "Receivables Turnover", "Total Asset Turnover"] #high is good
        liquiditylist=["Cash Ratio", "Current Ratio", "Quick Ratio"]#high is good
        profitabilitylist=["Gross Margin", "Operating Margin", "Pretax Margin", "Net Margin", "Return on Assets", "Return on Equity", "Return on Total Capital", "Return on Invested Capital"] #high is better
        capitalstructurelist=["Total Debt to Total Equity", "Total Debt to Total Capital", "Total Debt to Total Assets", "Long-Term Debt to Equity", "Long-Term Debt to Total Capital"]#low is better
        additionalmetricslist=["Revenue (millions USD)", "Net Income (millions USD)", "Sales Growth (most recent)(%)", "Employees", "Market Cap (million)"]#high is better
        totallist=["Revenue/Employee", "Income Per Employee", "Receivables Turnover", "Total Asset Turnover", "Cash Ratio", "Current Ratio", "Quick Ratio",  "Gross Margin", "Operating Margin", "Pretax Margin", "Net Margin", "Return on Assets", "Return on Equity", "Return on Total Capital", "Return on Invested Capital", "Revenue (millions USD)", "Net Income (millions USD)", "Sales Growth (most recent)(%)", "Enterprise Value to Sales"]#excludes capital structure and majority of valuation
        print(totallist)
        #filename="24MayTest"
        #picklefilename=filename+".pickle"
        totaltickers=[ticker.replace(ticker, ticker.lower()) for ticker in totaltickers]
        #dowehaveapickle=os.path.isfile(picklefilename)
        #print(os.path.abspath(picklefilename))
        tickerlabelratiodict=collections.OrderedDict()
        for ticker in totaltickers:
            americaurl="https://www.marketwatch.com/investing/stock/" + ticker + "/profile" #creates the url template for usa stock ticker designation
            resp=requests.get(americaurl) # requests the info on americaurl and sends it to response variable
            soup3=bs.BeautifulSoup(resp.text, "lxml")# turns the resp variable into a soup
            fundamentalratiolabels=[e.get_text() for e in soup3.select(".sixwide .column")] #soup perused and labels and ratios extracted and fed into vbls based upon html characteristics
            fundamentalratios=[e.get_text() for e in soup3.select(".sixwide .data")]
            new_dict=collections.OrderedDict({k:v for k, v in zip(fundamentalratiolabels, fundamentalratios)}) #the selected labels and selected ratios combined togteher into dictionary
            tickerlabelratiodict[ticker.upper()]=new_dict #label:ratio dictionary as values into another dictionary where stock ticker for each group is the key
            #df=pd.DataFrame(tickerlabelratiodict, columns=tickerlabelratiodict)
            df=pd.DataFrame.from_dict(tickerlabelratiodict, orient="columns")# dictionary turned into a pandas dataframe            
            #print(df[0:7][ticker.upper()]["Cash Ratio"])
            df = df.reset_index()
            df.reset_index(drop=True)
            df["Company Ratios"]=df["index"]
            df.index = np.arange(1, len(df) + 1)
            #with open(filename+".pickle", "wb") as f:
                #pickle.dump(df, f)
                #f.close()
        goodbadlist=[]
        for item in df["Company Ratios"]:
            if item in totallist:
                goodbadlist.append("High ~ Better")
            else:
                goodbadlist.append("Low ~ Better")
        df["Opinions"]=goodbadlist
        #df.to_csv("25MayTest.csv")
        return df
    
    def SentimentAnalysis(self):
        pass
        
#pasta=CompanyEvaluation()
print(CompanyEvaluation().stockprices())


        
        
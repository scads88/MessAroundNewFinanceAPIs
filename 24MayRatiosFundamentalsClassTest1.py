
import os #be care with this will return true for directories and files
import pandas as pd
import requests
import bs4 as bs
import pickle
import collections
import datetime
import alpha_vantage
import numpy as np


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
        

    def stockprices(self):
        #relates to what the actual prices are doing relative to self and others
        pass
    
    def fundamentalratios(self):
        totaltickers=["OPK", "MYGN", "DGX", "NVTA"]
        goodbaddiclist=[{"Cash Ratio": "High is Good"}, {"Current Ratio":"High is Good"}]
        df2=pd.DataFrame.from_dict(goodbaddiclist, orient="columns")
        print(df2)
        check=goodbaddiclist
        print(check)
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
        #numberasindexdict={}
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
            
            #print(df[:2])
            #df["Potential OPOE Treatment"]=df[0:]
            #del df["index"]
            #del df[0]
            df.index = np.arange(1, len(df) + 1)
            #print(fundamentalratiolabels)
            #with open(filename+".pickle", "wb") as f:
                #pickle.dump(df, f)
                #f.close()
        #df.to_csv("24MayTest5"+".csv")
        #print(tickerlabelratiodict)
        #return df.head()
        goodbadlist=[]
        for item in df["Company Ratios"]:
            if item in totallist:
                goodbadlist.append("High ~ Better")
            else:
                goodbadlist.append("Low ~ Better")
        print (goodbadlist)
        df["Opinions"]=goodbadlist







                #df.loc[:,"Opinion"]=goodbaddiclist
            #else:
                #df.loc[:,"Opinion"]
        df.to_csv("25MayTest.csv")
        return df
#pasta=CompanyEvaluation()
print(CompanyEvaluation().fundamentalratios())


        
        
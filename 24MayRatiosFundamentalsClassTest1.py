
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



#might wanna generate all of these for one instance and leave the looping for later?


###Company Evaluation Class
class CompanyEvaluation:
    pass
    #can use class variables instead of hardcoding into methods

    def __init__(self):
        pass
    
    
    def infotrigger1(self):
        pass
    
    def rawfundamentals(self):
        gonogo="pass"
        AVkey="E82V6HPLXDMUN5TM"
        tickerbox=["OPK", "DGX", "NVTA", "LH"]

        for tickername in tickerbox:
            resp=requests.get("https://www.marketwatch.com/investing/stock/"+tickername+"/financials")
            soup=bs.BeautifulSoup(resp.text, "lxml")
            table = soup.find_all("td", class_="rowTitle")
            rows=list()
            for row in table:
                labels=[e.get_text().strip() for e in soup.select(".rowTitle")]
                values=[e.get_text().strip() for e in soup.select(".valueCell")]
####these are sensitive be care if fuck with them####
            labels.pop(0)
            labels.pop(11)
#######################################################
            fucktable=list(sorted(set([e.get_text().strip() for e in soup.select("th")]))) #generates list with years, etc, redundancy; kills redundant; organizes; turns into list; forces to vbl, gets rid blank
            fucktable.pop(0)
            theyears=fucktable[:5]

            values2013=values[::5]
            values2014=values[1::5]
            values2015=values[2::5]
            values2016=values[3::5]
            values2017=values[4::5]

            labelsvalueslast5years=[]

            print(values2016)
            labelsvalues2013dict={}
            for label, value in zip(labels, values2013):
                labelsvalues2013dict[label]=value
                labelsvalueslast5years.append(labelsvalues2013dict)
            labelsvalues2014dict={}
            for label, value in zip(labels, values2014):
                labelsvalues2014dict[label]=value
                labelsvalueslast5years.append(labelsvalues2014dict)
            labelsvalues2015dict={}
            for label, value in zip(labels, values2015):
                labelsvalues2015dict[label]=value
                labelsvalueslast5years.append(labelsvalues2015dict)
            labelsvalues2016dict={}
            for label, value in zip(labels, values2016):
                labelsvalues2016dict[label]=value
                labelsvalueslast5years.append(labelsvalues2016dict)
            labelsvalues2017dict={}
            for label, value in zip(labels, values2017):
                labelsvalues2017dict[label]=value
                labelsvalueslast5years.append(labelsvalues2017dict)

            years2labelsvaluesdict={}

            years2labelsvaluesdict[theyears[0]]=labelsvalues2013dict
            years2labelsvaluesdict[theyears[1]]=labelsvalues2014dict
            years2labelsvaluesdict[theyears[2]]=labelsvalues2015dict
            years2labelsvaluesdict[theyears[3]]=labelsvalues2016dict
            years2labelsvaluesdict[theyears[4]]=labelsvalues2017dict

#######################################
            ticker2years2labelsvaluesdict={}
            ticker2years2labelsvaluesdict[tickername]=years2labelsvaluesdict
            years2labelsvaluesdict2=years2labelsvaluesdict.values()
            dfx=pd.DataFrame.from_dict(years2labelsvaluesdict)# dictionary turned into a pandas dataframe
        #could be a good place to start replacement loop
            print (dfx["2013"].head())
        #break
            dfx.to_csv("smoke"+tickername+".csv")
        

    def roundTime(dt=None, roundTo=60): #From Thierry Husson 2012
       if dt == None : dt = datetime.datetime.now()
       seconds = (dt.replace(tzinfo=None) - dt.min).seconds
       rounding = (seconds+roundTo/2) // roundTo * roundTo
       return dt + datetime.timedelta(0,rounding-seconds,-dt.microsecond)
       #print (roundTime(datetime.datetime(2012,12,31,23,44,59,1234),roundTo=15*60))


    def stockchart(self):
        #relates to what the actual prices are doing relative to self and others
        AVkey="E82V6HPLXDMUN5TM"
        totaltickers=["OPK", "DGX", "NVTA", "LH"]
        ts=TimeSeries(key=AVkey, output_format='pandas')
        start=dt.datetime.today()-dt.timedelta(days=100)
        #print(roundTime(start))
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
            #plt.legend(meta_data["2. Symbol"])
            tickerdic[ticker]["5. adjusted close"].plot(label=ticker)
            plt.xlabel("100 Day Moving Average")
            plt.ylabel("Stock Price ($)")
            #plt.axis([start, end, 0, 200])
            #print(meta_data["2. Symbol"])
            plt.legend(loc="upper right")
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
        df.to_csv("28MayTest.csv")
        return df
    
    def SentimentAnalysis(self):
        pass

    
    
    def PredictiveAnalytics(self):
        pass
        
#pasta=CompanyEvaluation()
print(CompanyEvaluation().fundamentalratios())
print(CompanyEvaluation().stockchart())
print(CompanyEvaluation().rawfundamentals())


        
        
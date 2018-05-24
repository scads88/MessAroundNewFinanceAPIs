# -*- coding: utf-8 -*-
"""
Created on Thu May 24 21:14:12 2018

@author: john3
"""

class CompanyEvaluation:
    pass
    #can use class variables instead of hardcoding into methods

    def __init__(self):
        pass
    
    def rawfundamentals(self, ticker):
        self.ticker=ticker
        return ticker
        

    def stockprices(self):
        pass
    
    def fundamentalratios(self):
        totaltickers=["OPK", "MYGN", "MSFT", "DGX", "NVTA"]
        
        filename="24MayTest"
        picklefilename=filename+".pickle"
        totaltickers=[ticker.replace(ticker, ticker.lower()) for ticker in totaltickers]
        #dowehaveapickle=os.path.isfile(picklefilename)
        #print(os.path.abspath(picklefilename))
        tickerlabelratiodict={}
        for ticker in totaltickers:
            americaurl="https://www.marketwatch.com/investing/stock/" + ticker + "/profile" #creates the url template for usa stock ticker designation
            resp=requests.get(americaurl) # requests the info on americaurl and sends it to response variable
            soup3=bs.BeautifulSoup(resp.text, "lxml")# turns the resp variable into a soup
            fundamentalratiolabels=[e.get_text() for e in soup3.select(".sixwide .column")] #soup perused and labels and ratios extracted and fed into vbls based upon html characteristics
            fundamentalratios=[e.get_text() for e in soup3.select(".sixwide .data")]
            new_dict=OrderedDict({k:v for k, v in zip(fundamentalratiolabels, fundamentalratios)}) #the selected labels and selected ratios combined togteher into dictionary
            tickerlabelratiodict[ticker.upper()]=OrderedDict(new_dict) #label:ratio dictionary as values into another dictionary where stock ticker for each group is the key
            df=pd.DataFrame.from_dict(tickerlabelratiodict, orient="columns")# dictionary turned into a pandas dataframe
        #df.to_csv(filename+".csv")
        return df  
#pasta=CompanyEvaluation()
print(CompanyEvaluation().fundamentalratios())
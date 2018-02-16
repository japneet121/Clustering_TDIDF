import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def scrapData():
    data={
        "EntrezSystem2.PEntrez.PubMed.Pubmed_PageController.PreviousPageName":"results"
        ,"term":"neurodegenerative diseases"
        ,"EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.sPageSize":100
        ,"EntrezSystem2.PEntrez.PubMed.Pubmed_ResultsPanel.Pubmed_DisplayBar.PageSize":100
    }
    req_search=requests.post("https://www.ncbi.nlm.nih.gov/pubmed/?term=neurodegenerative+diseases",data=data)
    abstracts=[]
    counter=0
    soup_search=BeautifulSoup(req_search.text)
    res_search=soup_search.find_all("div",attrs={'class':'rslt'})
    for res in res_search:
        try:
            req_abs=requests.get("https://www.ncbi.nlm.nih.gov/"+res.find("a").get("href"))
            soup_abs=BeautifulSoup(req_abs.text)
            abstract=soup_abs.find("div",attrs={"class":'abstr'})
            if abstract !=None:
                abstracts.append(abstract.p.text)
            counter+=1
            print counter
        except:
            print"error occured ",sys.exc_info()
            print counter
            counter+=1
    return abstracts        

import requests
from bs4 import BeautifulSoup


def get_para(site:str, idx:int=0):

    print(site)
    r = requests.get(site)
    #print(r.text)

    soup = BeautifulSoup(r.content, "html.parser")
    paras = soup.find_all("p")

    first_para = paras[idx]
    #if len(first_para.text) > 400:
        #print(f"it seems {site} may be formatted weirdly")
        #print("please manually insert paragraph in the HTML")
        #return (site,first_para.text)
        #return (site, "ERROR")
    return (site,first_para.text)
import requests
from bs4 import BeautifulSoup


def get_para(site:str, idx:int=0):

    r = requests.get(site)

    soup = BeautifulSoup(r.content, "html.parser")
    paras = soup.find_all("p")

    first_para = paras[idx]
    return (site,first_para.text)
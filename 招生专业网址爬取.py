# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:54:21 2020

@author: 30509
"""
import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import re
import json

with open ("华东师范大学2020年硕士研究生招生专业目录.json","r") as f:
    L=[]
    t1=json.load(f)
    L1=list(t1.values())
    for l in L1:
        L+=l
    
def getHTMLText(url):
    try:
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        h=requests.get(url,headers=headers,verify=False)
        h.raise_for_status()
        h.encoding="gbk"
        return h.text
    except:
        return ""

def getSite(soup):
    Site=[]
    nameTags = soup.findAll('a',{"href":True})
    for n in nameTags:
        p="sszyml"
        s=n['href']
        result=re.match(p,s)
        if result:
            Site.append(n['href'])
    return Site

def matchSite(L,Site):
    Match=dict(zip(L,Site))
    return Match

def main():
    url="https://yjszs.ecnu.edu.cn/system/sszszyml_list.asp"
    r=getHTMLText(url)
    soup=BeautifulSoup(r,"lxml")
    Site=getSite(soup)
    Match=matchSite(L,Site)
    json1=json.dumps(Match,ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
    with open("招生专业网址.json","w") as f:
        f.write(json1)

main()        
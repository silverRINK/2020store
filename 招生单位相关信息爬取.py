# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 17:21:01 2020

@author: 30509
"""

import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import re
import json

def getHTMLText(url):
    try:
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        h=requests.get(url,headers=headers,verify=False)
        h.raise_for_status()
        h.encoding="gbk"
        return h.text
    except:
        return ""
    
def getWebsite(Department):
    U=[]
    for i in Department:
        p='\d+'
        a=re.search(p,i)
        b=a.group()
        url1="https://yjszs.ecnu.edu.cn/system/yxjj_detail.asp?yxdm="+b+"&zsnd=2020"
        U.append(url1)
    return U

def getIntro(soup):
    Intro=[]
    data1=soup.find_all("p")
    for intro in data1:
        Intro.append(intro.string)
    return Intro

def main():
    with open("华东师范大学2020年硕士研究生招生专业目录.json","r") as m:
        t=json.load(m)
        Department=list(t.keys())
    U=getWebsite(Department)
    Brief=[]
    Feature=[]
    Team=[]
    I=[]
    for url1 in U:
        r1=getHTMLText(url1)
        soup1=BeautifulSoup(r1,"lxml")
        Intro=getIntro(soup1)
        if Intro != []:
            Intro.remove('本站内容未经书面许可,禁止一切形式的转载')
            Brief.append(Intro[1])
            Feature.append(Intro[2])
            Team.append(Intro[3])
        else:
            i=U.index(url1)
            I.append(Department[i])
    for j in I:
        if j in Department:
            Department.remove(j)
    table1=dict(zip(Department,Brief))
    table2=dict(zip(Department,Feature))
    table3=dict(zip(Department,Team))
    json1=json.dumps(table1,ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
    json2=json.dumps(table2,ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
    json3=json.dumps(table3,ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
    with open("简介.json","w") as f:
        f.write(json1)
    with open("特色.json","w") as g:
        g.write(json2)
    with open("团队.json","w") as h:
        h.write(json3)    

main()
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

def getMajor(soup):
    Major=[]
    data=soup.find_all("td")
    for u in data:
        lis=u.find_all("a")
        for major in lis:
            Major.append(major.string)
        #print(lis)
    return Major
            
def classMajor(Major):
    L1=[]
    Department=[]
    m1=""
    Subject=[]
    for m in Major:
        p="\d"
        l=re.findall(p, m)
        if len(l)==3:
            Department.append(m)
            Major=[" " if i == m else i for i in Major]
    for m in Major:
        m1+=m
    L=m1.split()
    for i in L:
        p1="(.\d{4}.{3}\w+)"
        l1=re.findall(p1, i)
        L1.append(l1)
    table=dict(zip(Department,L1))
    return table

def main():
    url="https://yjszs.ecnu.edu.cn/system/sszszyml_list.asp"
    r=getHTMLText(url)
    soup=BeautifulSoup(r,"lxml")
    dic=getMajor(soup)
    table=classMajor(dic)
    json1=json.dumps(table,ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
    with open("华东师范大学2020年硕士研究生招生专业目录.json","w") as f:
        f.write(json1)

main()
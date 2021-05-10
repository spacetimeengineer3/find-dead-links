#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

url = requests.get('http://10.92.21.107:8080/')

soup = BeautifulSoup(url.text, features='html.parser')


tags = soup.find_all('a')
#print(tags)
links = []
goodlinks = []
for tag in tags:
    links.append(tag.get('href'))

#for link in links:
    #print(link)

def testlinks():
    for link in links:
        #print(links)
        try:
            if "http" not in link:
                #print("NO HTTP")
                if link[0] == "/":
                    r = requests.get('http://10.92.21.107:8080' + link)
                if link[0] != "/":
                    r = requests.get('http://10.92.21.107:8080/' + link)
            else:
                r = requests.get(link)


            if r.status_code not in [200, 302]:
                #print("%s is a bad Link" %link)
                #links.pop(link)
                #print(r.status_code)
                continue
        except:
            #print("%s is a bad Link" %link)
            #links.remove(link)
            continue
        else:
            goodlinks.append(link)

testlinks()

for goodlink in goodlinks:
    if "http" not in goodlink:
        #print("NO HTTP")
        if goodlink[0] == "/":
            r = requests.get('http://10.92.21.107:8080' + goodlink)
        if goodlink[0] != "/":
            r = requests.get('http://10.92.21.107:8080/' + goodlink)
    else:
        r = requests.get(goodlink)
    soup = BeautifulSoup(r.text, features='html.parser')
    tags = soup.find_all('a')
    print(tags)
    #for link in links:
    #print(link)
#for child in soup.descendants:
    #print(child)

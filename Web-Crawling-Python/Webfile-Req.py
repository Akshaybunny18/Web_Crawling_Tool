import os
import requests
from bs4 import BeautifulSoup

def sif(x,url,visited,data,deep=0,maxdeep=8) :
    if deep > maxdeep:  # limit recursion depth to prevent stack overflow and to avoid infinite recursion
        return
    x=x.lower()
    if url in visited :
        return
    visited.add(url)

    try:
        print(f"(Bunny) Fetching SUB(URLS): {url}")
        # these are the urls not required to save in txt or to enter into sub_url_webpage
        code=requests.get(url,timeout=10).text  # setting timeout exception to avoid hang ; it executes if page dont responds in given time
    except requests.RequestException:
        return
    soup=BeautifulSoup(code,'lxml')
    hi=soup.find_all('a')

    for url in hi :
        link=url.get('href')
        # if required also can add oldintranet links/files which are in current intranet web page
        # http://oldintranet.iiit.ac.in adding this as a (or)condition as given below
        if link :  # if link is not null 
            if link.endswith(f'.{x}') :
                if link.startswith('https://intranet.iiit.ac.in') or link.startswith('http://intranet.iiit.ac.in') :  # Fixed logical error
                    data.add(link) 
                else :
                    data.add('https://intranet.iiit.ac.in' + link)
            elif link.startswith('/offices') :
                full_url='https://intranet.iiit.ac.in' + link
                sif(x,full_url,visited,data,deep+1,maxdeep)  # Increment depth
            elif link.startswith('https://intranet.iiit.ac.in') or link.startswith('http://intranet.iiit.ac.in') :
                sif(x,link,visited,data,deep+1,maxdeep)  # Increment depth

x=input("Enter any file extension :) ")
data=set()
visited=set()
sif(x,'https://intranet.iiit.ac.in/offices',visited,data)

file=open("urls.txt","w") # write indicates in overwriting the file i.e, new file
for link in data:
    file.write(link + '\n')


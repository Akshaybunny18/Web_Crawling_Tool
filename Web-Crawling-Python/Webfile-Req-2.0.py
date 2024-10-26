import os
import requests
from bs4 import BeautifulSoup

def sif(x,url,visited,data,deep=0,maxdeep=8) :
    if deep > maxdeep:  # limit recursion depth to prevent stack overflow and to avoid infinite recursion
        return
    x=x.lower()
    if url in visited :  # can also be placed for below to reduce time and recursions
        return
    visited.add(url)

    try:
        print(f"(Bunny) Fetching SUB(URLS): {url}")
        # these are the urls not required to save in txt or to enter into sub_url_webpage   
        code=requests.get(url,timeout=10,verify=False).text  # setting timeout exception to avoid hang ; it executes if page dont responds in given time
    except requests.RequestException: # secure sockets layer & transport layer secu  # up line .text can be used only while print also when direct print
        return
    soup=BeautifulSoup(code,'lxml') # 'html.parser' or 'html5lib' # x = soup.prettify()   & . functions used   # # can try except 
    hi=soup.find_all(['link','a','base','img','area','iframe','frame','audio','video','script']) #object-data # soup = formatted html code   
    for url in hi :
        link=url.get('href') #akshay # link = url['href']
        if link is None : 
            link=''
            link=url.get('src')
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
print(f"Surfing complete. Found {len(data)} files.")

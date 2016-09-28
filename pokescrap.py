#!usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as BS
import webbrowser #to open the image in safari


arr=[]
url = "http://imgur.com/gallery/ksnRO"
r=requests.get(url)
soup = BS(r.text,"html.parser")
for node in soup.find_all('div',{'class':'post-image'}):#we could have used this    soup.find_all('div',{'class':'post-image'})[3:]   to start from third
    image_url= node.img.get('src')
    arr.append(image_url)
    #webbrowser.open('http:'+image_url)  #this will open image source in default web browser i.e. in safari
#print arr





#to save the list of urls in a file that would be created 
file=open('urllist','w')
file.write(str(arr))

#!usr/bin/env pyhton
# -*- coding: UTF-8 -*-
# Author:Yin
import requests
from urllib.request import urlretrieve

import urllib.request
from bs4 import BeautifulSoup


x=0

def  getGrilsImg(page=1):

    response = requests.get('https://www.dbmeinv.com/index.htm?cid=7&pager_offset={}'.format(page))
    html = response.text


    soup = BeautifulSoup(html,"html.parser")

    gril = soup.find_all('img')
    # x = 0
    for i in gril:
        global x
        imgsrc =i.get('src')
        print( imgsrc)
        urllib.request.urlretrieve(imgsrc, 'C:/Users/90595/OneDrive/桌面/images/cluster-2/%s.jpg'%x)

        x +=1
        print('正在下载%s张'%x)
for i in range(1,50):
    getGrilsImg(i)
getGrilsImg()

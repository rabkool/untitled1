#!usr/bin/env pyhton
# -*- coding: UTF-8 -*-
# Author:Yin
import requests
from bs4 import BeautifulSoup

i = 0
# url = "https://movie.douban.com/top250"


urls = ['https://movie.douban.com/top250?start='+str(n) + '&filter=' for n in range(0, 250, 25)]
for url in urls:
    # 放入网址
    wb_data = requests.get(url)
    # 读取html
    soup = BeautifulSoup(wb_data.text, 'html')

    # 对div.hd>a读取
    title = soup.select('div.hd>a')
    # 对img读取
    imgs = soup.select('img[src]')

    for title, img in zip(title, imgs):
        # 放入字典
        data = {
            'title': list(title.stripped_strings),
            'img': img.get('src')
        }

        print(data)
        # 名称按顺序加1
        i += 1
        # 顺序 、名字 加文件格式
        fileName = str(i) + '、' + data['title'][0]+'.jpg'

        # 请求图片的地址
        pic = requests.get(data['img'])
        # 写入 路径 命名 wb二进制写入
        with open('C:/Users/90595/OneDrive/桌面/images/cluster-1/'+fileName, 'wb') as photo:
            # 写出
            photo.write(pic.content)
        print(str(i) + data['title'][0])




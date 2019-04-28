#!usr/bin/env pyhton
# -*- coding: UTF-8 -*-
# Author:Yin
import requests
import bs4

def open_url(url):
    headers ={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Mobile Safari/537.36"}
    res = requests.get(url, headers=headers)

    return res

def main():
    res = requests.get("https://press.vin/actress")
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # 名字
    name = []
    # targets = soup.find_all("div", class_="hd")
    targets = soup.find_all("li", class_="tags__list__item is-actress")
    for each in targets:
        # print(each.a.span.text)
        # 点a标签里面的文字
        name.append(each.a.text)

        print(name)

main()
# res = requests.get("https://press.vin/actress")
# soup = bs4.BeautifulSoup(res.text, "html.parser")
#
# # 名字
# name = []
# # targets = soup.find_all("div", class_="hd")
# targets = soup.find_all("li", class_="tags__list__item is-actress")
# for each in targets:
#     # print(each.a.span.text)
#     # 点a标签里面的文字
#     name.append(each.a.text)
#     print(name)

# def main():
#     res = requests.get("https://press.vin/actress")
#     # res = open_url(host)
#     result = []
#     with open("123.txt", "w", encoding="utf-8") as f:
#         for i in  range():
#             url =host
#             res = open_url(url)
#             result.extend(find_movies(res))
#
#
#         for each in result:
#             f.write(each)
#
# if __name__ == "__main__":
#     main()
#
#
#














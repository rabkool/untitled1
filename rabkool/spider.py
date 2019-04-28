from hashlib import md5

import requests
import re
import json
from requests.exceptions import RequestException

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
}

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile('<li class="tags__list__item is-actress">.*?href="(.*?)".*?src="(.*?)"(.*?)', re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items:
        yield {
            'name': item[0].strip()[8:],
            'image': 'https://'+item[1].strip()[2:]
        }

# 文件写出
def write_to_file(content):
        # 打开
    with open('学习资料demo.txt', 'a', encoding='utf-8') as f:
        # 写入
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        # 关闭
        f.close()



def main(offset):
    url = 'https://press.vin/actress/'+ str(offset)
    html = get_one_page(url)
    # parse_one_page(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':

    # sites = ["あ", "か", "さ", "た", "な", "は", "ま", "や", "ら", "わ"]
    sites = ["わ"]
    for site in sites:
        main(site)


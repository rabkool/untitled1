# -*- coding: utf-8 -*-
import scrapy
from  scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList
from YinDemo.items import demoItem

class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['press.vin/']

    start_urls = ['https://press.vin/actress']
    # start_urls = ['https: // www.qiushibaike.com / text / page / 1 /']

    def parse(self, response):
        duanzidivs = response.xpath("//li[@class='tags__list__item is-actress']")
        for duanzidiv in duanzidivs:
            name = duanzidiv.xpath(".//a/text()").get().strip()
            image = duanzidiv.xpath(".//img/@src").get().strip()
            # author = duanzidiv.xpath(".//a/text()").get().strip()
            # content = duanzidiv.xpath(".//div[@class='content']//text()").getall()

            print(name+image)

            item = demoItem(name=name, image=image)
            yield item

            # duanzidivs = response.xpath("//section[@class='tags']")
            # for duanzidiv in duanzidivs:
            #     name = duanzidiv.xpath(".//li[@class='tags__list__item is-actress']//a/text()").getall()
            #     image = duanzidiv.xpath(".//li[@class='tags__list__item is-actress']//img/@src").getall()
            # next_url = response.xpath("")
            # if not next_url:
            #     return
            # else:
            #     yield scrapy.Request(next_url,callback=self.parse())

            # duanzi= {
            #     "name": name,
            #     "image": "https:"+image
            # }
            # yield duanzi




# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from lxml import etree
import time


class sslSpider:

    def __init__(self):
        self.headers = {"User-Agent": "Mozilla5.0/"}
        self.pageurl = "http://www.18183.com/yys/shishen/"

    def getUrl(self):
        res = requests.get(self.pageurl, headers=self.headers)
        res.encoding = "utf-8"
        html = res.text

        parseHtml = etree.HTML(html)
        for i in range(1, 120):
            i = str(i)
            geturl = "/html/body/div[@class='maxWrap']/div[@class='wrap-index']/div[@class='wrap fwr wrap-bg']/div[@class='l-mod6 clear modBg mt15 m-pet']/div[@class='w-pet-wrap clear']/ul[@id='j-hero-list']/li[@class='item'][" + i + "]/a/div[@class='pic']/img/@src"
            getname = "/html/body/div[@class='maxWrap']/div[@class='wrap-index']/div[@class='wrap fwr wrap-bg']/div[@class='l-mod6 clear modBg mt15 m-pet']/div[@class='w-pet-wrap clear']/ul[@id='j-hero-list']/li[@class='item'][" + i + "]/a/h4"
            url = parseHtml.xpath(geturl)[0]
            name = parseHtml.xpath(getname)[0].text
            print(url)
            print(name)
            name = "./式神录/" + name + ".jpg"
            self.writeimg(url, name)
            time.sleep(2)

    def writeimg(self, url, filename):
        res = requests.get(url, headers=self.headers)
        res.encoding = "utf-8"
        img = res.content
        with open(filename, 'ab') as f:
            print("%s正在下载" % filename)
            f.write(img)
            print("%s下载成功" % filename)
if __name__ == "__main__":
    spider = sslSpider()
    spider.getUrl()

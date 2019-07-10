# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from lxml import etree
import time
import os


class sslSpider:

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        self.pageurl = "https://yys.cbg.163.com/cgi/mweb/equip/10/201811062101616-10-3BCYCTTI5RDCJ"

    def file_name(self, file_dir):
        fname_list = []
        for root, dirs, fname in os.walk(file_dir):
            for i in fname:
                k = i.replace('.png', '')
                fname_list.append(k)
            self.getUrl(fname_list)

    def getUrl(self):
        sulr = 'https://cbg-yys.res.netease.com/game_res/headskin/2'
        i = 3

        while i < 15:
            if i > 10:
                url = sulr + str(i) + '.png'
            else:
                url = sulr + '0' + str(i) + '.png'
            name = "./头像框/" + '901' + str(i) + '.png'
            self.writeimg(url, name)
            time.sleep(1)
            i += 1

    def writeimg(self, url, filename):
        res = requests.get(url, headers=self.headers)
        res.encoding = "utf-8"
        img = res.content
        if img:
            with open(filename, 'ab') as f:
                print("%s正在下载" % filename)
                f.write(img)
                print("%s下载成功" % filename)
        else:
            print('%s不存在' % filename)
if __name__ == "__main__":
    spider = sslSpider()
    # spider.file_name("./式神")
    spider.getUrl()

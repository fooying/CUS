#!/usr/bin/env python
#encoding=utf-8
#by Fooying 2013-12-17 01:56:04

'''
正则工具模块
'''
import re

class WWW():
    def __init__(self):
        pass

    def get_domain(self, site):
        if site.startswith('https://'):
            site = site[8:-1]
        elif site.startswith('http://'):
            site = site[7:-1]
        return site.split('/')[0]

    def is_url_format(self, url):
        regex = """
               ^ #必须是串开始
               (?:http(?:s)?://)? #protocol
               (?:[\w]+(?::[\w]+)?@)? #user@password
               ([-\w]+\.)+[\w-]+(?:.)? #domain
               (?::\d{2,5})? #port
               (/?[-:\w;\./?%&=#]*)? #params
               $
               """
        result = re.search(regex, url, re.X|re.I)
        if result:
            return True
        else:
            return False

www = WWW()
if __name__ == '__main__':
    print www.get_domain('http://www.mongodb.org/dr/fastdl.mongodb.org/linux/mongodb-linux-x86_64-2.4.8.tgz/download')
    print www.is_url_format('http://www.mongodb.org/dr/fastdl.mongodb.org/linux/mongodb-linux-x86_64-2.4.8.tgz/download')

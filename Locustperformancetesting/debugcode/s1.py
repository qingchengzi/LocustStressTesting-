#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2021/3/9 14:35'

import requests




from lxml import etree
import random

url = "https://docs.locust.io/en/latest/"

response = requests.get(url).text

tree = etree.HTML(response)
# print(tree)

to_urls = tree.xpath('//*[@id="getting-started"]/div/ul/li/a/@href')
random_url = random.choice(to_urls)
# print(random_url)
response_2 = requests.get(url,params=random_url).text

tree_2 = etree.HTML(response_2)
to_urls2 = tree_2.xpath("/html/body/div[1]/nav/div/div[2]/ul/li/a/@href")
to_urls2.append("#")
print(to_urls2)
if "#" in to_urls2:
    print(True)
else:
    print("没有啊")
random_url2 = random.choice(to_urls2)
print(random_url2)
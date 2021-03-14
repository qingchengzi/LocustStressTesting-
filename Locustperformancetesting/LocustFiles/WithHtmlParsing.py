#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2021/3/9 17:14'

import random
import re

from lxml import etree

from locust import HttpUser
from locust import between
from locust import task

from common import config


class AwesomeUser(HttpUser):
    """
    locust和lxml配合使用，通过lxmp获取指定url页面中a标签中href属性的值，作为下一个请求的url进行压测
    """
    wait_time = between(5, 600)
    host = config.URL
    current_page = []

    def on_start(self):
        self.index_page()

    @task(10)
    def index_page(self):
        r = self.client.get("", name="index")
        tree = etree.HTML(r.content)
        self.toc_urls = tree.xpath('//*[@id="getting-started"]/div/ul/li/a/@href')

    @task(50)
    def load_page(self):
        url = random.choice(self.toc_urls)
        r = self.client.get(url, name="load_page")
        tree = etree.HTML(r.content)
        current_page = tree.xpath('/html/body/div[1]/nav/div/div[2]/ul/li/a/@href')
        if not current_page:
            pass
        else:
            for i in current_page:
                if re.findall(r".html", i):
                    self.current_page.append(i)
                else:
                    continue

    @task(30)
    def load_sub_page(self):
        if self.current_page:
            url = random.choice(self.current_page)
            self.client.get(url, name="load_sub_page")

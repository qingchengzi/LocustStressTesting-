#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2021/3/10 15:41'

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试地址
URL = "https://docs.locust.io/en/latest/",

# Locust文件目录
LOCUST_DIR = "{0}/{1}".format(BASE_DIR, "LocustFiles")

# 目录路径

DIRECTORY_PATH = {
    "log_path": os.path.join(BASE_DIR, "log"),
    "data_path": os.path.join(BASE_DIR, "database")
}

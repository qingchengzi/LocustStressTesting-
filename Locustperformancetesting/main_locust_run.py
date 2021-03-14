#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'tian'
__data__ = '2021/3/9 12:07'

import os
import re


from common import config


def get_locust_file():
    """
    获取locust文件
    :return:
    """
    locust_file = "{0}".format(config.LOCUST_DIR)
    li_dir = []
    for i in os.listdir(locust_file):
        if re.findall(r"__.*__", i):
            continue
        else:
            li_dir.append("{0}/{1}".format(locust_file, i))
    return li_dir


def run_locust(*args):
    locust_list = get_locust_file()
    if args[0] == "1":
        os.system("locust -f {0}".format(locust_list[0]))
    elif args[0] == "2":
        flage = True
        while flage:
            input_user_numbers = input("请输入并发:用户数(默认10)/每秒启动用户数(默认2）/运行时长(默认1分钟)【输入格式(25/2/100)】-->")
            if re.findall(r"\d*/\d*/\d*", input_user_numbers):
                li_number = input_user_numbers.split("/")
                print("locust -f {0} --headless -u {1} -r {2} -t {3}m ".format(locust_list[0],
                                                                               li_number[0],
                                                                               li_number[1],
                                                                               li_number[2]))
                os.system("locust -f {0} --headless -u {1} -r {2} -t {3}m".format(locust_list[0],
                                                                                  li_number[0],
                                                                                  li_number[1],
                                                                                  li_number[2]))
                flage = False
            elif not input_user_numbers:
                os.system("locust -f {0} --headless -u 10 -r 2 -t 1m".format(locust_list[0]))
                flage = False
            else:
                print("输入有错，请重新输入")

    elif args[0] == "3":
        flage = True
        while flage:
            input_user_numbers = input("请输入并发:用户数(默认10)/每秒启动用户数(默认2）/运行时长(默认1分钟,单位：分钟)【输入格式(25/2/100)】-->")
            if re.findall(r"\d*/\d*/\d*", input_user_numbers):
                li_number = input_user_numbers.split("/")
                os.system("locust -f {0} --csv=example --headless -u {1} -r {2} -t {3}m ".format(
                    locust_list[0],
                    li_number[0],
                    li_number[1],
                    li_number[2]))
                flage = False
            elif not input_user_numbers:
                os.system(
                    "locust -f {0} --csv=example --headless -u 10 -r 10 -t 1m".format(locust_list[0],))
                flage = False
            else:
                print("输入有错去重新输入")


if __name__ == '__main__':
    print("""
        *****************请选择运行方式****************************
        1、图像界面运行
        2、没有Web UI下运行
        3、没有Web UI下运行，生成Excel类型测试报告
    """)
    ipt = input("请输入选择序号：").strip()
    run_locust(ipt)

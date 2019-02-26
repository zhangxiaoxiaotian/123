#coding=utf-8
# *******************************************************************
#     Filename @  111.py
#       Author @  XiaoTian
#  Create date @  2019/2/19 15:37
#        Email @  1075767641@qq.com
# ********************************************************************
import os
dir_report = os.path.split(os.path.realpath(__file__))[0]
report_dir = os.path.join(dir_report,"test.html")
case_dir = os.path.join(dir_report,"testcases")
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("www.baidu.com")

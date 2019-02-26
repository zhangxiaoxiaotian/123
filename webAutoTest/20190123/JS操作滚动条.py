#coding=utf-8
# *******************************************************************
#     Filename @  JS操作滚动条.py
#       Author @  XiaoTian
#  Create date @  2019/1/23 18:12
#        Email @  1075767641@qq.com
# ********************************************************************
from  selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# 打开浏览器
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# js语句执行window.scrollTo
# driver.execute_script("arguments[0].scrollTo")
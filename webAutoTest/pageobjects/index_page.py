#coding=utf-8
# *******************************************************************
#     Filename @  index_page.py
#       Author @  XiaoTian
#  Create date @  2019/2/15 17:00
#        Email @  1075767641@qq.com
# ********************************************************************
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import random
from elements import index_elements

class index_page:
    def __init__(self,driver):
        self.driver = driver
    def get_isExist(self):
        try:
            WebDriverWait(self.driver,15).until(expected_conditions.visibility_of_element_located(index_elements.quit_button))
            return True
        except:
            return False
    def get_bid(self):
        #获取标
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(index_elements.bid))
        # 点击抢投标
        self.driver.find_element(*index_elements.bid).click()


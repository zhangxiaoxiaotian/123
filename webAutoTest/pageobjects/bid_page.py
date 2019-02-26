#coding=utf-8
# *******************************************************************
#     Filename @  bidpage.py
#       Author @  XiaoTian
#  Create date @  2019/2/19 18:15
#        Email @  1075767641@qq.com
# ********************************************************************
from elements import bid_elements
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
class BidPage:
    def __init__(self,driver):
        self.driver = driver
    def get_user_leftmoney(self):
        pass
    # 投资输入操作
    def invest(self,Investment_amount):
        WebDriverWait(self.driver,20).until(expected_conditions.visibility_of_element_located(bid_elements.Investment_amount_frame))
        self.driver.find_element(*bid_elements.Investment_amount_frame).send_keys(Investment_amount)
    #点击投资按钮
    def click_invest(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(bid_elements.Investment_button))
        self.driver.find_element(*bid_elements.Investment_button).click()

    # 投资成功提示
    def invest_suc_tip(self):

        try:
            WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(bid_elements.Investment_success_tip))
            return True
        except:
            return False
    # 投资成功弹出框
    def click_success(self):
        WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(bid_elements.View_and_activate_button))
        self.driver.find_element(*bid_elements.View_and_activate_button).click
    # 获取按钮提示
    def button_tip(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(bid_elements.Investment_button))
        return self.driver.find_element(*bid_elements.Investment_button).text
#     获取页面中心提示
    def middle_page_tip(self):
        WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(bid_elements.page_center_tip))
        return self.driver.find_element(*bid_elements.page_center_tip).text


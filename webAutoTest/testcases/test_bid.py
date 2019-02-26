#coding=utf-8
# *******************************************************************
#     Filename @  test_bid.py
#       Author @  XiaoTian
#  Create date @  2019/2/20 10:08
#        Email @  1075767641@qq.com
# ********************************************************************
import unittest
from selenium import webdriver
from datas import common_data
from pageobjects.login_page import Login
from pageobjects.index_page import index_page
from pageobjects.bid_page import BidPage
from datas import bid_datas
import time
class testBid(unittest.TestCase):
    def setUp(self):
        #获取网页
        self.driver = webdriver.Chrome()
        self.driver.get(common_data.url)
        self.driver.maximize_window()
        Login(self.driver).login(common_data.user,common_data.password)
        index_page(self.driver).get_bid()
    def tearDown(self):
        # 退出网页
        self.driver.quit()
    def test_2_bid_success(self):
        bp = BidPage(self.driver)
        bp.invest(bid_datas.investment_amount)
        bp.click_invest()
        self.assertTrue(BidPage(self.driver).invest_suc_tip())
    def test_0_amount_no10(self):
        bp = BidPage(self.driver)
        bp.invest(bid_datas.decimal_investment_no10_amount["amount"])
        time.sleep(2)
        self.assertEqual(bid_datas.decimal_investment_no10_amount["check"],BidPage(self.driver).button_tip())
    def test_1_amount_no100(self):
        bp = BidPage(self.driver)
        bp.invest(bid_datas.decimal_investment_no100_amount["amount"])
        time.sleep(2)
        bp.click_invest()
        self.assertEqual(bid_datas.decimal_investment_no100_amount["check"],BidPage(self.driver).middle_page_tip())




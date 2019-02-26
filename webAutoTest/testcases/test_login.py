#coding=utf-8
# *******************************************************************
#     Filename @  test_login.py
#       Author @  XiaoTian
#  Create date @  2019/2/15 17:01
#        Email @  1075767641@qq.com
# ********************************************************************
import unittest
from selenium import webdriver
from pageobjects.login_page import Login
from pageobjects.index_page import index_page
from ddt import ddt,data
from datas import common_data as cd
from datas import login_datas as ld
def test_11():
    pass
@ddt
class Testlogin(unittest.TestCase):
    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("http://120.79.176.157:8012/Index/login.html")
    #     self.driver.maximize_window()
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(cd.url)
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    def test_2_login_success(self):
        Login(self.driver).login(ld.suc_data["user"],ld.suc_data["password"])

        self.assertTrue(index_page(self.driver).get_isExist())
    #
    # def test_login_nopassword(self):
    #     Login(self.driver).login("18684720553","")
    #
    #     self.assertEqual("请输入密码",Login(self.driver).get_error())
    # def test_login_nophonenum(self):
    #     Login(self.driver).login("","python")
    #
    #     self.assertEqual("请输入手机号",Login(self.driver).get_error())
    # def test_login_lessele(self):
    #     Login(self.driver).login("18684720","python")
    #     self.assertEqual("请输入正确的手机号",Login(self.driver).get_error())
    @data(*ld.fail_datas)
    def test_0_wrong(self,data):
        lp = Login(self.driver)
        lp.login(data["user"], data["password"])
        self.assertEqual(data["check"], lp.get_error())
        self.driver.refresh()
    @data(*ld.wrong_login)
    def test_1_err_Msg_cen(self,data):
        lp = Login(self.driver)
        lp.login(data["user"], data["password"])
        self.assertEqual(data["check"], lp.get_error_middle())
        self.driver.refresh()


    # def tearDown(self):
    #     self.driver.quit()
    #     self.driver.refresh()

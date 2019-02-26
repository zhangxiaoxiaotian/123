#coding=utf-8
# *******************************************************************
#     Filename @  login_page.py
#       Author @  XiaoTian
#  Create date @  2019/2/15 17:00
#        Email @  1075767641@qq.com
# ********************************************************************

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from elements import login_element as le
from basepage.common import Element_operation
class Login(Element_operation):
    # #用户名输入框
    # user_input = (By.XPATH,"//input[@name='phone']")
    # #密码输入框
    # password_input=(By.XPATH,"//input[@name='password']")
    # # 登录按钮
    # login_button= (By.XPATH,"//button")
    # # 输入区域错误提示框
    # error_Msg_loginArea = (By.XPATH,"//div[@class='form-error-info']")
    # # 页面中间错误提示框
    # error_Msg_pageCenter = (By.XPATH,"//div[@class='layui-layer-content']")
    # def __init__(self,driver):
    #     self.driver = driver

    def login(self,username,password):
        # self.wait_element("登录模块",le.user_input)
        self.input_text("登录模块",le.user_input,username)
        self.input_text("登录模块", le.password_input, password)
        self.click_element("登录模块",le.login_button)
        # WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(le.user_input))
        # self.driver.find_element(*le.user_input).send_keys(username)
        # self.driver.find_element(*le.password_input).send_keys(password)
        # self.driver.find_element(*le.login_button).click()
    def get_error(self):
        # WebDriverWait(self.driver,20).until(expected_conditions.visibility_of_element_located(le.error_Msg_loginArea))
        # return self.driver.find_element(*le.error_Msg_loginArea).text
        return self.get_element_text("登录模块",le.error_Msg_loginArea)
    def get_error_middle(self):
        # WebDriverWait(self.driver, 20).until(
        #     expected_conditions.visibility_of_element_located(le.error_Msg_pageCenter))
        # return self.driver.find_element(*le.error_Msg_pageCenter).text
        return self.get_element_text("登录模块",le.error_Msg_pageCenter)

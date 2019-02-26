#coding=utf-8
# *******************************************************************
#     Filename @  login_element.py
#       Author @  XiaoTian
#  Create date @  2019/2/18 18:32
#        Email @  1075767641@qq.com
# ********************************************************************
from selenium.webdriver.common.by import By
#用户名输入框
user_input = (By.XPATH,"//input[@name='phone']")
    #密码输入框
password_input=(By.XPATH,"//input[@name='password']")
    # 登录按钮
login_button= (By.XPATH,"//button")
    # 输入区域错误提示框
error_Msg_loginArea = (By.XPATH,"//div[@class='form-error-info']")
    # 页面中间错误提示框
error_Msg_pageCenter = (By.XPATH,"//div[@class='layui-layer-content']")
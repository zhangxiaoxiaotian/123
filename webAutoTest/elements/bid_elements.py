#coding=utf-8
# *******************************************************************
#     Filename @  bid_elements.py
#       Author @  XiaoTian
#  Create date @  2019/2/20 10:40
#        Email @  1075767641@qq.com
# ********************************************************************
from selenium.webdriver.common.by import By
#投资金额填写框
Investment_amount_frame = (By.XPATH,'//input[@class="form-control invest-unit-investinput"]')

# 投资按钮
Investment_button = (By.XPATH,'//button[@class="btn btn-special height_style"]')
# 投资成功提示
Investment_success_tip = (By.XPATH,"//div[text()='投标成功！']")
# 查看并激活按钮
View_and_activate_button=(By.XPATH,"//button[text()='查看并激活']")
# 页面中间提示
page_center_tip = (By.XPATH,'//div[@class="text-center"]')


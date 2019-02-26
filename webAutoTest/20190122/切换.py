#coding=utf-8
# *******************************************************************
#     Filename @  切换.py
#       Author @  XiaoTian
#  Create date @  2019/1/22 21:19
#        Email @  1075767641@qq.com
# ********************************************************************
# 1.窗口切换，多个窗口切换，获取句柄driver.window_handles有序的driver.switch_to.window()
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
# 打开浏览器
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("柠檬班")
driver.find_element_by_id("su").click()
# 获取当前句柄
wins_old = driver.window_handles
print(wins_old)
print(driver.title)
WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.XPATH,'//div[@tpl="tieba_general"]//a[text()="吧_百度贴吧"]')))
driver.find_element_by_xpath('//div[@tpl="tieba_general"]//a[text()="吧_百度贴吧"]').click()

#出现新的窗口
#等待窗口出现
WebDriverWait(driver,10).until(expected_conditions.new_window_is_opened(wins_old))

#切换窗口
wins = driver.window_handles
print(wins)
print(driver.title)
driver.switch_to.window(wins[-1])

# 点击页面
WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.ID,"tab_picture")))
driver.find_element_by_id("tab_picture").click()

# 2.alert弹框切换
ale = WebDriverWait(driver,10).until(expected_conditions.alert_is_present())
# driver.switch_to.alert
# 关闭alert窗口
ale = driver.switch_to.alert
# 获取文本提示
ale.text
# accept()/dismiss()
# send_keys()

# # 3.iframe切换:先确认是否要进行iframe切换
# # 1.下标2.名称name3.webelement
# # name
# driver = webdriver.Chrome()
# driver.get("https://ke.qq.com/")
# driver.maximize_window()
# WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.ID,"js_login")))
# driver.find_element_by_id("js_login").click()
# WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.XPATH,'//a[text()="QQ账号登录"]')))
# driver.find_element_by_xpath('//a[text()="QQ账号登录"]')
# WebDriverWait(driver,20).until(expected_conditions.frame_to_be_available_and_switch_to_it('login_frame_qq'))
# # driver.switch_to.frame(3)
# driver.switch_to.frame("login_frame_qq")
# # driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@name='login_frame_qq']"))
# time.sleep(1)
# driver.find_element_by_xpath('//a[@id="switcher_plogin"]').click()
#
# # 回到默认页面
# driver.switch_to.default_content()


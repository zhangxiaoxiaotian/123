#coding=utf-8
# *******************************************************************
#     Filename @  鼠标操作.py
#       Author @  XiaoTian
#  Create date @  2019/1/23 17:09
#        Email @  1075767641@qq.com
# ********************************************************************

from  selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
# 打开浏览器
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 设置按钮//div[@id='u1']//a[@name='tj_settingicon']

# 更多搜索//a[text()='高级搜索']
ActionChains(driver).move_to_element(driver.find_element_by_xpath("//div[@id='u1']//a[@name='tj_settingicon']")).perform()
WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.XPATH,"//a[text()='高级搜索']")))
driver.find_element_by_xpath("//a[text()='高级搜索']").click()


# 下拉框操作"//select[@name='ft']",三种方式，value属性，下标，名称
WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.XPATH,"//select[@name='ft']")))
s = Select(driver.find_element_by_xpath("//select[@name='ft']"))
s.select_by_value('rtf')
s.select_by_index(3)
s.select_by_visible_text('RTF 文件 （.rtf)')
#键盘操作
from selenium.webdriver.common.keys import Keys
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("柠檬班",Keys.ENTER)




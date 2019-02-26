#coding=utf-8
# *******************************************************************
#     Filename @  等待.py
#       Author @  XiaoTian
#  Create date @  2019/1/22 20:30
#        Email @  1075767641@qq.com
# ********************************************************************

from selenium import webdriver
import time
# 打开浏览器
driver = webdriver.Chrome()
# 方式二：隐形等待implicitly_wait
# driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

# 方式一:time.sleep()
# driver.find_element_by_xpath('//div[@id="u1"]//a[@name="tj_login"]').click()
# time.sleep(2)
# driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()
# time.sleep(5)
# driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("我爱小小小小天")
# driver.quit()


# 方式三：显性等待webdriverwait().until()
# 引入第三方库
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

# expected_conditions.visibility_of_element_located((By.XPATH,'//div[@id="u1"]//a[@name="tj_login"]'))
WebDriverWait(driver,10,1).until(expected_conditions.visibility_of_element_located((By.XPATH,'//div[@id="u1"]//a[@name="tj_login"]')))

driver.find_element_by_xpath('//div[@id="u1"]//a[@name="tj_login"]').click()
WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located((By.ID,'TANGRAM__PSP_10__footerULoginBtn')))
driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn').click()

driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("我爱小小小小天")
# driver.quit()

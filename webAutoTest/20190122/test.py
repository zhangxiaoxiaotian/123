#coding=utf-8
# *******************************************************************
#     Filename @  test.py
#       Author @  XiaoTian
#  Create date @  2019/1/22 20:17
#        Email @  1075767641@qq.com
# ********************************************************************

from selenium import webdriver
import time
# 打开浏览器
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.get("https://www.ketangpai.com")
# 全屏设置
driver.maximize_window()
# 回退到上个页面
driver.back()
# 到下一个界面
driver.forward()

# 获取当前页面标题
print(driver.title)
# 获取当前页面url
print(driver.current_url)
# 获取句柄
print(driver.window_handles)
# 刷新页面
driver.refresh()
# 关闭当前窗口
time.sleep(5)
driver.close()
# 关闭浏览器
driver.quit()
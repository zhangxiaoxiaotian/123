#coding=utf-8
# *******************************************************************
#     Filename @  index_elements.py
#       Author @  XiaoTian
#  Create date @  2019/2/20 10:19
#        Email @  1075767641@qq.com
# ********************************************************************

from selenium.webdriver.common.by import By
import random
#抢投标按钮
bid = (By.XPATH,"//a[@class='btn btn-special'][1]")

#随机取标
bid_num = random.randint(1,3)
quit_button_xpath = "//a[@class='btn btn-special'][bid_num]"
quit_button_xpath=quit_button_xpath.replace("bid_num",str(bid_num))

#退出按钮
quit_button = (By.XPATH,"//a[text()='退出']")
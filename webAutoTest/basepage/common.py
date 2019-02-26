#coding=utf-8
# *******************************************************************
#     Filename @  common.py
#       Author @  XiaoTian
#  Create date @  2019/2/21 17:16
#        Email @  1075767641@qq.com
# ********************************************************************
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium import webdriver
from basepage import file_dir
from basepage.my_log import mylogging
import datetime
import time

class Element_operation:
    def __init__(self,driver):
        self.driver = driver
    #等待元素加载
    def wait_element(self,modulename,Element):
        print(modulename, Element, self.driver)
        try:
            start_time = datetime.datetime.now()

            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Element))
            end_time = datetime.datetime.now()
            Consumption_time = (end_time-start_time).seconds
            mylogging().debug("元素{}出现，等待元素加载用时{}秒".format(Element,Consumption_time))
        except:
            now_time = datetime.datetime.now()
            present_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
            screenshot_save_path=file_dir.screenshot_path+'\\'+modulename
            self.driver.save_screenshot(screenshot_save_path)
            mylogging().debug("{},等待元素加载失败，页面截图保存路径{}".format(present_time,screenshot_save_path))
            raise
    # 元素查找
    def seek_element(self,modulename,Element):
        try:
            self.wait_element(modulename=modulename,Element=Element)
            element = self.driver.find_element(*Element)
            now_time = datetime.datetime.now()
            present_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
            mylogging().debug("{}，元素{}出现已找到".format(present_time,Element))
            return element

        except:
            now_time = datetime.datetime.now()
            present_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
            screenshot_save_path = file_dir.screenshot_path + '\\' + modulename
            self.driver.save_screenshot(screenshot_save_path)
            mylogging().debug("{}元素查找失败，页面截图保存路径{}".format(present_time, screenshot_save_path))
            raise
    # 元素单击
    def click_element(self,modulename,Element):
        try:
            now_time = datetime.datetime.now()
            present_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
            self.seek_element(modulename,Element).click()
            mylogging().debug("{}单击元素{}".format(present_time,Element))
        except:
            now_time = datetime.datetime.now()
            present_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
            screenshot_save_path = file_dir.screenshot_path + '\\' + modulename
            self.driver.save_screenshot(screenshot_save_path)
            mylogging().debug("{}元素查找失败，页面截图保存路径{}".format(present_time, screenshot_save_path))
            raise
    # 获取元素属性
    def get_element_attribute(self,modulename,Element,attribute):
        try:
            now_time = datetime.datetime.now()
            present_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
            # 获取属性
            self.seek_element(modulename,Element).get_attribute(attribute)
            mylogging().debug("{}单击元素{}".format(present_time,Element))
        except:
            now_time = datetime.datetime.now()
            present_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
            screenshot_save_path = file_dir.screenshot_path + '\\' + modulename
            self.driver.save_screenshot(screenshot_save_path)
            mylogging().debug("{}元素查找失败，页面截图保存路径{}".format(present_time, screenshot_save_path))
            raise
    # 获取元素文本内容
    def get_element_text(self,modulename,Element):
        try:
            now_time = datetime.datetime.now()
            present_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
            # 获取属性
            return self.seek_element(modulename,Element).text
            mylogging().debug("{}获取元素{}的文本内容".format(present_time,Element))
        except:
            now_time = datetime.datetime.now()
            present_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
            screenshot_save_path = file_dir.screenshot_path + '\\' + modulename
            self.driver.save_screenshot(screenshot_save_path)
            mylogging().debug("{}文本内容获取失败，页面截图保存路径{}".format(present_time, screenshot_save_path))
            raise
    # 文本输入
    def input_text(self,modulename,Element,content):
        try:
            now_time = datetime.datetime.now()
            present_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
            # 获取属性
            element = self.seek_element(modulename,Element)
            element.send_keys(content)
            mylogging().debug("{}在元素{}中输入文本内容".format(present_time,Element))
        except:
            now_time = datetime.datetime.now()
            present_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
            screenshot_save_path = file_dir.screenshot_path + '\\' + modulename
            self.driver.save_screenshot(screenshot_save_path)
            mylogging().debug("{}文本输入失败，页面截图保存路径{}".format(present_time, screenshot_save_path))
            raise
    # window窗口切换
    def switch_windows(self,modulename,Page_name=None,index=-1):
        try:
            time.sleep(2)
            windowhandles = self.driver.window_handles
            if Page_name==None and index==None:
                mylogging().debug("未输入指定的页签名称或者编号")
            else:
                if Page_name!=None:
                    for handle in windowhandles:
                        self.driver.switch_to.window(handle)
                        if self.driver.title == Page_name:
                            break
                else:
                    self.driver.switch_to.window(windowhandles[int(index)])
        except:
            now_time = datetime.datetime.now()
            present_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
            screenshot_save_path = file_dir.screenshot_path + '\\' + modulename
            self.driver.save_screenshot(screenshot_save_path)
            mylogging().debug("窗口切换失败")
            raise
        # alter窗口切换
    def switch_alter(self,modulename,result,get_text=0):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present())
            a = self.driver.switch_to.alter
            if get_text == 0:
                if result == "accept":
                    a.accept()
                    self.driver.switch_to_default_content()
                else:
                    a.dismiss()
                    self.driver.switch_to_default_content()
            else:
                if result == "accept":
                    textcontent = a.text
                    a.accept()
                    self.driver.switch_to_default_content()
                    return textcontent
                else:
                    textcontent = a.text
                    a.dismiss()
                    self.driver.switch_to_default_content()
                    return textcontent
        except:
            now_time = datetime.datetime.now()
            present_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
            screenshot_save_path = file_dir.screenshot_path + '\\' + modulename
            self.driver.save_screenshot(screenshot_save_path)
            mylogging().debug("窗口切换失败")
            raise
#     iframe切换
    def switch_iframe(self,modulename,Element=None):
        try:
            WebDriverWait(self.driver, 20).until(
                expected_conditions.frame_to_be_available_and_switch_to_it(Element))
        except:
            now_time = datetime.datetime.now()
            present_time = now_time.strftime('%Y-%m-%d %H:%M:%S')
            screenshot_save_path = file_dir.screenshot_path + '\\' + modulename
            self.driver.save_screenshot(screenshot_save_path)
            mylogging().debug("窗口切换失败")
            raise



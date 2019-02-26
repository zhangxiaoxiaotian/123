#coding=utf-8
# *******************************************************************
#     Filename @  file_dir.py
#       Author @  XiaoTian
#  Create date @  2019/2/21 17:16
#        Email @  1075767641@qq.com
# ********************************************************************
import os
import time
cuurent_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
# 根目录
root_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# 截图存放路径
screenshot_path = os.path.join(root_path,"screenshot_dir")
# 日志截图
log_path = os.path.join(root_path,"log")
log_file = os.path.join(log_path,cuurent_time+".log")

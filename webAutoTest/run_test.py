#coding=utf-8
# *******************************************************************
#     Filename @  run_test.py
#       Author @  XiaoTian
#  Create date @  2019/2/20 15:51
#        Email @  1075767641@qq.com
# ********************************************************************
import unittest
import HTMLTestRunnerNew
import os
dir_report = os.path.split(os.path.realpath(__file__))[0]
report_dir = os.path.join(dir_report,"test.html")
case_dir = os.path.join(dir_report,"testcases")
descover = unittest.defaultTestLoader.discover(case_dir,pattern='test*', top_level_dir=None)
with open(report_dir,'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,title='测试报告',description='一次测试实验',tester='xiaotian')
    runner.run(descover)

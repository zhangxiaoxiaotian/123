#coding=utf-8
# *******************************************************************
#     Filename @  logging.py
#       Author @  XiaoTian
#  Create date @  2019/2/24 16:09
#        Email @  1075767641@qq.com
# ********************************************************************
import logging
from basepage import file_dir
class mylogging:
    def log_set(self,msg,level):
        # 创建日志收集器
        mylogger = logging.getLogger("log")
        mylogger.setLevel("DEBUG")
        # 指定日志文件存放路径
        logfile = logging.FileHandler(file_dir.log_file,encoding="utf-8")
        logfile.setLevel("DEBUG")
        # 设定日志收集格式
        formater = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(name)s - 日志内容:%(message)s")
        logfile.setFormatter(formater)
        # 对接
        mylogger.addHandler(logfile)
        if level == 'debug':
            mylogger.debug(msg)
        elif level == 'info':
            mylogger.info(msg)
        elif level == 'warning':
            mylogger.warning(msg)
        elif level == 'error':
            mylogger.error(msg)
        elif level == 'critical':
            mylogger.critical(msg)
        mylogger.removeHandler(logfile)
    def debug(self,msg):
        self.log_set(msg,"debug")
    def info(self,msg):
        self.log_set(msg, "info")



if __name__ == '__main__':
    my = mylogging()
    my.debug("1233{}".format(111))
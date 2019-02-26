#coding=utf-8
# *******************************************************************
#     Filename @  login _datas.py
#       Author @  XiaoTian
#  Create date @  2019/2/19 15:09
#        Email @  1075767641@qq.com
# ********************************************************************
# 登录成功
suc_data={"user":"18684720553","password":"python"}
# 登录失败
fail_datas = [{"user":"18684720553","password":"","check":"请输入密码"},
         {"user":"","password":"python","check":"请输入手机号"},
         {"user":"1868472","password":"python","check":"请输入正确的手机号"}]
#登录失败-提示在页面中心
wrong_login = [{"user":"18684720000","password":"python","check":"此账号没有经过授权，请联系管理员!"},
         {"user":"18684720553","password":"111111","check":"帐号或密码错误!"}]
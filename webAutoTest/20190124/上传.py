#coding=utf-8
# *******************************************************************
#     Filename @  上传.py
#       Author @  XiaoTian
#  Create date @  2019/1/24 16:39
#        Email @  1075767641@qq.com
# ********************************************************************
import win32con
import win32gui
def upload(file_path,browser='chrome'):
    if browser == 'chrome':
        text = '打开'
    elif browser== 'firefox':
        text = '文件上传'

    dialog = win32gui.FindWindow("#32770",text)
    ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32,0,"ComboBox",None)
    edit = win32gui.FindWindowEx(ComboBox,0,"Edit",None)
    button = win32gui.FindWindowEx(dialog,0,"Button","打开(&O)")

    win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,file_path)#发送文件路径
    win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)#点击打开按钮

if __name__ == '__main__':
    up = upload("D:\\python12_xiaotian.zip")

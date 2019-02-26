#coding=utf-8
# *******************************************************************
#     Filename @  conftest.py
#       Author @  XiaoTian
#  Create date @  2019/2/26 10:45
#        Email @  1075767641@qq.com
# ********************************************************************
import pytest
@pytest.fixture(scope="class")
def prepare():
    # 前置条件
    yield #后面可以带上一个返回的变量，使用时直接使用函数名称来代表返回值，调用时在用例中传入该变量
    # 后置条件
    pass
@pytest.fixture
def refresh():
    # 前置条件
    yield
    # 后置条件
    pass
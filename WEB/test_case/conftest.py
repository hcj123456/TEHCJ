#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:huangCijin
# datetime:2020/11/20 10:44
# software: PyCharm
# import pytest
# from pluggy import HookspecMarker
#
# hookspec = HookspecMarker("pytest")
#
#
# # 1. 调用钩子方法，获取到用例对象并赋值给全局变量
# @hookspec(firstresult=True)
# def pytest_runtest_protocol(item, nextitem):
#     # print()
#     # print('执行hook方法，将 item,nextitem 赋值全局变量')
#     print('当前用例的对象', item)
#     print('下一个用例的对象', nextitem)
#     global Item, NextItem
#     Item = item
#     NextItem = nextitem
#
#
# # 2. 创建一个 fixture，从全局变量的用例对象中获取用例名
# @pytest.fixture(autouse=True)
# def print_fix():
#     print()
#     name = Item.name
#
#     # 3. 注意，如果是最后一条用例执行前调用钩子方法，那么 NextItem 则是 None；
#     if NextItem:
#         next_name = NextItem.name
#     else:
#         next_name = None
#     print('要执行用例的名称：', name)
#     print('预计下一个测试用例的名称', next_name)
#
#
# if __name__ == '__main__':
#     pytest.main(['-s', '-q'])


import pytest


@pytest.fixture(autouse=True)
def fix_result():
    # setup
    print("我说的是对的，怎么了")
    yield
    # teardown
    print("怎么了，你有意见嘛")


# 1. 调用钩子方法, item 参数这里不用
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport():
    print('------------------------------------')

    # 2. 获取钩子方法的调用结果
    result = yield
    print('钩子方法的执行结果', result)
    # 3. 从钩子方法的调用结果中获取测试报告
    report = result.get_result()

    print('从结果中获取测试报告：', report)
    # print('从报告中获取 nodeid：', report.nodeid)
    print('从报告中获取调用步骤：', report.when)
    print('从报告中获取执行结果：', report.outcome)


if __name__ == '__main__':
    pytest.main(['-s', '-q'])
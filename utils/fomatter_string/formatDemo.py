#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/1/6/006 10:38
# software: PyCharm
string01 = "{} {}".format("hello", "world")
print(string01)
string02 = "{} aaabbbccc {}".format("hello", "world")
print(string02)
string03 = "{1} {0} {1}".format("hello", "world")
print(string03)
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
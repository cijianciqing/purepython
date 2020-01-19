#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/1/8/008 10:14
# software: PyCharm
class ClassDemo01(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender= gender

    def myName00(self):
        print('My name is :',self.name)
        return 'hello'

class00 = ClassDemo01('111',11)
print(class00.name)
print(type(class00.myName00))

func01 = class00.myName00
print('func00() : '+ func01())
# func01()
#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/1/6/006 10:25
# software: PyCharm

class ClassDemo01(object):
    def __init__(self,name,gender):
        self.name = name
        self.gender= gender

    def myName00(self):
        print('My name is :',self.name)

if __name__ == '__main__':
    p03 = ClassDemo01()
    p01 = ClassDemo01('wqn','男')
    p01.myName00()
    p02 = ClassDemo01('lihui')
    p02.myName00()
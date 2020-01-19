#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/1/15/015 15:03
# software: PyCharm

def log01(func):
    def myWrapper(*args,**kw):
        print("the function name is {}".format(func.__name__))
        return func(*args, **kw)
    return myWrapper

'''
把@log01放到testFunc()函数的定义处，相当于执行了语句：
testFunc = log01(testFunc)
'''
@log01
def testFunc(arg01):
    return arg01+1


if __name__ == '__main__':
   b =  testFunc(2)
   print(testFunc.__name__)
   print(b)


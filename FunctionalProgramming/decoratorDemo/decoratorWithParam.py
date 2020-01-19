#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/1/15/015 15:23
# software: PyCharm
import functools

def log01(decoratorParam):
    def decorator(func):
        @functools.wraps(func)
        def myWrapper(*args,**kw):
            print("the function name is {},the decoratorParam is {}".format(func.__name__,decoratorParam))
            return func(*args, **kw)
        return myWrapper
    return decorator

'''
把@log01放到testFunc()函数的定义处，相当于执行了语句：
testFunc = log01('execute')(testFunc)
'''
@log01('Debug')
def testFunc(arg01):
    return arg01+1


if __name__ == '__main__':
   b =  testFunc(2)
   print(b)
   #经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper',需要添加@functools.wraps(func)
   print(testFunc.__name__)
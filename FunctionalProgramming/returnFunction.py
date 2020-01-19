#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2020/1/15/015 15:11
# software: PyCharm

def aa(func):
    return func

def function01():
    print('bbbb')
    return 'aaaaa'

if __name__ == '__main__':
    bb = aa(function01)
    print(type(bb))
    cc = bb()
    print(cc)
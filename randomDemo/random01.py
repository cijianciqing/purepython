#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Administrator
# datetime:2019/12/31/031 9:57
# software: PyCharm

import random
import string

ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print (ran_str)
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 19:46:08 2020

@author: 蒋冰
"""
import re
x = 'From robot@zju.edu.cn Feb 10:38:06 2019 '
y = re.findall(r'^From (\S+@)',x)
print(y)

import re
s = input()
'abcdefghi_def'
result = re.sub(r'abc(def)ghi', r'\1',s)
print(result)


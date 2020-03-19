# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 17:47:59 2020

@author: 蒋冰
"""

import numpy as np
import matplotlib.pyplot as plt
scores =(25,75,75,25)
std = (2,3,4,1)
N=4
ind=np.arange(N)
width=0.5
p1= plt.bar(ind,scores,width,yerr=std)
plt.ylabel('percentage of attacked models')
plt.title('beach habitat              inland habitat')
plt.xticks(ind,('light models','dark models','light models','dark models'))
plt.yticks(np.arange(0,101,10))
plt.show()
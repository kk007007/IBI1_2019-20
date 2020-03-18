# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:08:11 2020

@author: 蒋冰
"""

gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
gene_lengths1=sorted(gene_lengths)
del(gene_lengths1[9])
del(gene_lengths1[0])
print(gene_lengths1)

import numpy as np
import matplotlib.pyplot as plt
score = gene_lengths1
plt.boxplot(score,vert=True,whis=1.5,patch_artist=True,meanline=True,showmeans=True,showbox=True,showcaps=True,
            showfliers=True,notch=False,boxprops = {'facecolor':'orange'})
plt.title('Gene',fontsize=20)
plt.show()

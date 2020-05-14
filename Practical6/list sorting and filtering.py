# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:08:11 2020

@author: 蒋冰
"""
#plan:import the 10 gene lengths,sort and delete the maximum and minimum, then use boxplt to plot
#import the length
gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
#sort the input data
gene_lengths1=sorted(gene_lengths)
#follwing the guide, we need to delete the maximun and the minimum
#delete the largest value
del(gene_lengths1[9])
#delete the smallest value
del(gene_lengths1[0])
print(gene_lengths1)
# start making plot
#import libraries 
import numpy as np
import matplotlib.pyplot as plt
score = gene_lengths1
#the boxplot is orange and contains meanline
plt.boxplot(score,vert=True,#make the boxplot vertical
            whis=1.5,#specify the distance between top and bottom line and the quartile
            patch_artist=True,#fill the box with color
            showmeans=True,#show mean
            showbox=True,#show box
            showcaps=True,#show the top and bottom line
            showfliers=True,# show abnormal values
            notch=False,# no notch
            boxprops = {'facecolor':'orange'})# color is orange
#set the title
plt.title('Gene',fontsize=20)
plt.show()

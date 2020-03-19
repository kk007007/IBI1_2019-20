# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:20:24 2020

@author: 蒋冰
"""
A0 = 0
C0= 0
G0 = 0
T0 = 0
genes = {}
DNA = 'ATGCTTCAGAAAGGTCTTACG'
for i in DNA:
    if i == 'A':
        A0 += 1
genes['A']=A0
for i in DNA:
    if i == 'C':
        C0 += 1
genes['C']=C0
for i in DNA:
    if i == 'G':
        G0 += 1
genes['G']=G0
for i in DNA:
    if i == 'T':
        T0 += 1
genes['T']=T0
print(genes)
#start making plot
import matplotlib.pyplot as plt
labels = 'A','C','G','T'
sizes = [A0,C0,G0,T0]
explode=[0.1,0.1,0,0]
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.title('pie of the four DNA nucleotides')
plt.show




        
        
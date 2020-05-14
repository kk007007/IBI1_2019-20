# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:20:24 2020

@author: 蒋冰
"""
#plan：first input the number of ATCG and add it into frequency dictionary, then plot a pie 
#input the number of time that that the symbok 'A','T','C','G' occur in the DNA string
A0 = input("number of 'A':")
C0= input("number of ''C:")
G0 = input("number of 'G':")
T0 = input("number of 'T':")
#set up a frequency dictionary called 'genes'
genes = {}
#document the information into the dictionary, count A,C,G,T
genes['A']=A0
genes['C']=C0
genes['G']=G0
genes['T']=T0
#print the frequency dictionary
print('\n',genes)
#start making plot
#import libraries
import matplotlib.pyplot as plt
labels = 'A','C','G','T'#add labels
sizes = [A0,C0,G0,T0] # fill in the values
explode=[0.1,0.1,0.1,0.1]# seperate them euqally
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%'# one significant digit
        ,shadow=False,startangle=90)
plt.axis('equal')
#set the title
plt.title('pie of the four DNA nucleotides')
plt.show




        
        
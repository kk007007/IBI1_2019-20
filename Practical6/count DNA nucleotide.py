# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:20:24 2020

@author: 蒋冰
"""
#plan：first input the number of ATCG and add it into frequency dictionary, then plot a pie 
# input the DNA sequence
sequence=input("please input a sequence of DNA:")
#count the number of each nucleotide in the sequence
a=sequence.count("A")#count 'A'
g=sequence.count("G")#count 'G'
c=sequence.count("C")#count 'C'
t=sequence.count("T")#count 'T'
#create sunch a dictionary
dictionary={"A":a,"G":g,"C":c,"T":t}
#print the frequency dictionary
print("the frequency dictionary is:\n {}".format(dictionary))
#start making plot
#import libraries
import matplotlib.pyplot as plt
labels = 'A','C','G','T'#add labels
sizes = [a,g,c,t] # fill in the values
explode=[0.1,0.1,0.1,0.1]# seperate them euqally
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%'# one significant digit
        ,shadow=False,startangle=90)
plt.axis('equal')
#set the title
plt.title('pie of the four DNA nucleotides')
plt.show




        
        
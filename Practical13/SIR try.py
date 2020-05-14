# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:54:24 2020

@author: 蒋冰
"""
#import libraries
import numpy as np
import matplotlib.pyplot as plt 
# need : Four variables seperately indicates the number of total population, susceptible people ,infected people and recover people
N = 10000
susceptible = 9999
infected = 1
recovered = 0
# beta indicates the infection probability upon contact, gamma indicates the recover probability
beta = 0.3
gamma = 0.05
#creat arrays(S,I,R) to track the evolvement of different population
S = []#track susceptible
I = []#tract infected
R = []#track recovered
# list X was used to function as the x axis
X = []
# funtion 'delete' used to delete the unwanted elements
#reference: the idea of creat a function to delete unwanted numbers was inspired by a classmates Qi Liu
def delete(l,e):
        while e in l:
            l.remove(e)
        return l
# need : variable 'a' indicated the contact rate, variable 'c' indicates the infected possibility
# run 1000 times
for i in range(1000):
    a = infected/N
    c = a*beta
    b = 1- c
    X.append(i)
# need : use 'np.random.choice' to randomly collected infected people and recovered people
#'0' indicates recovered and '1' indicates infected
    e = np.random.choice(range(2),susceptible,p=[1-c,c])
    f = e.tolist()
# delete all the '0' in the list and remain a list contains various '1'
# use len method to get out the number of infected people in this turn
    S2 = len(delete(f,0))
    susceptible = susceptible - S2
    S.append(susceptible)
    #add new infected people
    infected += S2
# line 49~51 used similar method mentiond before to get recovered people
    g = np.random.choice(range(2),infected,p=[0.95,0.05])
    h = g.tolist()
    I2 = len(delete(h,0))
    # minus recovered people from infected
    infected = infected - I2
    # add new recoverd people
    recovered += I2
    R.append(recovered)
    I.append(infected)
#plot
plt.figure(figsize=(6,4),dpi =150)
#reference about the line type: https://blog.csdn.net/sinat_36219858/article/details/79800460?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase
plt.plot(X,S,'r+',marker = ',',linestyle = '-',label = 'Susceptible')
plt.plot(X,I,'b+',marker = ',',linestyle = '-',label = 'Infected')
plt.plot(X,R,'g+',marker = ',',linestyle = '-',label = 'Recovered')
plt.title('SIR model')
plt.xlabel('time')
plt.ylabel('number of people')
plt.legend()
plt.savefig("simulation of SIR model",type="png" )







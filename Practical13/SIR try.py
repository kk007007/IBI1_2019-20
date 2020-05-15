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
susceptible = 9999#set original susceptible numbers
infected = 1#set original infected numbers
recovered = 0#set original recovered numbers
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
    a = infected/N# each turn calculate new contact rate
    c = a*beta#each turn calculate new infected possibility
    b = 1- c
    X.append(i)#add i in list X to form the final x axis
# need : use 'np.random.choice' to randomly collected infected people and recovered people
#'0' indicates recovered and '1' indicates infected
    e = np.random.choice(range(2),susceptible,p=[1-c,c])
    #convert to list format
    #refence:https://blog.csdn.net/gqixf/article/details/82743662
    f = e.tolist()
# delete all the '0' in the list and remain a list contains various '1'
# use len method to get out the number of infected people in this turn
    S2 = len(delete(f,0))#calculate new infected people
    susceptible = susceptible - S2#minus new infected people from susceptible population
    S.append(susceptible)#add nubers of susceptible to list to help tract the evolvement ot susceptible population
    #add new infected people to infected population
    infected += S2
# line 51~55 similar method mentiond before to get recovered people
    g = np.random.choice(range(2),infected,p=[0.95,0.05])
    #convert to list format
    #refence:https://blog.csdn.net/gqixf/article/details/82743662
    h = g.tolist()
    I2 = len(delete(h,0))#calculate new recovered people
    # minus recovered people from infected
    infected = infected - I2
    # add new recoverd people to recovered population
    recovered += I2
    R.append(recovered)#add nubers of recored to list to help tract the evolvement ot recovered population
    I.append(infected)#add nubers of infected to list to help tract the evolvement ot infected population
#plot
plt.figure(figsize=(6,4),dpi =150)
#reference about the line type: https://blog.csdn.net/sinat_36219858/article/details/79800460?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase
plt.plot(X,S,'r+',marker = ',',linestyle = '-',label = 'Susceptible')
plt.plot(X,I,'b+',marker = ',',linestyle = '-',label = 'Infected')
plt.plot(X,R,'g+',marker = ',',linestyle = '-',label = 'Recovered')
plt.title('SIR model')#add title
plt.xlabel('time')# add x label
plt.ylabel('number of people')#add y label
plt.legend()
plt.savefig("simulation of SIR model",type="png")#save image







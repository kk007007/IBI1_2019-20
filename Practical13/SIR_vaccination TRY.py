# -*- coding: utf-8 -*-
"""
Created on Tue May 12 17:12:36 2020

@author: 蒋冰
"""
# import libraries
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import cm
I = {}
# funtion 'delete' used to delete the unwanted elements
#reference: the idea of creat a function to delete unwanted numbers was inspired by a classmates Qi Liu
def delete(l,e):
        while e in l:
            l.remove(e)
        return l
#use 'for j in range(11) to simulate the vaccination rate from 0% to 100%
for j in range(11):
#When vaccination rate reaches 100%, there will be no susceptible and infected, thus we need to take classified discussion
    if j !=10:
# similar mechnism to task1 
# need : Four variables seperately indicates the number of total population, susceptible people ,infected people and recover people
        #each turn vaccination rate will increase 10%
        Vaccine_rate = j/10
        N = 10000
        #get the susceptible population number
        susceptible = 9999 - Vaccine_rate*N
        infected = 1
        recovered = 0
# beta indicates the infection probability upon contact, gamma indicates the recover probability
        beta = 0.3
        gamma = 0.05
#use I[j] to store the result of each turn to tract infected population, and need to empty I[j] each turn
# need : variable 'a' indicated the contact rate, variable 'c' indicates the infected possibility
        I[j] = []
        # list X was used to function as the x axis
        X = []
        # under each vaccination circumstance, run 1000times to simulate
        for i in range(1000):
            #variable 'a' indicated the contact rate
            a = infected/N
            #variable 'c' indicates the infected possibility
            c = a*beta
            b = 1- c
            # each turn X add i to form the x axis
            X.append(i)
# need : use 'np.random.choice' to randomly collected infected people and recovered people
#'0' indicates recovered and '1' indicates infected
            e = np.random.choice(range(2),int(susceptible),p=[1-c,c])
            #convert to list format
            #refence:https://blog.csdn.net/gqixf/article/details/82743662
            f = e.tolist()
# delete all the '0' in the list and remain a list contains various '1'
# use len method to get out the number of infected people in this turn
            S2 = len(delete(f,0))
            susceptible = susceptible - S2
            #add new infected people
            infected += S2
#similar method mentiond before to get recovered people
            g = np.random.choice(range(2),infected,p=[0.95,0.05])
            #convert to list format
            h = g.tolist()
            I2 = len(delete(h,0))
            #delete new recovered people from infected population
            infected = infected - I2
            I[j].append(infected)
    else:
#mentioned in line 20
        I[j] = []
        X = []
        for i in range(1000):  
            #each turn X add i to form the x axis
            X.append(i)
            # no infected people, thus add 0 each turn
            I[j].append(0)
#plot 11 lines together, change color through changing the number after cm.viridis to seperate each lines
#reference about the line type: https://blog.csdn.net/sinat_36219858/article/details/79800460?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase
plt.figure(figsize=(6,4),dpi =150)
plt.plot(X,I[0],color = cm.viridis(30),marker = ',',linestyle = '-',label = '0%')
plt.plot(X,I[1],color = cm.viridis(80),marker = ',',linestyle = '-',label = '10%')
plt.plot(X,I[2],color = cm.viridis(100),marker = ',',linestyle = '-',label = '20%')
plt.plot(X,I[3],color = cm.viridis(150),marker = ',',linestyle = '-',label = '30%')
plt.plot(X,I[4],color = cm.viridis(200),marker = ',',linestyle = '-',label = '40%')
plt.plot(X,I[5],color = cm.viridis(250),marker = ',',linestyle = '-',label = '50%')
plt.plot(X,I[6],color = cm.viridis(300),marker = ',',linestyle = '-',label = '60%')
plt.plot(X,I[7],color = cm.viridis(350),marker = ',',linestyle = '-',label = '70%')
plt.plot(X,I[8],color = cm.viridis(400),marker = ',',linestyle = '-',label = '80%')
plt.plot(X,I[9],color = cm.viridis(450),marker = ',',linestyle = '-',label = '90%')
plt.plot(X,I[10],color = cm.viridis(500),marker = ',',linestyle = '-',label = '100%')
plt.title('SIR model with different vaccination rate')
plt.xlabel('time')
plt.ylabel('number of people')
plt.legend()
plt.savefig("simulation with different vaccination rate",type="png" )
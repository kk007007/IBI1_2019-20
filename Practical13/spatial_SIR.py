# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:35:06 2020

@author: 蒋冰
"""
# import necessary libraries 
import numpy as np 
import matplotlib.pyplot as plt
# make array of all susceptible population 
population = np.zeros((100,100))
#creat one random infected people 
outbreak = np.random.choice(range(100),2)
population[outbreak[0] ,outbreak[1]]=1
#plot the first figure which only contains one infected people
plt.figure(figsize =(6,4),dpi=150) 
plt.imshow(population,cmap='viridis',interpolation='nearest')
plt.savefig("spatial 0%",type="png" )
# beta indicates the infection probability upon contact, gamma indicates the recover probability
beta = 0.3
gamma = 0.05
#run 100 times
for i in range(100):
    infectedIndex = np.where(population==1)
    #simulate the recover process
    for j in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][j]
        y = infectedIndex[1][j]
        # infected prople randomly recovered, the infect rate was set as 0, recovered was represented by number 2
        population[x,y]=np.random.choice(range(3),1,p=[0,1-gamma,gamma])[0]
#reference: line 31 - 48 was provided by teacher
# find infected points
    infectedIndex = np.where(population==1)
# loop through all infected points
    for k in range(len(infectedIndex[0])):
    # get x, y coordinates for each point
        x = infectedIndex[0][k]
        y = infectedIndex[1][k]
    # infect each neighbour with probability beta
    # infect all 8 neighbours (this is a bit finicky, is there a better way?):
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
            # don't infect yourself! (Is this strictly necessary?)
                if (xNeighbour,yNeighbour) != (x,y):
                # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                    # only infect neighbours that are not already infected!
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
# plot when vaccination rate is 10%,50% and 100%
    if i ==9:
        plt.figure(figsize =(6,4),dpi=150) 
        plt.imshow(population,cmap='viridis',interpolation='nearest')
        plt.savefig("spatial 10%",type="png" )
    elif i ==49:
        plt.figure(figsize =(6,4),dpi=150) 
        plt.imshow(population,cmap='viridis',interpolation='nearest')
        plt.savefig("spatial 50%",type="png" )
    elif i ==99:
        plt.figure(figsize =(6,4),dpi=150) 
        plt.imshow(population,cmap='viridis',interpolation='nearest')
        plt.savefig("spatial 100%",type="png" )
        
        
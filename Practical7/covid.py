# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 16:49:56 2020

@author: 蒋冰
"""
#import libraries
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
#read full_data.csv
covid_data = pd.read_csv("full_data.csv")
#show all columns, and every third row between (and including) 0 and 15
print(covid_data.iloc[0:16:3,:],'\n')          
#code for finding the totoal cases in Afghanistan
a = covid_data.loc[:,"location"] == 'Afghanistan'
#find the total row number and assign it to variablt c
b = covid_data.describe()
c = int((b.iloc[0,0]))
d = []#list d was used to store row numbers that location is Afghanistan
for i in range(c):
#find out the row with the location Afghanistan
    if a[i] == True:
        d.append(i)
print('Afghanistan total case:')
print(covid_data.loc[d,"total_cases"])
#creat  world_new_cases 
#find out the row with the location world
e = covid_data.loc[:,"location"] == 'World'
#get the total row number and assign it to  g
f = covid_data.describe()
g = int((f.iloc[0,0]))
j = []#list j was used to store row numbers that location is world
for i in range(g):
    #find out the row with the lication world
    if e[i] == True:
        # document the row number
        j.append(i)
# use row number to find world new cases
world_new_cases = covid_data.loc[j,"new_cases"]
#calculate meam and median
mean = np.mean(world_new_cases)
median = np.median(world_new_cases)
print('\n','the mean of new cases for the entire world is :',mean)#print mean
print('\n','the median of new cases for the entire world is: ',median)#print median
#plot boxplot of world new cases
plt.boxplot(world_new_cases,
            vert=True,#make the boxplot vertical
            whis=1.5,#specify the distance between top and bottom line and the quartile
            patch_artist=True,#fill the box with color
            meanline=True,#show mean line
            showbox=True,#show box
            showcaps=True,#show the top and bottom line
            showfliers=True,# show abnormal values
            notch=False# no notch
            )
plt.title('world new cases')#add title
plt.show()
# fetch dates as the x axis
world_dates = covid_data.loc[j,"date"]
covid_data.loc[j,["date","new_deaths"]]
#creat world new death 
world_new_deaths=[]
#store the number of world new death
world_new_deaths = covid_data.loc[j,"new_deaths"]
#plot world new cases in blue color, world new deaths in red color
plt.plot(world_dates, world_new_deaths, 'r+')
plt.plot(world_dates, world_new_cases, 'b+')
plt.ylabel('Numbers')#add y label
plt.xlabel('Date')#add x label
plt.title('Daily new cases and new death')#add title
    #interval of dates is 4 and clockwise rotate 90 degree
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()
##### find the country has less than 10 total deaths cases (till 2020.3.31)
#get out the data with date'2020-03-31'
a = covid_data.loc[:,"date"] == '2020-03-31'
#find the total row number that date is 2020-03-31 and assign it to variablt c
b = covid_data.describe()
c = int((b.iloc[0,0]))
d = []# list d used to store row number that date is 2020-03-31 and the total death number smaller than 10
# find the country with total death less than 10
e = covid_data.loc[:,"total_deaths"]  < 10
for i in range(c):
    # find out the circumstance that date is 2020-03-31 and the total death number smaller than 10
    if a[i] and e[i]:
        d.append(i)
#print the result
print('\n','The country had less than 10 death cases')
print(covid_data.loc[d,["date","location","total_deaths"]])







        
        












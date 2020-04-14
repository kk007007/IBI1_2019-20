# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 16:49:56 2020

@author: 蒋冰
"""

import os
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
os.chdir("D:\GitKraken\IBI1_2019-20\Practical7")
covid_data = pd.read_csv("full_data.csv")
#show all rows, and every third column between (and including) 0 and 15
#need to check
covid_data.iloc[0:16,0:6:3]            
#code for finding the totoal cases in Afghanistan
a = covid_data.loc[:,"location"] == 'Afghanistan'
b = covid_data.describe()
c = int((b.iloc[0,0]))
d = []
for i in range(c):
    if a[i] == True:
        d.append(i)
print(covid_data.loc[d,"total_cases"])
####creat  world_new_cases 
e = covid_data.loc[:,"location"] == 'World'
f = covid_data.describe()
g = int((f.iloc[0,0]))
j = []
h = []
for i in range(g):
    if e[i] == True:
        j.append(i)
covid_data.loc[j,["date","new_cases"]]
world_new_cases=[]
world_new_cases = covid_data.loc[j,"new_cases"]
##calculate meam and median
import numpy as np
import matplotlib.pyplot as plt
np.mean(world_new_cases)
np.median(world_new_cases)
######plot box need to check
import matplotlib.pyplot as plt
import numpy as np
plt.boxplot(world_new_cases.loc[:,"new_cases"],
            vert=True,whis=1.5,patch_artist=True,
            meanline=True,showbox=True,showcaps=True,
            showfliers=True,notch=False)
#####'b+' plot x-y figure in blue color
world_dates = covid_data.loc[j,"date"]
plt.plot(world_dates, world_new_cases, 'b+')
#####'r+' plot x-y figure in red color
plt.plot(world_dates, world_new_cases, 'r+')
#####'bo' make the point bold
plt.plot(world_dates, world_new_cases, 'bo')
##### creat both new death and new cases
k = covid_data.loc[:,"location"] == 'World'
l = covid_data.describe()
m = int((l.iloc[0,0]))
n = []
p = []
for i in range(m):
    if e[i] == True:
        n.append(i)
covid_data.loc[j,["date","new_deaths"]]
world_new_deaths=[]
world_new_deaths = covid_data.loc[j,"new_deaths"]
plt.plot(world_dates, world_new_deaths, 'r+')
plt.plot(world_dates, world_new_cases, 'b+')
plt.ylabel('Numbers')
plt.xlabel('Date')
plt.title('Daily new cases and new death')
#####interval is 4 and clockwise rotate 90 degree
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)






        
        












# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:50:04 2020

@author: 蒋冰
"""
#Here are 3 methods in total, method 3 is the best.
##method 1
import random
x = random.randint(1,8192)
x1=x
# we first need to list the first one 
for i in range(0,14):
        j=13-i
        if x>=2**j and x<2**(j+1):
            m=j
            break
x=x-2**m
# then we add the rest nunmbers step by step
#end="" was used to make sure the outcome were in the same line
#if x=0, we need to discuss it seperately
if x==0:
    print(x1,"is","2**",m)
while x!=0: 
    print(x1,"is",sep=" ",end="")
    print("2**",m,sep="",end=" ")
    for i in range(0,14):
        j=13-i
        if x>=2**j:
            print("+","2**",j,sep="",end=" ")
            x=x-2**j
            
            
            


#method 2
import random
x = random.randint(1,8192)
x1=x
print(x,"is",sep=" ",end="")
for i in range(0,14):
        j=13-i
        if x>2**j:
            print("2**",j,sep=" ",end="")
            print("+",end="")
            x=x-2**j
        elif x==2**j:
            print("2**",j,end="")
            x=x-2**j
            
#method 3
#use the knowledge of transfering decimalism into binary system
x=1500
y=x
a=str()
b=0
while y>=2:
    if y%2==0:
        b=b+1
    else:
        a="+" + "2**"+ str(b)+ str(a)
        b=b+1
        
    y=(y-y%2)/2
a = "2**" + str(b) +str(a)
print(x,"=",str(a))





    









            
            
            
            
            
            
            
            
            
            
            
            


        
        

        

        
        


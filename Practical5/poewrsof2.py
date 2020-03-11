# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:50:04 2020

@author: 蒋冰
"""
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
x=19
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



            
            
            
            
            
            
            
            
            
            
            
            


        
        

        

        
        


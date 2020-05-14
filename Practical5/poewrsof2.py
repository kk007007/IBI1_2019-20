# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 10:50:04 2020

@author: 蒋冰
"""
#plan: found the biggest powers of 2 which is equal to or smaller than the input number. Minus it. And then find the subsequent biggest power of 2 and minus it. continue until the number reaches 0.
#we input a positive integer to x, for example 2019 in the script
input_number = input('please input a number:')
x = int(input_number)
#the use of (sep="", end="") is to make the print result in the same line
print(x,"is ",sep=" ",end="")
#we assume that x is no	larger than	8192 which is 2**13
for i in range(0,14):
        j=13-i
#To find the biggest power of 2, we test from 2**13 down to 2**0
#if the number is not exactly the power of 2, we can find the current biggest power of 2 which is small than it 
        if x>2**j:
            print("2**",j,sep=" ",end="")
            print(" + ",end="")
#minus the current biggest power of 2
            x=x-2**j
#if the number is the power of 2, than the number itself is what we want
        elif x==2**j:
            print("2**",j,end="")
#minus the  power of 2
            x=x-2**j









    









            
            
            
            
            
            
            
            
            
            
            
            


        
        

        

        
        


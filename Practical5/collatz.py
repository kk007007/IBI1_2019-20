# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 09:58:19 2020

@author: 蒋冰
"""
#Collatz sequence: The obtained number will be divided by 2 (if it is even) or multiplying by 3 and add 1(is it is odd), the process will continue until first reaches 1
#plan: The user input a positive interger to function as the start number of the collatz sequence
start_number = input('please input a positive integer :')
#the product of input function is a string, we use float function to change the input positive number from string to integer 
n = float(start_number)
#plan: do classified discussion, if the input number is 1, fisrt multiply by 3 and add 1, then use while loop to do conduct collatz sequence
if n ==1:
    n=3*n+1
    print(n)
#use while loop to conduct collatz sequence, continue until reaches 1 
    while n!=1:
        if n%2==0:
#if number is even, divided by 2
            n=n/2
#print current number out to show the process
            print(n)
#if number is odd but not 1, multiplied by 3 and add 1 
        else:
            n=3*n+1
#print current number out to show the process
            print(n)  
#plan:if the input number is not 1, use while loop to conduct collatz sequence until reaches 1 
while n!=1:
#if number is even, divided by 2
    if n%2==0:
        n=n/2
#print current number out to show the process
        print(n)
#when number is odd but not 1, multiplied by 3 and add 1 
    else:
        n=3*n+1
#print current number out to show the process
        print(n)

        
        
        
        

       
            
    




# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 12:16:02 2020

@author: Dell
"""
#reference: the following codes was inspired by a classmate called Zezhen Lu
#reference: He remind me to define a function that calculate all the 5 possible operations between 2 numbers, the function is called 'Function'
#import libraries
import re
import sys
import copy
#'Aggregate_result'list  used to store the all the ultimate recursion result
Aggregate_Result = []
#input_nums list used to store input numbers
input_nums = []
#variable recursion_time used to count the recursion time
recursion_time = 0
#input numbers
input_numbers = input('''Please input numbers to compute 24:(use ',' to divide them):''')
#split input numbers by ','
nums = re.split(',', input_numbers)
#get out input numbers 
for item in nums:
    input_nums.append(float(item))#use float to guaranteen fraction calculation is possible
#define a function called 'Function ', which contains all possible 5 operations between 2 number
def Function(a,b,funtion):#using this fucntion, we take 5 kind of classified discussion,so the estimated the complexity at this step: O(5)
#define global variable
    global c,recursion_time
#use number 1~5 to represent the 5 operations
    if funtion == 1:
        c = a + b# add
    elif funtion == 2:
        c = a * b# multiply
    elif funtion == 3:# minus
        c = a - b# we do not consider whetehr the result is positive or negative beacause we can change the previous step' + or - to reach the same effect
                 # and eliminate one classified classification would outstandingly reduce the operation process
    elif funtion == 4:# divide
        #when dividing ,we deperate it into two parts to make it clearer
        if b == 0.0:
#if the denominator is 0, we would abandon the susequent process, which would lead to calculate all the meaningful recursion time
            c = 'stop'
        else:
            c = a/b
    elif funtion == 5:
        if a == 0.0:
            c = 'stop'
        else:
            c = b/a
#if any intermediate precess reahced 24, the funtion would break
    if c == 24.0:
        recursion_time += 1
        #print out the result
        print('Yes')
        print('Recursion times:',recursion_time)
        # end the function
        #reference：https://blog.csdn.net/tomorrowsummer/article/details/92843007
        sys.exit()
    else:
        return c
#define another function called 'Recursion' to do the recursive merging and calculating 
def Recursion(L):
#define global variable
    global c,recursion_time
#each turn we would check the length of the remaining list, if only one number eremained,add the ultimate one number into list
    if len(L) == 1:
        Aggregate_Result.append(L[0])
    else:
#method of exhaustion. We take every two possible numbers into account, but this may lead to repetition
        for i in range(0,len(L)-1):
          for j in range (i+1,len(L)):
            #make a copy of L called L_copy that would not change original L
            L_copy = copy.deepcopy(L)
#take two numbers out, merge them,delete the original numbers and put the merging result back
            A = L[i]
            B = L[j]
            L_copy.remove(A)
            L_copy.remove(B)
#try all the possible equation between two numbers
            for k in range(1,6):
                copyL_copy = copy.deepcopy(L_copy)
                #carried out +,-,*,/
                Result = Function(A,B,k)
#record the recursion time
                recursion_time += 1
#if the denominator is 0, we would abandon the susequent process, which would lead to calculate all the meaningful recursion time
                if not c == 'stop':
                 copyL_copy.append(Result)
#put the result list back into recursion until one number remained in the list
                 Recursion(copyL_copy)           
for n in range(len(nums)):
#check if the input number is a integer
    if float(nums[n]) - int(float(nums[n])) !=0:
        print('The input must be integer from 1 to 23')
        break
#check if the imput numbers is euqal to or smaller than 23 and equal to or larger than 1
    elif int(nums[n]) >= 24 or int(nums[n]) < 1:
#inform the user to input numbers between(equal to) 1 and 23
        print('The input must be integers from 1 to 23')
# if the input number is not between 1 and 23, break 
        break
else:
    #use recursion function defined before to get out all the possible result
    Recursion(input_nums)
    #check through the result list
    for i in range(len(Aggregate_Result)):
#check if we got 24 in our list which contains all the recursion result, if 24 existed,print 'yes'
        if Aggregate_Result[i] == 24:
            print('Yes')
            break
#if we cannot find 24, print'no'
    print('No')
    print('Recursion times:',recursion_time)
#Big O: [[(5/2)**n]*[(n-1)!)**2]]*n, n is the number of input numbers




# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:35:00 2020

@author: 蒋冰
"""
####半成品
import random
from random import shuffle
import fractions
from fractions import Fraction
Finish = False
n = 0
while not Finish:
    n += 1
    Finish = False
    L = [1,1,1,1]
    N = len(L)
    for i in range(N-1):
        M=random.sample(range(0,N),2)
        a = M[0]
        b = M[1]
        c = L[a]
        d = L[b]
        if d == 0:
            result1 = c + d
            result2 = c - d
            result3 = c * d
            op = [result1,result2,result3]
            e = random.choice(op)
        else:
            result1 = c + d
            result2 = c - d
            result3 = c * d
            result4 = Fraction(c,d)
            op = [result1,result2,result3,result4]
            e = random.choice(op)
        L.remove(c)
        L.remove(d)
        L.append(e)
        shuffle(L)
        N = N -1
    if L[0] == 24:
        print('yes')
        Finish = True
    elif n >= 1000000:
        print('no')
        break

    

    


    
    
    





        
        
    
    

    









            




            

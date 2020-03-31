# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 21:08:30 2020

@author: 蒋冰
"""
seq = str('ATGCGACTACGATCGAGGGCCAT')
re_seq = str()
l = len(seq)
l = l + 1
for i in range (1,l):
    if seq[-i] == 'T':
        re_seq += 'A'
    elif seq[-i] == 'A':
        re_seq += 'T'
    elif seq[-i] == 'C':
            re_seq += 'G'
    else: re_seq += 'C'
print(re_seq)

                
            
            
        

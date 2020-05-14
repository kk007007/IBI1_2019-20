# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 21:08:30 2020

@author: 蒋冰
"""
# input the template
seq = str('ATGCGACTACGATCGAGGGCCAT')
#re_seq stored the reverse complementary sequecen
re_seq = str()
# get the length of the template
l = len(seq)
l = l + 1
#go through all the nucleotide
for i in range (1,l):
# start from the end of the template
# do reverse complementary T->A,A->T,C->G,G->c
    if seq[-i] == 'T':
        re_seq += 'A'
    elif seq[-i] == 'A':
        re_seq += 'T'
    elif seq[-i] == 'C':
            re_seq += 'G'
    else: re_seq += 'C'
#print result
print(re_seq)

                
            
            
        

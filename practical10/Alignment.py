# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 20:24:02 2020

@author: 蒋冰
"""
import re
import os
import pandas as pd
os.chdir('D:\GitKraken\IBI1_2019-20\practical10')
MG= open('SOD2_mouse.fa')
HG= open('SOD2_human.fa')
RG= open('RandomSeq.fa')
BM= pd.read_csv("BLOSUM62 matrix.csv")
score= 0
#human-mouse
import re
MG1 = []
for line in MG:
        MG1 = re.findall(r'\w+',line)
MG2 = str(MG1)
MG3 = MG2[2:]
MG4 = MG3[:-2]

l1 = len(str(MG4))
HG1 = []
for line in HG:
    HG1 = re.findall(r'\w+',line)
HG2 = str(HG1)
HG3 = HG2[2:]
HG4 = HG3[:-2]
l2 = len(str(HG4))
seq1 = MG4
seq2 = HG4
lseq1 = len(seq1)
lseq2 = len(seq2)
print(lseq1)
edit_distance = 0 
if lseq1 >= lseq2:
    for i in range(len(seq1)):
        if seq1[i] == 'A':
            a = 0
        elif seq1[i] == 'R':
            a = 1
        elif seq1[i] == 'N':
            a =2
        elif seq1[i] == 'D':
            a =3
        elif seq1[i] == 'C':
            a =4
        elif seq1[i] == 'Q':
            a=5
        elif seq1[i] == 'E':
            a =6
        elif seq1[i] == 'G':
            a = 7
        elif seq1[i] == 'H':
            a = 8
        elif seq1[i] == 'I':
            a = 9
        elif seq1[i] == 'L':
            a = 10
        elif seq1[i] == 'K':
            a = 11
        elif seq1[i] == 'M':
            a = 12
        elif seq1[i] == 'F':
            a =13
        elif seq1[i] == 'P':
            a =14
        elif seq1[i] == 'S':
            a = 15
        elif seq1[i] == 'T':
            a = 16
        elif seq1[i] == 'W':
            a = 17
        elif seq1[i] == 'Y':
            a =18
        elif seq1[i] == 'V':
            a = 19
        elif seq1[i] == 'B':
            a = 20
        elif seq1[i] == 'Z':
            a = 21
        elif seq1[i] == 'X':
            a = 22
        score += BM.loc[a,seq2[i]]	
print(score)
print(edit_distance)

# human-random
import re
import os
import pandas as pd
os.chdir('D:\GitKraken\IBI1_2019-20\practical10')
MG= open('SOD2_mouse.fa')
HG= open('SOD2_human.fa')
RG= open('RandomSeq.fa')
BM= pd.read_csv("BLOSUM62 matrix.csv")
score= 0
HG1 = []
for line in HG:
    HG1 = re.findall(r'\w+',line)
HG2 = str(HG1)
HG3 = HG2[2:]
HG4 = HG3[:-2]
l2 = len(str(HG4))
seq1 = HG4

RG1=[]
for line in RG:
    RG1 = re.findall(r'\w+',line)
RG2 = str(RG1)
RG3 = RG2[2:]
RG4 = RG3[:-2]
seq3 = RG4
l3 = len(RG4)
edit_distance	=	0 
for	i in range(l3): 
    if	seq1[i]!=seq3[i]:
        edit_distance	+=	1   
print(edit_distance)   								

if lseq1 >= lseq2:
    for i in range(l3):
        if seq1[i] == 'A':
            a = 0
        elif seq1[i] == 'R':
            a = 1
        elif seq1[i] == 'N':
            a =2
        elif seq1[i] == 'D':
            a =3
        elif seq1[i] == 'C':
            a =4
        elif seq1[i] == 'Q':
            a=5
        elif seq1[i] == 'E':
            a =6
        elif seq1[i] == 'G':
            a = 7
        elif seq1[i] == 'H':
            a = 8
        elif seq1[i] == 'I':
            a = 9
        elif seq1[i] == 'L':
            a = 10
        elif seq1[i] == 'K':
            a = 11
        elif seq1[i] == 'M':
            a = 12
        elif seq1[i] == 'F':
            a =13
        elif seq1[i] == 'P':
            a =14
        elif seq1[i] == 'S':
            a = 15
        elif seq1[i] == 'T':
            a = 16
        elif seq1[i] == 'W':
            a = 17
        elif seq1[i] == 'Y':
            a =18
        elif seq1[i] == 'V':
            a = 19
        elif seq1[i] == 'B':
            a = 20
        elif seq1[i] == 'Z':
            a = 21
        elif seq1[i] == 'X':
            a = 22
        score += BM.loc[a,seq3[i]]	
print(score)

#mouse random
import re
import os
import pandas as pd
os.chdir('D:\GitKraken\IBI1_2019-20\practical10')
MG= open('SOD2_mouse.fa')
HG= open('SOD2_human.fa')
RG= open('RandomSeq.fa')
BM= pd.read_csv("BLOSUM62 matrix.csv")
score= 0
import re
MG1 = []
for line in MG:
        MG1 = re.findall(r'\w+',line)
MG2 = str(MG1)
MG3 = MG2[2:]
MG4 = MG3[:-2]
seq1 = MG4
l1 = len(str(MG4))

RG1=[]
for line in RG:
    RG1 = re.findall(r'\w+',line)
RG2 = str(RG1)
RG3 = RG2[2:]
RG4 = RG3[:-2]
seq3 = RG4
l3 = len(RG4)
score = 0
if l1 >= l3:
    for i in range(l3):
        if seq1[i] == 'A':
            a = 0
        elif seq1[i] == 'R':
            a = 1
        elif seq1[i] == 'N':
            a =2
        elif seq1[i] == 'D':
            a =3
        elif seq1[i] == 'C':
            a =4
        elif seq1[i] == 'Q':
            a=5
        elif seq1[i] == 'E':
            a =6
        elif seq1[i] == 'G':
            a = 7
        elif seq1[i] == 'H':
            a = 8
        elif seq1[i] == 'I':
            a = 9
        elif seq1[i] == 'L':
            a = 10
        elif seq1[i] == 'K':
            a = 11
        elif seq1[i] == 'M':
            a = 12
        elif seq1[i] == 'F':
            a =13
        elif seq1[i] == 'P':
            a =14
        elif seq1[i] == 'S':
            a = 15
        elif seq1[i] == 'T':
            a = 16
        elif seq1[i] == 'W':
            a = 17
        elif seq1[i] == 'Y':
            a =18
        elif seq1[i] == 'V':
            a = 19
        elif seq1[i] == 'B':
            a = 20
        elif seq1[i] == 'Z':
            a = 21
        elif seq1[i] == 'X':
            a = 22
        score += BM.loc[a,seq3[i]]	
print(score)

    









        

# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:08:06 2020

@author: 蒋冰
"""

redna = open('reversesequence.fa','w')
import re
gene=[]
seq = str()
genename=[]
z=str()
count = 0
re_seq = str()
x=[]
DNA = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
for line in DNA:
    if line.startswith('>'):
        if z != '':
            gene.append(z)
        sta = re.search(r'(gene):(\w+)',line)
        sta1 = sta.group(2)
        genename.append(sta1)
        z=''
        x.append(line)
        count += 1 
    else:
        line = line.rstrip()
        z += str(line)
gene.append(z)
xfile=open('mito_gene.fa','w')
for i in range(count):
    if ':Mito:' in x[i]:
        a = '\n' + '>' + genename[i] + '       ' + str(len(gene[i])) + '\n'
        seq = str(gene[i])
        l = len(seq)
        l = l +1
        for i in range(1,l):
            if seq[-i] == 'T':
                re_seq += 'A'
            elif seq[-i] == 'A':
                re_seq += 'T'
            elif seq[-i] == 'C':
                re_seq += 'G'
            else: re_seq += 'C'
        xfile.write(a)
        xfile.write(re_seq)
DNA.close
xfile.close
yfile = open('mito_gene.fa')
for line in yfile:
    print(line)
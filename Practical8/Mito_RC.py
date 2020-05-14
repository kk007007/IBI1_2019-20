# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:08:06 2020

@author: 蒋冰
"""
#Task3 is the combination of Task 1 and Task 2
#line 9~ 30 is the work of Task2, tries to get out gene name and gene sequence
import re
#creat list used to store gene and its gene name
gene=[]
seq = str()
genename=[]
z=str()
#variable 'count' was used to calculate the total gene numbers contained in the file
count = 0
re_seq = str()
x=[]
DNA = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
for line in DNA:
     #find the line that contain gene name and description
    if line.startswith('>'):
        if z != '':
            gene.append(z)
        #get out gene name and append it to list genename
        sta = re.search(r'(gene):(\w+)',line)
        sta1 = sta.group(2)
        genename.append(sta1)
        #clean the list for next gene sequence
        z=''
        x.append(line)
        count += 1 
     #add the gene sequence
    else:
        line = line.rstrip()
        z += str(line)
#add the result of the last run
gene.append(z)
#ask the user to input a filename as the new fasta file
file_name1 = input('please input a file name:')
file_name = file_name1 + str('.fa')
#open file
xfile=open(file_name,'w')
for i in range(count):
     # check if it is mitochondria chromosome
    if ':Mito:' in x[i]:
        #correspond genename and gene length
        a = '\n' + '>' + genename[i] + '       ' + str(len(gene[i])) + '\n'
        seq = str(gene[i])
        l = len(seq)
        l = l +1
        # do reverse complementary 
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
#print the file to check
yfile = open(file_name)
for line in yfile:
    print(line)
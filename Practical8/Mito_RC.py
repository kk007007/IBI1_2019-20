# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 14:08:06 2020

@author: 蒋冰
"""
#my spyder would get two differnet result, and randomly will generate a exit.fa  I think there's some mistakes with my spyder
#hope my code works well foe you
#Task3 is the combination of Task 1 and Task 2
#line 24~45 is the work of Task2, tries to get out gene name and gene sequence
#import library
import re
#creat list used to store gene and its gene name
gene=[] #store gene sequence
seq = str()# used to temporary store gene sequence  in line 45~63
genename=[]#used to store gene name
z=str()#used to store line in the file
#variable 'count' was used to calculate the total gene numbers contained in the file
count = 0
#variable re_seq used to store reverse sequence
re_seq = str()
x=[]# X list used to store lines that contains gene information 
#open file
DNA = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
for line in DNA:
     #find the line that contain gene name and description by checking '>' sign
    if line.startswith('>'):
        if z != '':
            gene.append(z)
        #get out gene name by finding signal 'gene:' and append it to list genename
        sta = re.search(r'(gene):(\w+)',line)
        #get out gene name 
        sta1 = sta.group(2)
        #add gene name into list 'genename'
        genename.append(sta1)
        #clean the list for next gene sequence
        z=''
        # add lines that contain gene description into X
        x.append(line)
        #add 1, indicates one more gene found
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
#open a new fasta file and modify it
xfile=open(file_name,'w')
for i in range(count):
     # check if it is mitochondria chromosome by finding '>' in line
    if ':Mito:' in x[i]:
        #correspond genename and gene length
        a = '\n' + '>' + genename[i] + '       ' + str(len(gene[i])) + '\n'
        #count the gene sequence length
        seq = str(gene[i])
        l = len(seq)
        l = l +1
        re_seq = str()
        # do reverse complementary 
        for i in range(1,l):
            if seq[-i] == 'T':
                re_seq += 'A'
            elif seq[-i] == 'A':
                re_seq += 'T'
            elif seq[-i] == 'C':
                re_seq += 'G'
            else: re_seq += 'C'
        xfile.write(a)# write gene name and gene length into new fasta file
        xfile.write(re_seq)#write reverse gene sequence into new fasta file
xfile.close#close new fasta file

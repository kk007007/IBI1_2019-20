# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 23:06:28 2020

@author: 蒋冰
"""
#reference: the method that first creating a list that stored the gene name, gene length and then check if it is mitochondria chromosome was inspired by a classmate called Jincheng Cheng
import re
#creat list used to store gene and its gene name
gene=[] #store gene sequence
genename=[]#used to store gene name
z=str()#used to store line in the file
#variable 'count' was used to calculate the total gene numbers contained in the file
count = 0
x=[]# X list used to store lines that contains gene information
#open the file
DNA = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
#line 18 ~30 tried to extract gene name and gene sequence into list
for line in DNA:
    #find the line that contain gene name and description
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
#create a new file called mito_gene
xfile=open('mito_gene.fa','w')
for i in range(count):
    # check if it is mitochondria chromosome
    if ':Mito:' in x[i]:
        #correspond genename and gene length
        a = '\n' + genename[i] + '    ' + str(len(gene[i])) + '\n'
        seq = gene[i]
        xfile.write(a) #write gene name and gene length into new fasta file
        xfile.write(seq)#write gene sequence into it
xfile.close#colse file
# print the mito_gene out to check
yfile = open('mito_gene.fa')
for line in yfile:
    print(line)
    
    
    
    
    
 

    



    
    



        
        
        
        
            
        
        
        
        


    
            
            
        
        
                
        
            
        
        
        


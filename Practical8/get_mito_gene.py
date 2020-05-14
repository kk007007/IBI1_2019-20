# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 23:06:28 2020

@author: 蒋冰
"""
#reference: the method that first creating a list that stored the gene name, gene length and then check if it is mitochondria chromosome was inspired by a classmate called Jincheng Cheng
import re
#creat list used to store gene and its gene name
gene=[]
genename=[]
z=str()
#variable 'count' was used to calculate the total gene numbers contained in the file
count = 0
x=[]
#open the file
DNA = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
#line 18 ~30 tried to extract gene name and gene sequence into list
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
#create a new file called mito_gene
xfile=open('mito_gene.fa','w')
for i in range(count):
    # check if it is mitochondria chromosome
    if ':Mito:' in x[i]:
        #correspond genename and gene length
        a = '\n' + genename[i] + '    ' + str(len(gene[i])) + '\n'
        seq = gene[i]
        xfile.write(a)
        xfile.write(seq)
DNA.close
xfile.close
# print the mito_gene out to check
yfile = open('mito_gene.fa')
for line in yfile:
    print(line)

    
    
    
    
    
 

    



    
    



        
        
        
        
            
        
        
        
        


    
            
            
        
        
                
        
            
        
        
        


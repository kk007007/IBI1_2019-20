# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 23:06:28 2020

@author: 蒋冰
"""

#intact     ################################################
import re
gene=[]
genename=[]
z=str()
count = 0
x=[]
DNA = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
for line in DNA:
    if line.startswith('>'):
        if z != '':
            gene.append(z)
        sta = re.findall(r'^>\w+',line)
        sta1 = str(sta)
        sta2 = sta1[3:8]
        genename.append(sta2)
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
        a = genename[i] + '       ' + str(len(gene[i])) + '\n'
        xfile.write(a)
DNA.close
xfile.close
yfile = open('mito_gene.fa')
for line in yfile:
    print(line)

    
    
    
    
    
 

    



    
    



        
        
        
        
            
        
        
        
        


    
            
            
        
        
                
        
            
        
        
        


# -*- coding: utf-8 -*-
"""
Created on Wed May 13 10:06:42 2020

@author: 蒋冰
"""
#The code i wrote need a long time to run, which may derived from the inferior recursion step 
#imort library
import xml.dom.minidom
import pandas as pd
#list1 stored various sublist which indicate different line in the excel
list1 = []
#index was used to document the row number
index = []
# variable 'count' used for storing the number of childnodes
count = 0
#get out all the descendants with the tag 'term'
DOMTree = xml.dom.minidom.parse('go_obo.xml')
collection = DOMTree.documentElement
GO = collection.getElementsByTagName("term")   
#the finding functon is used to findall the needed childnodes related to the input gene 'a'
def finding(a):  
    global id,id1,child,count
#the variable 'count' will add 1 everytime when the function is called, thus the total childnodes number will be count-1
    count += 1
    # c was used to store the element in is_a tag
    c={}
# go through all the descendants with tag 'term'
    for go in GO:
#line 30~32 used to check if the 'go' has the tag 'is_a'
        child = go.getElementsByTagName('is_a')
        b = child.length
        if b !=0:
            #if <is_a> tag existed, get out all the element in the is_a tag
            for j in range(b):
#get out the element in tag <is_a>
                child1 = go.getElementsByTagName('is_a')[j]
                c[j] = child1.childNodes[0].data
# if we can find the gene we input in the tag 'is_a' , than we do recursion until no more childnodes existed
                if c[j].find(a) != -1:
                    id = go.getElementsByTagName('id')[0]
                    id1 = id.childNodes[0].data
                    finding(id1)
# the reason for minus 1 mentioned in the line 24
    return(count-1)
i = 1
for go in GO:
#get out the element in tag <defstr>
    check = go.getElementsByTagName('defstr')[0]
    a = check.childNodes[0].data
#check if it is related to autophagosome
    if a.find('autophagosome') != -1:
        name = go.getElementsByTagName('name')[0]
        name1 = name.childNodes[0].data
#get out the id
        id = go.getElementsByTagName('id')[0]
        id2 = id.childNodes[0].data
        #clear the count value, important!!
        count = 0
        childnodes = finding(id2)
# form a list wichi contains id,name,definition and the number of childnodes
        b=[id2,name1,a,childnodes]
        #list 1 contains column content for excel
        list1.append(b)
        # index list used to document the row number ,add one each turn
        i += 1
        index.append(i)
#output as excel file
#use list 1 as the content for each column,use index list as the row number
#define column name as : id names definition and childnodes
df = pd.DataFrame(list1,index,columns=['id', 'names', 'definition','chilnodes'])
#export as excel
df.to_excel("GO task.xls")


    

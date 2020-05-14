# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:18:44 2020

@author: bluem
"""
#reference: blosum62 source get from https://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt
#reference：This practical was guided by Qi Liu
#import library
import re
import pandas as pd
#change directory to where the file exist
#ask user to input two file they want to compare 
file_name1=input("please input the first fasta file name:")
file_name2=input("please input the second fasta file name:")
#read the file and extract the sequence as strings
file1=open(file_name1).read()
file2=open(file_name2).read()
#convert the list to a string
#reference: taught by Qi Liu
seq1=''.join(re.findall(r">.+?\n([A-Z]+)",file1))
seq2=''.join(re.findall(r">.+?\n([A-Z]+)",file2))
#calculate the hamming distanceS
#set initial distance as zero
edit_distance=0 
#compare each amino acid
for i in range(len(seq1)): 
    if seq1[i]!=seq2[i]:
#add a score 1 if amino acids are different
        edit_distance+=1 
#print the result
print('the hamming distance of two sequence is ',edit_distance)
#read the "BLOSUM62 matrix.csv" 
blosum62=pd.read_csv("BLOSUM62 matrix.csv")
#blosum 62 was read into a dataframe, and the name of the amino acid is in the first column
#define a function to correspond the amin oacid name to the row number
#reference： the idea of creating a function to got the corresponding row number was inspired by Qi Liu
def find(place):
    j=0
    while True:
        #check each amino acid name one by one
        if blosum62.iloc[j,0]!=place:
            #add 1 until reached the wanted row number 
            j+=1
        if blosum62.iloc[j,0]==place:
            break
    return j
#variable score used to calculate blosum score
score=0
#variable alignment used to store blast-like alignment
alignment=''
for i in range(len(seq1)):
    #seperately get out the amino acid in two gene sequence
    place1=seq1[i]
    place2=seq2[i]
#use find function to get the corresponding amino acid row number
#get the score in blosum62 by giving x,y coordinates
    score_plus=blosum62.loc[find(place2),place1]
#acumulate the score
    score+=score_plus
#bonus part: print out blast-line alignment
    # if two amino acid was the same, alignment sign equal to the amino acid
    if place1==place2:
        alignment+=place1
    # if the two amino acid was different, use '+' to indicate conservative	substitutions witch the score is positive
    elif score_plus>=0:
        alignment+='+'
    else:
    # if the two amino acid was different, use ' ' to indicate unrelated substitution
        alignment+= " "  
#print out the result
print('the bolusum62 score is {}\n'.format(score))
#use format method to standarize the out. Reference：taught by Qi Liu
print("seq1:{}".format(seq1))
print("     {}".format(alignment))
print("seq2:{}".format(seq2))
    
    
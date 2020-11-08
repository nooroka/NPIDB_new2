#!/usr/bin/env python
# coding: utf-8

import sys

op = open("/home/nooroka/backupnores02102020/families/families_without_resfull2null.txt","r")

listresdomains = []
listdomains = []
liststructs = []
listresstructs = []
for line in op:
    line = line.strip()
    line = line.split("\t")
    if len(line) > 1:
        if str(line[1]) == sys.argv[1] and sys.argv[1] != ' ':
            line[3] = line[3].split()
            for i in range(len(line[3])):
                listdomains.append(line[3][i])              
            line[2] = line[2].split()
            for j in range(len(line[2])):
                liststructs.append(line[2][j])      
        if sys.argv[1] == ' ':
            las = ''
            if las in line:
                line[3] = line[3].split()
                for i in range(len(line[3])):
                    listdomains.append(line[3][i])
                line[2] = line[2].split()
                for j in range(len(line[2])):
                    liststructs.append(line[2][j])                     
        
                
                
 
op.close()

setdomains = set(listdomains)
setstructs = set(liststructs)


print(str(sys.argv[1])+"\t"+str(len(setdomains))+"\t"+str(len(setstructs)))

#print(str(sys.argv[1]))
#print("domains "+str(len(setdomains)))
#print("structs "+str(len(setstructs)))
#print("\n")
listdomains2 = []
listfamilies2 = []
'''
op2 = open("result_sqldatabasenew5corr.txt","r")
for line2 in op2:
    line2 = line2.strip()
    line2 = line2.split("\t")
    if len(line2) > 1: #не учитываем случаи, где пустой Interaction mode
        if str(line2[1]) == str(sys.argv[1]):
             op3 = open("structsend.txt", "r")
             for line3 in op3:
                 line3 = line3.strip()
                 line3 = line3.split("\t",1)
                 line3[1] = line3[1].strip()
                 if str(line2[0]) in str(line3[1]):
                     listdomains2.append(line3[0])
             op3.close()
             op4 = open("structsend23.txt", "r")
             for line4 in op4:
                 line4 = line4.strip()
                 line4 = line4.split("\t",1)
                 line4[1] = line4[1].strip()
                 if str(line2[0]) in str(line4[1]):
                     listfamilies2.append(line4[0])
             op4.close()      
print(listdomains2)
print(listfamilies2)
      
                     
print("domains_in_structs "+str(len(listdomains2)))
print("families_in_structs "+str(len(listfamilies2)))
              
'''

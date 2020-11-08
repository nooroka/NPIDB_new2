#!/usr/bin/env python
# coding: utf-8

import sys
import os

op = open("/home/nooroka/backupres02102020/families/families_without_resfull2null.txt","r")
listresdomains = []
listresstructs = []
f = open("/home/nooroka/backupres02102020/res/listresstructs.txt","r")#отбираем хиты с подходящим разрешением
listres = [line.rstrip() for line in f]
f.close()
#print(listres) печатает
f = open("/home/nooroka/backupres02102020/res/listresdomains.txt","r")#отбираем хиты с подходящим разрешением
listresd = [line2.rstrip() for line2 in f]
f.close()
for line in op:
    line = line.strip()
    line = line.split("\t")
    if len(line) > 1:
        if str(line[1]) == sys.argv[1] and sys.argv[1] != ' ':
            line[3] = line[3].split()
            for i in range(len(line[3])):
                if line[3][i] in listresd:
                    listresdomains.append(line[3][i])
            line[2] = line[2].split()
           # print(line[2]) #печатает все
            for j in range(len(line[2])):
                if line[2][j] in listres:
                    listresstructs.append(line[2][j])
        if sys.argv[1] == ' ':
            las = ''
            if las in line:
                line[3] = line[3].split()
                for i in range(len(line[3])):
                    if line[3][i] in listresd:
                        listresdomains.append(line[3][i])
                line[2] = line[2].split()
                for j in range(len(line[2])):    
                   if line[2][j] in listres:                   
                        listresstructs.append(line[2][j])
        
                
                
  
op.close()


setresstructs = set(listresstructs)
setresdomains = set(listresdomains)

#print(setdomains)
#print(setstructs)
#print(listresstructs)
#print(str(sys.argv[1]))

#print("domainsres "+str(len(setresdomains)))
#print("structsres "+str(len(setresstructs)))
#NULL не считается, поскольку в sys.argv[1] нет
print(str(sys.argv[1])+"\t"+str(len(setresdomains))+"\t"+str(len(setresstructs)))

#print(listresstructs)
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

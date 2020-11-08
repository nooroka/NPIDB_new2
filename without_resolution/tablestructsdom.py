#!/usr/bin/env python
# coding: utf-8

import sys

op = open("/home/nooroka/backupnores02102020/uniprot/domains_without_resfull2.txt","r")

listdomains = []
liststructs = []

for line in op:
    line = line.strip()
    line = line.split("\t")
    if len(line) > 1:
        if str(line[1]) == sys.argv[1] and sys.argv[1] != ' ':
            line[0] = line[0].split()
            for i in range(len(line[0])):
                listdomains.append(line[0][i])              
            line[2] = line[2].split()
            for j in range(len(line[2])):
                liststructs.append(line[2][j])      
        if sys.argv[1] == ' ':
            las = ''
            if las in line:
                line[0] = line[0].split()
                for i in range(len(line[0])):
                    listdomains.append(line[0][i])
                line[2] = line[2].split()
                for j in range(len(line[2])):
                    liststructs.append(line[2][j])                     
        
           
                
 
op.close()

setdomains = set(listdomains)
setstructs = set(liststructs)

listfamilies = []

#print(str(sys.argv[1]))
#print("domains "+str(len(setdomains)))
#print("structs "+str(len(setstructs)))
#print("\n")
op3 = open("/home/nooroka/backupnores02102020/families/families_without_resfull2.txt","r")
for line3 in op3:
    line3 = line3.strip()
    line3 = line3.split("\t")
    endc = line3[-1].split()
    for item in range(len(endc)):
        if str(endc[item]) in setdomains:
           listfamilies.append(str(line3[0]))

setfamilies = set(listfamilies)
#print("families "+str(len(setfamilies)))
#print("\n")
print(str(sys.argv[1])+"\t"+str(len(setdomains))+"\t"+str(len(setstructs))+"\t"+str(len(setfamilies)))

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


print(str(sys.argv[1])+"\t"+str(len(setresdomains))+"\t"+str(len(setresstructs)))


listdomains2 = []
listfamilies2 = []


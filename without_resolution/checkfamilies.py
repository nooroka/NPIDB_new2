#!/usr/bin/env python
#coding: utf-8
#таблица соответствия uniprot id pfam и Interaction mode
import os
import sys
import subprocess
from collections import OrderedDict
listpfamid = []
listinteraction = []
fileuni = open("/home/nooroka/backupnores02102020/b_pfam_struct_types2.txt", "r")
file2 = open("/home/nooroka/backupnores02102020/pfamcheck4.txt","w")
file4 = open("/home/nooroka/backupnores02102020/interaction_mode_families.txt","w")
list1 = []
list2 = []
file5 = open("/home/nooroka/backupnores02102020/interaction_mode_uncorr.txt","w")

countint = 0
for line in fileuni:
    if "INSERT INTO `b_pfam_struct_types` VALUES" in line: 
        line = line.split()
        lineintmode = line[4].split(",")
        if len(lineintmode) == 14:
            countint+=1
        listpfamid.append(str(lineintmode[5]))
        listinteraction.append(str(lineintmode[6]))
        lineintmode[1] = lineintmode[1].split(".")
        #print(lineintmode[1])
        if len(lineintmode[1]) == 3: #обычные файлы
            file2.write(str(lineintmode[1][0][1:])+"."+str(lineintmode[2][1:-1])+"_"+str(lineintmode[3])+"-"+str(lineintmode[4])+"."+str(lineintmode[1][0][1:])+"."+str(lineintmode[1][1])+"."+str(lineintmode[1][2][:-1])+"\n")
            a1 = str(lineintmode[1][0][1:])+"."+str(lineintmode[2][1:-1])+"_"+str(lineintmode[3])+"-"+str(lineintmode[4])+"."+str(lineintmode[1][0][1:])+"."+str(lineintmode[1][1])+"."+str(lineintmode[1][2][:-1])+"\n" #разбиваем по точке, потом соединяем из [1] - трехточечный идентификатор из pdb
            list1.append(a1.strip())
            os.chdir("/home/npidb/data/pdb_new/dna")          
            if os.path.exists("pdb{}.pdb".format(lineintmode[1][0][1:])): 
                file4.write(str(a1.strip())+" "+str(lineintmode[9][1:-1])+"_"+str(lineintmode[12])+"-"+str(lineintmode[13][:-2])+" "+str(lineintmode[5][1:-1])+"\n")
                file5.write(str(a1.strip())+" "+str(lineintmode[6])[1:-1]+"\n")
             

        elif len(lineintmode[1]) == 2:#учитываем pdb
            file2.write(str(lineintmode[0][2:-1])+"."+str(lineintmode[2][1:-1])+"_"+str(lineintmode[3])+"-"+str(lineintmode[4])+"."+str(lineintmode[1][0][1:])+"."+str(lineintmode[1][1][:-1])+"\n")
            a2 = str(lineintmode[0][2:-1])+"."+str(lineintmode[2][1:-1])+"_"+str(lineintmode[3])+"-"+str(lineintmode[4])+"."+str(lineintmode[1][0][1:])+"."+str(lineintmode[1][1][:-1])+"\n"
            list1.append(a2.strip())
            os.chdir("/home/npidb/data/pdb_new/dna")       
            if os.path.exists("pdb{}.pdb".format(lineintmode[0][2:-1])): 
                file4.write(str(a2.strip())+" "+str(lineintmode[9][1:-1])+"_"+str(lineintmode[12])+"-"+str(lineintmode[13][:-2])+" "+str(lineintmode[5][1:-1])+"\n")
                file5.write(str(a2.strip())+" "+str(lineintmode[6][1:-1])+"\n")
            #пишем файл и юнипрот во второй колонке
os.chdir("/home/npidb/data/pdb_new/pfam")
'''
for l in os.listdir("."):
    file3.write(str(l)+"\n")
    list2.append(l)  
'''


    

fileuni.close()


file2.close()

file4.close()
file5.close()

os.chdir("/home/nooroka/backupnores02102020/scripts")
'''
file6 = open("interaction_mode_uncorr.txt","r")
file7 = open("interaction_mode_uncorr2.txt","w")
for line in file6:
    line = line.replace("|"," ")
    file7.write(str(line))
file6.close()
file7.close()
'''
print("countint "+str(countint))

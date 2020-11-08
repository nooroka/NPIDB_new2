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
file4 = open("/home/nooroka/backupnores02102020/interaction_mode_uniprot6.txt","w")
list1 = []
list2 = []
file5 = open("/home/nooroka/backupnores02102020/interaction_mode_uncorr.txt","w")
file6 = open("/home/nooroka/backupnores02102020/interaction_mode_domain_uncorr.txt","w")
file7 = open("/home/nooroka/backupnores02102020/interaction_mode_family_uncorr.txt","w")


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
        if len(lineintmode[1]) == 3: #обычные файлы            
            file2.write(str(lineintmode[1][0][1:])+"."+str(lineintmode[2][1:-1])+"_"+str(lineintmode[3])+"-"+str(lineintmode[4])+"."+str(lineintmode[1][0][1:])+"."+str(lineintmode[1][1])+"."+str(lineintmode[1][2][:-1])+"\n")
            a1 = str(lineintmode[1][0][1:])+"."+str(lineintmode[2][1:-1])+"_"+str(lineintmode[3])+"-"+str(lineintmode[4])+"."+str(lineintmode[1][0][1:])+"."+str(lineintmode[1][1])+"."+str(lineintmode[1][2][:-1])+"\n"
            list1.append(a1.strip())
            file4.write(str(a1.strip())+" "+str(lineintmode[9][1:-1])+"_"+str(lineintmode[12])+"-"+str(lineintmode[13][:-2])+" "+str(lineintmode[5])[1:-1]+"\n")
            file5.write(str(a1.strip())+" "+str(lineintmode[6])[1:-1]+"\n")
            os.chdir("/home/npidb/data/pdb_new/dna")          
            if os.path.exists("pdb{}.pdb".format(lineintmode[1][0][1:])): 
               os.chdir("/home/nooroka/backupnores02102020/scripts")
               file6.write(str(lineintmode[9][1:-1])+"_"+str(lineintmode[12])+"-"+str(lineintmode[13][:-2])+" "+str(lineintmode[6])[1:-1]+"\n")
               file7.write(str(lineintmode[5][1:-1])+" "+str(lineintmode[6])[1:-1]+"\n")

               
        elif len(lineintmode[1]) == 2:#учитываем pdb
         #   print(lineintmode[1])
            file2.write(str(lineintmode[0][2:-1])+"."+str(lineintmode[2][1:-1])+"_"+str(lineintmode[3])+"-"+str(lineintmode[4])+"."+str(lineintmode[1][0][1:])+"."+str(lineintmode[1][1][:-1])+"\n")
            a2 = str(lineintmode[0][2:-1])+"."+str(lineintmode[2][1:-1])+"_"+str(lineintmode[3])+"-"+str(lineintmode[4])+"."+str(lineintmode[1][0][1:])+"."+str(lineintmode[1][1][:-1])+"\n"
            list1.append(a2.strip())
            file4.write(str(a2.strip())+" "+str(lineintmode[9][1:-1])+"_"+str(lineintmode[12])+"-"+str(lineintmode[13][:-2])+" "+str(lineintmode[5])[1:-1]+"\n")
            file5.write(str(a2.strip())+" "+str(lineintmode[6][1:-1])+"\n")
            os.chdir("/home/npidb/data/pdb_new/dna")          
            if os.path.exists("pdb{}.pdb".format(lineintmode[0][2:-1])): 
               os.chdir("/home/nooroka/backupnores02102020/scripts")
               file6.write(str(lineintmode[9][1:-1])+"_"+str(lineintmode[12])+"-"+str(lineintmode[13][:-2])+" "+str(lineintmode[6])[1:-1]+"\n")
               file7.write(str(lineintmode[5][1:-1])+" "+str(lineintmode[6])[1:-1]+"\n")

            #пишем файл и юнипрот во второй колонке
os.chdir("/home/npidb/data/pdb_new/pfam")
'''
for l in os.listdir("."):
    file3.write(str(l)+"\n")
    list2.append(l)  

result2 = list(set(sorted(list1)) - set(sorted(list2)))#таблица, где не совпадет с pstart pend
result22 = sorted(result2)
'''
print("countint " + str(countint))
fileuni.close()

file2.close()

file4.close()
file5.close()
file6.close()
file7.close()
os.chdir("/home/nooroka/backupnores02102020/scripts")



#!/usr/bin/env python
#coding: utf-8
#таблица соответствия uniprot id pfam и Interaction mode
import os
import sys
import subprocess
from collections import OrderedDict
listpfamid = []
listinteraction = []
file1 = open("uniprot.txt", "a")
filedomain = open("b_pfam_struct_types","w")
fileuni = open("b_pfam_struct_types2.txt", "r")
pdbmap = open("pdbmap", "r")
file2 = open("pfamcheck4.txt","w")
file3 = open("pfamlistdir.txt","w")
file4 = open("interaction_mode_uniprot6.txt","w")
list1 = []
list2 = []
file5 = open("interaction_mode_uncorr.txt","w")
file6 = open("interaction_mode_domain_uncorr.txt","w")
file7 = open("interaction_mode_family_uncorr.txt","w")
#file6 = open("int_mode_compare.txt","w")
#можно отсюда выкачать uniprot id
#lineintmode[3], lineintmode[4] - это координаты pstart, pend
text0 = pdbmap.readlines()

for line in fileuni:
    if "INSERT INTO `b_pfam_struct_types` VALUES" in line:
        line = line.split()
        lineintmode = line[4].split(",")
        filedomain.write(str(lineintmode[5])+"\t") #печатаем id-шник pfam и записываем в список listpfamid. цифры, чтобы убрать кавычки
        listpfamid.append(str(lineintmode[5]))
        listinteraction.append(str(lineintmode[6]))
        lineintmode[1] = lineintmode[1].split(".")
        if len(lineintmode[1]) == 3: #обычные файлы
            file1.write(str(lineintmode[1][0][1:])+"\t"+str(lineintmode[2])[1:-1]+"\t"+str(lineintmode[9][1:-1])+"\t"+str(lineintmode[6][1:-1])+"\n")#тут цепь и idшник, и сам uniprot (9) и interaction mode (6)
            file2.write(str(lineintmode[1][0][1:])+"."+str(lineintmode[2][1:-1])+"_"+str(lineintmode[3])+"-"+str(lineintmode[4])+"."+str(lineintmode[1][0][1:])+"."+str(lineintmode[1][1])+"."+str(lineintmode[1][2][:-1])+"\n")
            a1 = str(lineintmode[1][0][1:])+"."+str(lineintmode[2][1:-1])+"_"+str(lineintmode[3])+"-"+str(lineintmode[4])+"."+str(lineintmode[1][0][1:])+"."+str(lineintmode[1][1])+"."+str(lineintmode[1][2][:-1])+"\n"
            #file4.write(str(a1.strip())+" "+str(lineintmode[6][1:-1])+str(lineintmode[9][1:-1])+"\n") #interaction_mode для pstart/pend
            list1.append(a1.strip())
            #print(lineintmode[1][0][1:])
            file4.write(str(a1.strip())+" "+str(lineintmode[9][1:-1])+"_"+str(lineintmode[10])+"-"+str(lineintmode[11])+" "+str(lineintmode[9][1:-1])+"_"+str(lineintmode[3])+"-"+str(lineintmode[4])+"\n")
            file5.write(str(a1.strip())+" "+str(lineintmode[6])[1:-1]+"\n")
            os.chdir("/home/npidb/data/pdb_new/dna/")          
            if os.path.exists("pdb{}.pdb".format(lineintmode[1][0][1:])): 
               os.chdir("/home/nooroka")
               file6.write(str(lineintmode[9][1:-1])+"_"+str(lineintmode[10])+"-"+str(lineintmode[11])+" "+str(lineintmode[6])[1:-1]+"\n")
               file7.write(str(lineintmode[5][1:-1])+" "+str(lineintmode[6])[1:-1]+"\n")

               
        elif len(lineintmode[1]) == 2:#учитываем pdb
            print(lineintmode[1])
            file2.write(str(lineintmode[0][2:-1])+"."+str(lineintmode[2][1:-1])+"_"+str(lineintmode[3])+"-"+str(lineintmode[4])+"."+str(lineintmode[1][0][1:])+"."+str(lineintmode[1][1][:-1])+"\n")
            a2 = str(lineintmode[0][2:-1])+"."+str(lineintmode[2][1:-1])+"_"+str(lineintmode[3])+"-"+str(lineintmode[4])+"."+str(lineintmode[1][0][1:])+"."+str(lineintmode[1][1][:-1])+"\n"
            list1.append(a2.strip())
            #file4.write(str(a2.strip())+" "+str(lineintmode[6][1:-1])+str(lineintmode[9][1:-1])+"\n") #interaction_mode для pstart/pend
            file4.write(str(a2.strip())+" "+str(lineintmode[9][1:-1])+"_"+str(lineintmode[10])+"-"+str(lineintmode[11])+" "+str(lineintmode[9][1:-1])+"_"+str(lineintmode[3])+"-"+str(lineintmode[4])+"\n")
            file5.write(str(a2.strip())+" "+str(lineintmode[6][1:-1])+"\n")
            #print(lineintmode[0][2:-1])
            os.chdir("/home/npidb/data/pdb_new/dna/")          
            if os.path.exists("pdb{}.pdb".format(lineintmode[0][2:-1])): 
               os.chdir("/home/nooroka")
               file6.write(str(lineintmode[9][1:-1])+"_"+str(lineintmode[10])+"-"+str(lineintmode[11])+" "+str(lineintmode[6])[1:-1]+"\n")
               file7.write(str(lineintmode[5][1:-1])+" "+str(lineintmode[6])[1:-1]+"\n")

            #пишем файл и юнипрот во второй колонке
os.chdir("/home/npidb/data/pdb_new/pfam/")
for l in os.listdir("."):
    file3.write(str(l)+"\n")
    list2.append(l)  
#result = list(set(sorted(list1)) & set(sorted(list2)))
result2 = list(set(sorted(list1)) - set(sorted(list2)))#таблица, где не совпадет с pstart pend
result22 = sorted(result2)
#print(result22)
writepend = open("/home/nooroka/writepend1.txt","w")
for k in range(len(result22)):
    writepend.write(str(result22[k]))
    
writepend.close()
#print(result)
#print("result "+str(sorted(result)))
#print(list2)
#print(list1)
#print("len(list1) "+str(len(list1)))
#print("len(list2) "+str(len(list2)))
#print("len(result) "+str(len(result)))
fileuni.close()
filedomain.close()
file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()
os.chdir("/home/nooroka/")
'''
file6 = open("interaction_mode_uncorr.txt","r")
file7 = open("interaction_mode_uncorr2.txt","w")
for line in file6:
    line = line.replace("|"," ")
    file7.write(str(line))
file6.close()
file7.close()
'''

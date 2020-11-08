#!/usr/bin/env python
#coding: utf-8
#таблица соответствия uniprot id pfam и Interaction mode
import os
import sys
import subprocess
from collections import OrderedDict
listpfamid = []
listinteraction = []
#file1 = open("uniprot.txt", "a")
fileuni = open("/home/nooroka/backupres02102020/b_pfam_struct_types2.txt", "r")
file2 = open("/home/nooroka/backupres02102020/pfamcheck4.txt","w")
#file3 = open("pfamlistdir.txt","w")
file4 = open("/home/nooroka/backupres02102020/interaction_mode_families.txt","w")
list1 = []
list2 = []
f = open("/home/nooroka/backupres02102020/res/listresdomains_sorted.txt","r")#отбираем хиты с подходящим разрешением
listres = [line.rstrip() for line in f]
f.close()
file5 = open("/home/nooroka/backupres02102020/interaction_mode_uncorr.txt","w")
#lineintmode[3], lineintmode[4] - это координаты pstart, pend

set1 = set()
for line in fileuni:
    if "INSERT INTO `b_pfam_struct_types` VALUES" in line:
        line = line.split()
        lineintmode = line[4].split(",")
        listpfamid.append(str(lineintmode[5]))
        listinteraction.append(str(lineintmode[6]))
        lineintmode[1] = lineintmode[1].split(".")
        if len(lineintmode[1]) == 3: #обычные файлы           
            file2.write(str(lineintmode[1][0][1:])+"."+str(lineintmode[2][1:-1])+"_"+str(lineintmode[3])+"-"+str(lineintmode[4])+"."+str(lineintmode[1][0][1:])+"."+str(lineintmode[1][1])+"."+str(lineintmode[1][2][:-1])+"\n")
            a1 = str(lineintmode[1][0][1:])+"."+str(lineintmode[2][1:-1])+"_"+str(lineintmode[3])+"-"+str(lineintmode[4])+"."+str(lineintmode[1][0][1:])+"."+str(lineintmode[1][1])+"."+str(lineintmode[1][2][:-1])+"\n" #разбиваем по точке, потом соединяем из [1] - трехточечный идентификатор из pdb
            list1.append(a1.strip())
            os.chdir("/home/npidb/data/pdb_new/dna")
            if os.path.exists("pdb{}.pdb".format(lineintmode[1][0][1:])):
                os.chdir("/home/nooroka/backupres02102020/scripts")
                if (str(lineintmode[9][1:-1])+"_"+str(lineintmode[12])+"-"+str(lineintmode[13][:-2])) in listres:
                    file4.write(str(a1.strip())+" "+str(lineintmode[9][1:-1])+"_"+str(lineintmode[12])+"-"+str(lineintmode[13][:-2])+" "+str(lineintmode[5][1:-1])+"\n")
                    file5.write(str(a1.strip())+" "+str(lineintmode[6])[1:-1]+"\n")
                    set1.add(lineintmode[5][1:-1])
        elif len(lineintmode[1]) == 2:#учитываем pdb
            file2.write(str(lineintmode[0][2:-1])+"."+str(lineintmode[2][1:-1])+"_"+str(lineintmode[3])+"-"+str(lineintmode[4])+"."+str(lineintmode[1][0][1:])+"."+str(lineintmode[1][1][:-1])+"\n")
            a2 = str(lineintmode[0][2:-1])+"."+str(lineintmode[2][1:-1])+"_"+str(lineintmode[3])+"-"+str(lineintmode[4])+"."+str(lineintmode[1][0][1:])+"."+str(lineintmode[1][1][:-1])+"\n"
            list1.append(a2.strip())
            os.chdir("/home/npidb/data/pdb_new/dna")
            if os.path.exists("pdb{}.pdb".format(lineintmode[0][2:-1])):
                os.chdir("/home/nooroka/backupres02102020/scripts")
                if (str(lineintmode[9][1:-1])+"_"+str(lineintmode[12])+"-"+str(lineintmode[13][:-2])) in listres:
                    file4.write(str(a2.strip())+" "+str(lineintmode[9][1:-1])+"_"+str(lineintmode[12])+"-"+str(lineintmode[13][:-2])+" "+str(lineintmode[5][1:-1])+"\n")
                    file5.write(str(a2.strip())+" "+str(lineintmode[6][1:-1])+"\n")
                    set1.add(lineintmode[5][1:-1])

wf = open("/home/nooroka/backupres02102020/res/listfamilies.txt","w")
for i in set1:
    wf.write(str(i) + "\n")
wf.close()

                
os.chdir("/home/npidb/data/pdb_new/dna")
#for l in os.listdir("."):
 #   file3.write(str(l)+"\n")
  #  list2.append(l)  

fileuni.close()
file2.close()
#file3.close()
file4.close()
file5.close()

os.chdir("/home/nooroka/backupres02102020/scripts")


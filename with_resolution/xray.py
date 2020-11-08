#!/usr/bin/env python
#coding: utf-8
import os
op = open("/home/nooroka/backupres02102020/pdb_information.txt","r")
w = open("/home/nooroka/backupres02102020/res/resnmr.txt","w")
w2 = open("/home/nooroka/backupres02102020/res/resnmr_sorted.txt","w")

for line in op:
    if "INSERT INTO `pdb_information` VALUES" in line:
       line = line.strip()
       line = line.split("','") #такой разделитель потому, что нужно, чтобы  попал метод разрешения обязательно
       line[0] = line[0].split()
       line2 = line[0][4]
       pdb = line2[2:] #pdb-идентификатор
       print(str(pdb)+" "+str(len(line)))
       os.chdir("/home/npidb/data/pdb_new/dna")
       if os.path.exists("pdb{}.pdb".format(line2[2:])):
            os.chdir("/home/nooroka/backupres02102020/scripts")
            liner = line[3].split("'")
            w.write(str(pdb)+"\t"+str(liner[0])+"\n")
            
op.close()
w.close()
r22 = []
r2 = open("/home/nooroka/backupres02102020/res/resnmr.txt").readlines()
for line2222 in r2:
    line2222 = line2222.strip()
    line2222 = line2222.split()
    r22.append(line2222)

a2 = sorted(r22, key=lambda student: student[0])
for item2 in a2:
    w2.write(' '.join(map(str,item2))+"\n")
w2.close()


       

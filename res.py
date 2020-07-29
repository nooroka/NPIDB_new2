#!/usr/bin/env python
# coding: utf-8
import os
from collections import defaultdict
w = open("reschern.txt","w")
res1 = open("structsres.txt","r")
res2 = open("structsres2.txt","w")
for line in res1:
     line = line.split("\t")
     line[2] = line[2].strip()
     linek = line[2].split(" ")
     dict1 = defaultdict(list)
     for i in range(len(linek)):
         linekdot = linek[i].split(".")
         os.chdir("/home/npidb/data/pdb_new/dna/")
         op = open("pdb{}.pdb".format(linekdot[0]),"r")
         for line2 in op:
             if "REMARK" in line2 and "2" in line2 and "RESOLUTION." in line2:
                 line2 = line2.strip()
                 line2 = line2.split()
                 if "NOT" not in line2:
                     key,value = line2[3],linek[i]
                  #   print(str(key)+" "+str(value))
                     #value2 = 2 #дополнительное значение
                     dict1[key].append(value)
                     #dict1[key].append(value2)#ура, несколько значений
                     #dict1[line2[3]] = linek[i] 
                     #dict1[line2[3]] = 2 #новое значение присваивается
                 else:
                     key,value = line2[3], " "
                     dict1[key].append(value)
                 #w.write(str("pdb{}.pdb".format(linekdot[0]))+" "+str(line2[3])+"\n")
         os.chdir("/home/nooroka/")
     res2.write(str(line[0])+"\t"+str(dict1)+"\n")
     #print(str(linek)+"\t"+str(dict1))
     w.write(str(line[0])+"\t"+str(line[1])+"\t"+str(min(dict1))+"\n")#есть пустой словарь, на нем все останавливается
res1.close()   
w.close()
res2.close()
     

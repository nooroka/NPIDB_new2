#!/usr/bin/env python
# coding: utf-8

import os
import subprocess
from collections import defaultdict
dict1 = defaultdict(list)
op = open("/home/nooroka/backupnores02102020/interaction_mode_domain_uncorr.txt","r")
op3 = open("/home/nooroka/backupnores02102020/interaction_mode_domain_corr.txt","w")
list1 = []
list2 = []
dict2 = {}
for line in op: 
    line = line.replace("|"," ")
    line = line.strip()
    line = line.split(" ",1)
    if len(line) > 1:
            line[1] = line[1].split()
            line[1] = sorted(line[1])            
            key,value = line[0],line[1]
            dict1[key].extend(value)
    else:
            key,value = line[0]," "
            dict1[key].extend(value)          
for key2 in dict1:
    dict1[key2] = set(dict1[key2])

listkeys = dict1.keys()
#print(listkeys)
#listkeys = sorted(listkeys)

for key3 in listkeys:    
    op3.write(str(key3)+"\t"+' '.join(map(str,sorted(list(dict1[key3]))))+"\n")
op.close()
op3.close()
process3 = subprocess.Popen(["sort", "-k1", "/home/nooroka/backupnores02102020/interaction_mode_domain_corr.txt"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
data3,data33 = process3.communicate()
with open("/home/nooroka/backupnores02102020/interaction_mode_domain_corr2.txt", 'w') as f:
    f.write(data3)

#process4 = subprocess.Popen(["sort","-k1", "familiesendcorr.txt"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
#data4,data44 = process4.communicate()
#with open('familiesendcorr2.txt', 'w') as f2:
 #   f2.write(data4)


list3 = []
list4 = []
op2 = open("/home/nooroka/backupnores02102020/interaction_mode_domain_corr2.txt","r")
for line2 in op2:
    line2 = line2.strip()
    line2  = line2.split("\t",1)
    list2.append(line2[0])
    if len(line2) > 1:
        line2[1] = line2[1].split()
        list4.append(sorted(line2[1]))
    else:
        list4.append("NULL")
op2.close()
op4 = open("/home/nooroka/backupnores02102020/uniprot/familiesend_red.txt","r")
for line4 in op4:
    line4 = line4.strip()
    line4 = line4.split("\t",1)
    list1.append(line4[0])
    if len(line4) > 1:
        line4[1] = line4[1].split()
        list3.append(sorted(line4[1]))
    else:
        list3.append("NULL")
op4.close()
countok = 0
countno = 0
countok2 = 0
countno2 = 0
cnf = open("/home/nooroka/backupnores02102020/countnofile.txt","w")
for i in range(len(list2)):
    if list1[i] == list2[i]:
        countok+=1
    else:
        countno+=1
        print(str(list1[i])+"\t"+str(list2[i]))
for j in range(len(list4)):
    if list4[j] == list3[j]:
        countok2+=1
    else:
        countno2+=1
        cnf.write(str(list1[j])+"\t"+str(list3[j])+"\t"+str(list2[j])+"\t"+str(list4[j])+"\n")
cnf.close()
print("countok "+str(countok))
print("countno "+str(countno)) 
print("countok2 "+str(countok2)) 
print("countno2 "+str(countno2))


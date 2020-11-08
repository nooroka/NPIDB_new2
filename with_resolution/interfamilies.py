#!/usr/bin/env python
# coding: utf-8

import os
import subprocess
from collections import defaultdict
dict1 = defaultdict(list)
f = open("listfamilies.txt","r")#отбираем хиты с подходящим разрешением
listres = [line.rstrip() for line in f]
f.close()
op = open("b_pfam_family_types4.txt","r")
op3 = open("interaction_mode_family_corr.txt","w")
list1 = []
list2 = []
dict2 = {}
for line in op: 
    if "INSERT INTO" in line:
        if len(line) > 1:
            line = line.strip()
            line = line.split(" ")
            line11 = line[4].split(",")
            line11[1] = line11[1].replace("|"," ")
            op5 = open("structsend23.txt", "r")
            for line22 in op5:
                line22 = line22.strip()
                line22 = line22.split()
                if str(line11[0][2:-1]) in line22[0] and str(line11[0][2:-1]) in listres:
                    if "NULL" not in line11[1]:
                        key,value = str(line11[0][2:-1]),str(line11[1][2:-2])
                        dict1[key].append(value)
                    else:
                        key, value = str(line11[0][2:-1])," "
                        dict1[key].append(value)




listkeys = dict1.keys()
#print(listkeys)
#listkeys = sorted(listkeys)


op9 = open("familiesend.txt","r")
op10 = open("familiesend_red.txt","w")
for line15 in op9:
    line15 = line15.replace("'","")
    line15 = line15.replace("]","")
    line15 = line15.replace("[","")
    line15 = line15.replace(",","")
    op10.write(str(line15))
op9.close()
op10.close()



for key3 in listkeys:  
    op3.write(str(key3)+"\t"+' '.join(map(str,sorted(list(dict1[key3]))))+"\n")
op.close()
op3.close()
process3 = subprocess.Popen(["sort", "-k1", "interaction_mode_family_corr.txt"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
data3,data33 = process3.communicate()
with open('interaction_mode_family_corr2.txt', 'w') as f1:
    f1.write(data3)
#process4 = subprocess.Popen(["sort", "-k1"," dictinter5.txt"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
#data4,data44 = process4.communicate()
#with open('f.txt', 'w') as f2:
#    f2.write(data4)

#subprocess.call("sort -k1  interaction_mode_family_corr.txt > interaction_mode_family_corr2.txt",shell = True)
#print(dict1)
subprocess.call("sort -k1 dictinter5.txt > uniprot6corr2.txt", shell = True)
list3 = []
list4 = []
op2 = open("interaction_mode_family_corr2.txt","r")
for line2 in op2:
    line2 = line2.strip()
    line2  = line2.split("\t",1)
    if str(line2[0]) in listres:
       list2.append(line2[0])
       if len(line2) > 1:
           line2[1] = line2[1].split()
           list4.append(sorted(line2[1]))
       else:
           list4.append("NULL")
op2.close()
op4 = open("uniprot6corr2.txt","r") 
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
print(len(list1))
print(len(list2))
cnf = open("countnofile.txt","w")
for i in range(len(list2)):
    if list1[i] == list2[i]:
        countok+=1
    else:
        countno+=1
        #print(str(list1[i])+"\t"+str(list2[i]))
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


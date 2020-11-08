#!/usr/bin/env python
# coding: utf-8

import os
import subprocess
op = open("/home/nooroka/backupnores02102020/interaction_mode_uncorr.txt","r")
op2 = open("/home/nooroka/backupnores02102020/interaction_mode_corr.txt","w")
list1 = []
list2 = []
dict1 = {}
dict2 = {}
listcompare = []
listcompare2 = []
listcompare3 = []
listcompare4 = []
for line in op:
    os.chdir("/home/npidb/data/pdb_new/dna")
    line3 = line.split(".")
    if os.path.exists("pdb{}.pdb".format(line3[0])): 
        os.chdir("/home/nooroka/backupnores02102020/scripts")
        line = line.replace("|"," ")
        line = line.strip()
        line = line.split(" ",1)
        if len(line) > 1:
            line[1] = line[1].split()
            line[1] = sorted(line[1]) #сортируются Interaction_modes
            list2.append(' '.join(map(str,line[1])))
            dict1[line[0]] = ' '.join(map(str, line[1]))
            op2.write(str(line[0])+"\t"+str(' '.join(map(str,line[1])))+'\n')
        else:
            dict1[line[0]] = " "
            op2.write(str(line[0])+'\n')
op.close()
op2.close()

process1 = subprocess.Popen(["sort", "-nk1", "/home/nooroka/backupnores02102020/interaction_mode_corr.txt"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
data1,data11 = process1.communicate()
with open('/home/nooroka/backupnores02102020/interaction_mode_corr_sorted.txt', 'w') as f:
       f.write(data1)
f1 = open('/home/nooroka/backupnores02102020/interaction_mode_corr_sorted.txt',"r")
for line3 in f1:
    line3 = line3.strip()
    line3 = line3.split('\t',1)
    listcompare.append(str(line3[0]))
    if len(line3) > 1:
        listcompare3.append(str(line3[1]))
    else:
        listcompare3.append(" ")

op3 = open("/home/nooroka/backupnores02102020/result_sqldatabase_updated_new_sorted.txt","r")
op4 = open("/home/nooroka/backupnores02102020/result_sqldatabase_updated_new_sortedcorr.txt","w")
for line2 in op3:
    line2 = line2.strip()
    line2 = line2.split(" ",1)
    if len(line2) > 1:
        line2[1] = line2[1].split()
        line2[1] = sorted(line2[1]) #сортируются Interaction modes #уже отсортированы, но пусть будет
        list1.append(' '.join(map(str,line2[1])))
        dict2[line2[0]] = ' '.join(map(str, line2[1]))
        op4.write(str(line2[0])+"\t"+str(' '.join(map(str,line2[1])))+'\n')
    else:
        dict2[line2[0]] = " "
        op4.write(str(line2[0])+'\n')
op3.close()
op4.close()


process2 = subprocess.Popen(["sort", "-nk1", "/home/nooroka/backupnores02102020/result_sqldatabase_updated_new_sortedcorr.txt"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
data2,data22 = process2.communicate()
with open('/home/nooroka/backupnores02102020/result_sqldatabase_updated_new_sortedcorrsorted.txt', 'w') as f:
       f.write(data2)
os.remove("/home/nooroka/backupnores02102020/result_sqldatabase_updated_new_sortedcorr.txt")
f2 = open('/home/nooroka/backupnores02102020/result_sqldatabase_updated_new_sortedcorrsorted.txt',"r")
for line4 in f2:
    line4 = line4.strip()
    line4 = line4.split('\t',1)
    listcompare2.append(str(line4[0]))
    if len(line4) > 1:
        listcompare4.append(str(line4[1]))
    else:
        listcompare4.append(" ")


countok = 0
countno = 0
countok2 = 0
countno2 = 0
countok3 = 0
countno3 = 0
for key in dict1:
    #print("dict1[key] " +str(dict1[key]))
    #print("dict2[key] "+str(dict2[key]))
    if dict1[key] == dict2[key]:
        countok3+=1
    else:
        countno3+=1

print("len(dict1) "+str(len(dict1)))
print("len(dict2) "+str(len(dict2)))

for item in range(len(listcompare)):
    if listcompare[item] == listcompare2[item]:
        countok2 += 1
    else:
        countno2 += 1
for item in range(len(listcompare3)): #это interaction modes
    if listcompare3[item] == listcompare4[item]:
        countok += 1
    else:
        countno += 1
#print(listcompare3)
print("countok "+str(countok))
print("countno "+str(countno))
print("countok2 "+str(countok2))
print("countno2 " + str(countno2))
print("countok3 "+str(countok3))
print("countno3 " + str(countno3))

print(len(dict1))
print(len(dict2))

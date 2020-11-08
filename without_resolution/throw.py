#!/usr/bin/env python
#coding: utf-8

from collections import defaultdict
op2 = open("/home/nooroka/backupnores02102020/families/domainsend23_red_three.txt","w")
op = open("/home/nooroka/backupnores02102020/families/domainsend23_red.txt", "r")
op3 = open("/home/nooroka/backupnores02102020/families/dictinter5.txt","r")
op4 = open("/home/nooroka/backupnores02102020/families/dictinter7.txt","w")
op5 = open("/home/nooroka/backupnores02102020/uniprot/familiesend_red.txt","r")
dict1 = defaultdict(list)
'''залезли в файл доменов для семейств'''
dict2 = {}
for line5 in op5:
    line5 = line5.strip()
    line5 = line5.split("\t",1)
    if len(line5) > 1: #берем только непустые
       dict2[line5[0]] = line5[1]
print(dict2)
for line in op:
    count = 0
    line = line.strip()
    line = line.split("\t")
    line[1] = line[1].split(" ")
    for j in range(len(line[1])):
        if line[1][j]  in dict2.keys():
            count+=1
    print(str(line[0])+" "+str(count))
    if len(line[1]) >= 3 and len(line[1]) == len(set(line[1])) and count >= 3: #eсли непустых хотя бы три       
        key,value = str(line[0]),str(' '.join(line[1]))
        dict1[key].append(value)
        op2.write(str(line[0]) +"\t"+' '.join(line[1])+"\n")
    else:
        op2.write(str(line[0])+"\t"+"NULL"+"\n")
        key,value = str(line[0]),"NULL"
        dict1[key].append(value)


#print(dict1)#словарь семейства-домены, с NULL
for line3 in op3:
    line3 = line3.strip()
    lined = line3.split()
    if str(lined[0]) in dict1.keys():
          if dict1[lined[0]] == ['NULL']:
              op4.write(str(lined[0])+"\t"+"NULL"+"\n")
          else:
              op4.write(str(line3)+"\n")
op.close()
op2.close()
op3.close()
op4.close()

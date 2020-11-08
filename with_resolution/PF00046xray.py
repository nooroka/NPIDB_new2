#!/usr/bin/env python
#coding: utf-8
from collections import defaultdict
op = open("/home/nooroka/backupres02102020/res/xray.txt","r")
op4 = open("/home/nooroka/backupres02102020/res/nmr.txt","r")
op2 = open("/home/nooroka/backupres02102020/PF00046_int.txt","r")
op3 = open("/home/nooroka/backupnores02102020/uniprot/structsend.txt","r") #потому что нужно для структур без разрешения посмотреть
list1 = []
list2 = []
list11 = []
list111 = []
dict3 = {}
count = 0
count4 = 0
for line in op:
    line = line.strip()
    line = line.split()
    list1.append(line[0])
op.close()
for line4 in op4:
    line4 = line4.strip()
    line4 = line4.split()
    list11.append(line4[0])
op4.close()
for line2 in op2:
    linex = line2.strip()
    linex = linex.split(".")
    if linex[0] in list1:
        count+=1
        line2 = line2.strip()
        line2 = line2.split(" ",1) 
        list2.append(line2[0])
    if linex[0] in list11:
        count4+=1
    elif linex[0] not in list1:
        print(linex[0])
   
print("count " + str(count))#количество структур с xray
print("count4 "+str(count4))#количество структур с nmr
#print(list2)
listdomains = []

#z = [[list2[item] for item in range(len(list2))] for line3 in op3]
for line3 in op3:
    line3 = line3.strip()
    line3 = line3.split("\t",1)
    for item in range(len(list2)):
        if list2[item] in line3[1]:
            listdomains.append(str(line3[0]))
            #print(str(line3[0])+" "+str(list2[item]))
setdomains = set(listdomains)
print(len(listdomains))
print(setdomains)
print("domains " +str(len(setdomains)))



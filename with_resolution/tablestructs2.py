#!/usr/bin/env python
# coding: utf-8

import sys
listdomains2 = []
listfamilies2 = []
list1 = []
op5 = open("/home/nooroka/backupres02102020/res/listresstructs.txt","r")
for line in  op5:
    line = line.strip()
    line = line.split()
    list1.append(str(line[0]))
op5.close()

op2 = open("/home/nooroka/backupres02102020/result_sqldatabase_updated_new_sorted.txt","r")
for line2 in op2:
    line2 = line2.strip()
    line2 = line2.split(" ",1)
    if len(line2) > 1: #не учитываем случаи, где пустой Interaction mode
        if str(line2[1]) == str(sys.argv[1]) and str(line2[0]) in list1:
             op3 = open("/home/nooroka/backupres02102020/uniprot/structsend.txt", "r")
             for line3 in op3:
                 line3 = line3.strip()
                 line3 = line3.split("\t",1)
                 line3[1] = line3[1].strip()
                 if str(line2[0]) in str(line3[1]):
                     listdomains2.append(line3[0])
                     op4 = open("/home/nooroka/backupres02102020/families/domainsend23.txt","r")
                     for line4 in op4:
                         line4 = line4.strip()
                         line4 = line4.split("\t",1)
                         if str(line3[0]) in str(line4[1]):
                             listfamilies2.append(line4[0])
                     op4.close()
             op3.close()







#print(listdomains2)
#print(listfamilies2)
w = open("/home/nooroka/backupres02102020/listdomainfam.txt","w")
w.write(str(listdomains2)+'\n')
w.write(str(listfamilies2)+'\n')
w.close()
#print(str(sys.argv[1]))
#print("domains_in_structs "+str(len(set(listdomains2))))
#print("families_in_structs "+str(len(set(listfamilies2))))
#print("\n")
print(str(sys.argv[1])+"\t"+str(len(set(listdomains2)))+"\t"+str(len(set(listfamilies2))))

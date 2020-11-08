#!/usr/bin/env python
#coding: utf-8
op = open("/home/nooroka/backupres02102020/PF00046_structs.txt","r")
w = open("/home/nooroka/backupres02102020/PF00046_int.txt","w")
w1 = open("/home/nooroka/backupres02102020/pdb.txt","w")
listresstructs = []
opl = open("/home/nooroka/backupres02102020/res/listresstructs.txt","r")
list1 = []
countstructs = 0 #подсчет количества структур
#если убрать часть с listresstructs, то без учета разрешения
for linel in opl:
    linel = linel.strip()
    listresstructs.append(linel)

for line in op:
    line = line.strip()
    line = line.split()
    for i in range(len(line)):
        op2 = open("/home/nooroka/backupres02102020/result_sqldatabase_updated_new_sorted.txt","r")
        for line2 in op2:
            if str(line[i]) in line2:
            #if str(line[i]) in line2 and str(line[i]) in listresstructs:
                countstructs+=1
                line2 = line2.strip()
                w.write(str(line2)+"\n")
                line2 = line2.split(".")
                if line2[0] not in list1:
                   list1.append(line2[0])
                   w1.write(str(line2[0])+";"+" ")
        op2.close()
w1.close()
w.close()
op.close()

count2 = 0
op3 = open("/home/nooroka/backupres02102020/PF00046_int.txt","r")
for line3 in op3:
    line3 = line3.strip()
    line3 = line3.split(" ",1)
    if len(line3) > 1:
        if  "L-Mj" in line3[1]:
            print(line3)
            count2+=1
op3.close()
print(count2)
print(countstructs)
    

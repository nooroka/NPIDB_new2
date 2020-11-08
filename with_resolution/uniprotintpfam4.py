#!/usr/bin/env python
#coding: utf-8
import os
import subprocess
from collections import defaultdict
list1 = []
listk1 = []
listk2 = []
listk21 = []
listk22 = []
list2 = []
list3 = []
list4 = []
list9 = []


#fileok = open("fileok.txt","w") #проверка на то, что в обоих файлах названия из sql соответствуют друг другу
f = open("/home/nooroka/backupres02102020/res/listresdomains_sorted.txt","r")#отбираем хиты с подходящим разрешением
listres = [line.rstrip() for line in f]
f.close()

#отсортируем оба файла по nk1
#op = open("interaction_mode_uniprot3.txt", "r")


w1 = open("/home/nooroka/backupres02102020/test4.txt","w")# просто в папке scripts, но, видимо, это не влияет, так как потом все равно сразу в список
w2 = open("/home/nooroka/backupres02102020/test3.txt","w")

r11 = []
r1 = open("/home/nooroka/backupres02102020/interaction_mode_uniprot6.txt").readlines()
for line1111 in r1:
    line1111 = line1111.strip()
    line1111 = line1111.split()
    r11.append(line1111)

a1 = sorted(r11, key=lambda student: student[0])
for item in a1:
    w1.write(' '.join(map(str,item))+"\n")
w1.close()

r22 = []
r2 = open("/home/nooroka/backupres02102020/result_sqldatabase_updated_new_sorted.txt").readlines()
for line2222 in r2:
    line2222 = line2222.strip()
    line2222 = line2222.split()
    r22.append(line2222)

a2 = sorted(r22, key=lambda student: student[0])
for item2 in a2:
    w2.write(' '.join(map(str,item2))+"\n")
w2.close()
##subprocess.call("sort -nk1 interaction_mode_uniprot6.txt > test1.txt",shell = True)
#subprocess.call("sort -nk1 result_sqldatabase.txt > test2.txt",shell = True)
op = open("/home/nooroka/backupres02102020/test4.txt","r")
#opw = open("test4cropped.txt","w")
for line in op:
    line = line.split()
    a = line[0].split(".")
    os.chdir("/home/npidb/data/pdb_new/dna")
    list9.append(line[2].strip())
    if os.path.exists("pdb{}.pdb".format(a[0])):
        list1.append(line[0].strip()) #добавляем файл
        list2.append(line[1].strip()) #добавляем uniprot-идентификаторы         
        #opw.write(str(line[0].strip())+"\t"+str(line[1].strip())+"\n")

    '''
    os.chdir("/home/npidb/data/pdb_new/stride/")
    if os.path.exists("{}.std.txt".format(a[0])):
         listk2.append(line[0].strip())
         listk22.append(line[1].strip())
    '''

#opw.close()
op.close()
os.chdir("/home/nooroka/backupres02102020/scripts")
#op2 = open("result_sqldatabase.txt","r")
op2 = open("/home/nooroka/backupres02102020/test3.txt","r") #отсортированный по nk файл
for line2 in op2:
    line2 = line2.split(" ",1)   
    list3.append(line2[0].strip())#файлы
    if len(line2) > 1:
        list4.append(line2[1].strip())#interaction_modes
    else:
        list4.append(" ")

op2.close()
countok = 0
countno = 0
print(set(list1)-set(list3))
data = defaultdict(list)
data2 = defaultdict(list)#словарь структур, соответствующих uniprot
#opw = open("uniprot.txt","w")#совпадает с uniprot.txt  в check.py
#opw2 = open("uniprot2.txt", "w")
print(len(list1))
print(len(list3))
for i in range(len(list1)):
    if str(list1[i]) == str(list3[i]):        
        countok+=1
    else:        
        countno+=1
    if list2[i] in listres:
        key,value = list2[i],list4[i]
        data[key].append(value)#словарь, где для каждого uniprot написаны все interaction mode
        key2, value2 = list2[i], list1[i]
        data2[key2].append(value2)
        if list1[i] in list3:
            ak = list3.index(list1[i])
#opw.close()
#opw2.close()
#fileok.close()
print("countok "+str(countok))
print("countno "+str(countno))
fam = open("/home/nooroka/backupres02102020/uniprot/families.txt","w")
for key1 in data:
    data[key1] = ' '.join(data[key1]) #объединить значения value словаря #если просто сделать set, то пишет только буквы с запятыми
    data[key1] = set(data[key1].split())
    fam.write(str(key1)+"\t"+str(sorted(data[key1]))+"\n")
print(len(data))
fam3 = open("/home/nooroka/backupres02102020/uniprot/structsres.txt","w")
fam2 = open("/home/nooroka/backupres02102020/uniprot/structs.txt","w")
for key3 in data2:
     fam2.write(str(key3)+"\t"+str(data2[key3])+"\n")
     fam3.write(str(key3)+"\t"+str(len(data2[key3]))+"\t"+str(' '.join(map(str,data2[key3])))+"\n")
fam.close()
fam2.close()
fam3.close()

list5 = []
list6 = []
process3 = subprocess.Popen(["sort", "-k1", "/home/nooroka/backupres02102020/uniprot/structs.txt"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
data3,data33 = process3.communicate()
with open('/home/nooroka/backupres02102020/uniprot/structsend.txt', 'w') as f:
       f.write(data3)

process4 = subprocess.Popen(["sort", "-k1", "/home/nooroka/backupres02102020/uniprot/families.txt"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
data4,data44 = process4.communicate()
with open('/home/nooroka/backupres02102020/uniprot/familiesend.txt', 'w') as f2:
       f2.write(data4)



op3 = open("/home/nooroka/backupres02102020/uniprot/structsend.txt","r")
op4 = open("/home/nooroka/backupres02102020/uniprot/familiesend.txt","r")
for line3 in op3:
    line3 = line3.split()
    list5.append(line3[0])
for line4 in op4:
    line4 = line4.split()
    list6.append(line4[0])
op3.close()
op4.close()
countok2 = 0
countno2 = 0
for k in range(len(list5)):
    if list5[k] == list6[k]:
        countok2 += 1
    else:
        countno2 += 1


print("countok2 "+str(countok2))
print("countno2 "+str(countno2)) 
##хотя в табличке там,a где нет stride, они учитываются
os.remove("/home/nooroka/backupres02102020/uniprot/structs.txt")
os.remove("/home/nooroka/backupres02102020/uniprot/families.txt")
op9 = open("/home/nooroka/backupres02102020/uniprot/familiesend.txt","r")
op10 = open("/home/nooroka/backupres02102020/uniprot/familiesend_red.txt","w")
for line15 in op9:
    line15 = line15.replace("'","")
    line15 = line15.replace("]","")
    line15 = line15.replace("[","")
    line15 = line15.replace(",","")
    op10.write(str(line15))
op9.close()
op10.close()

#os.remove("fileok.txt")

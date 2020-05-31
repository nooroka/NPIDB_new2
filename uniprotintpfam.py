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
filelist1 = open("filelist1.txt","w")
filelist2 = open("filelist2.txt","w")
fileok = open("fileok.txt","w") #проверка на то, что в обоих файлах названия из sql соответствуют друг другу

#отсортируем оба файла по nk1
#op = open("interaction_mode_uniprot3.txt", "r")
file1 = "interaction_mode_uniprot6.txt"
file2 = "resultsqldatabase.txt"
'''
#не работает
command = ["sort -nk1",file1+">test1.txt"]
seqret = Popen(command, shell=True, stdout = PIPE, stderr = PIPE)
seqret.wait()
(a,b) = seqret.communicate()
command2 = ["sort -nk1", file2+">test2.txt"]
seqret2 = Popen(command2, shell=True, stdout = PIPE, stderr = PIPE)
seqret2.wait()
(a2,b2) = seqret2.communicate()
'''
subprocess.call("sort -nk1 interaction_mode_uniprot6.txt > test1.txt",shell = True)
subprocess.call("sort -nk1 result_sqldatabase.txt > test2.txt",shell = True)
op = open("test1.txt","r")
opw = open("test1cropped.txt","w")
for line in op:
    line = line.split()
    a = line[0].split(".")
    os.chdir("/home/verassd/home/vera/Документы/NPIDB/dna/")
    list9.append(line[2].strip())
    if os.path.exists("pdb{}.pdb".format(a[0])):
        list1.append(line[0].strip()) #добавляем файл
        list2.append(line[1].strip()) #добавляем uniprot-идентификаторы
        #list9.append(line[2].strip()) 
        opw.write(str(line[0].strip())+"\t"+str(line[1].strip())+"\n")

    '''
    os.chdir("/home/npidb/data/pdb_new/stride/")
    if os.path.exists("{}.std.txt".format(a[0])):
         listk2.append(line[0].strip())
         listk22.append(line[1].strip())
    '''
opw.close()
op.close()
os.chdir("/home/verassd/home/vera/Документы/NPIDB/")
#op2 = open("result_sqldatabase.txt","r")
op2 = open("test2.txt","r") #отсортированный по nk файл
for line2 in op2:
    line2 = line2.split(" ",1)
    list3.append(line2[0].strip())#файлы
    list4.append(line2[1].strip())#interaction_modes
op2.close()
countok = 0
countno = 0
data = defaultdict(list)
data2 = defaultdict(list)#словарь структур, соответствующих uniprot
opw = open("uniprot.txt","w")#совпадает с uniprot.txt  в check.py
opw2 = open("uniprot2.txt", "w")
for i in range(len(list1)):
    if str(list1[i]) == str(list3[i]):
        fileok.write(str(list1[i])+" "+str(list3[i])+" ok"+"\n")
        countok+=1
    else:
        fileok.write(str(list1[i])+" "+str(list3[i])+" no"+"\n")
        countno+=1
    opw.write(str(list1[i])+" "+str(list2[i])+" "+str(list4[i])+"\n")
    opw2.write(str(list1[i])+"\t"+str(list2[i])+"\t"+str(list4[i])+"\n")
    key,value = list2[i],list4[i]
    data[key].append(value)#словарь, где для каждого uniprot написаны все interaction mode
    key2, value2 = list2[i], list1[i]
    data2[key2].append(value2)
    if list1[i] in list3:
        ak = list3.index(list1[i])
opw.close()
opw2.close()
fileok.close()
print("countok "+str(countok))
print("countno "+str(countno))
fam = open("families.txt","w")
for key1 in data:
    data[key1] = ' '.join(data[key1]) #объединить значения value словаря #если просто сделать set, то пишет только буквы с запятыми
    data[key1] = set(data[key1].split())
    fam.write(str(key1)+"\t"+str(data[key1])+"\n")
print(len(data))
fam2 = open("structs.txt","w")
for key3 in data2: #data неверен, но ошибки не было, так как раньше делался
     fam2.write(str(key3)+"\t"+str(data2[key3])+"\n")
fam.close()
fam2.close()

list5 = []
list6 = []
subprocess.call("sort -k1 structs.txt > structsend.txt",shell = True)
subprocess.call("sort -k1 families.txt > familiesend.txt",shell = True)
op3 = open("structsend.txt","r")
op4 = open("familiesend.txt","r")
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
fileok2 = open("fileok2.txt","w") #проверка на то, что названия в файлах uniprot и структурами соответствуют друг другу
for k in range(len(list5)):
    if list5[k] == list6[k]:
        fileok2.write("ok2"+"\n")
        countok2 += 1
    else:
        fileok2.write("no"+"\n")
        countno2 += 1
print("countok2 "+str(countok2))
print("countno2 "+str(countno2)) 
#list1 = list(set(listk1)&set(listk2))
#list2 = list(set(listk21)&set(listk22))
list8 = []
k = open("interaction_mode_uniprot3.txt","r")
for line3 in k:
   line3 = line3.split()
   list8.append(line3[1])
k.close()
fam.close()
print(len(list8))
print(len(list9))
diff = list(set(sorted(list8))-set(sorted(list9)))
print("diff "+str(diff))
#print(len(list1))
#print(len(list2))
#print(len(list3))
#print(len(list4))
filelist1.close()
filelist2.close()
#хотя в табличке там,a где нет stride, они учитываются

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


fileok = open("fileok.txt","w") #проверка на то, что в обоих файлах названия из sql соответствуют друг другу

''' 
process1 = subprocess.Popen(["sort", "-nk1", "interaction_mode_families.txt"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
data1,data11 = process1.communicate()
with open('test6.txt', 'w') as f:
       f.write(data1)
process2 = subprocess.Popen(["sort", "-nk1", "result_sqldatabase_updated_sorted.txt"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
data2,data22 = process2.communicate()
with open('test2.txt', 'w') as f:
       f.write(data2)
'''
w1 = open("/home/nooroka/backupres02102020/test6.txt","w")
w2 = open("/home/nooroka/backupres02102020/test2.txt","w")

r11 = []
r1 = open("/home/nooroka/backupres02102020/interaction_mode_families.txt").readlines()
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
op = open("/home/nooroka/backupres02102020/test6.txt","r")
#opk = open("test1cropped.txt","w")
for line in op:
    line = line.split()
    a = line[0].split(".")
    os.chdir("/home/npidb/data/pdb_new/dna")
    if os.path.exists("pdb{}.pdb".format(a[0])):
        list1.append(line[0].strip()) #добавляем файл
        list2.append(line[1].strip()) #добавляем uniprot-идентификаторы
        list9.append(line[2].strip()) #добавляем идентификаторы семейств
        #opk.write(str(line[0].strip())+"\t"+str(line[1].strip())+"\t"+str(line[2].strip()) + "\n")



#opk.close()
op.close()
os.chdir("/home/nooroka/backupres02102020/scripts")


op2 = open("/home/nooroka/backupres02102020/test2.txt","r") #отсортированный по nk файл
for line2 in op2:
    line2 = line2.split(" ",1)
    if (line2[0].strip() in list1):# убираем лишнее в Interaction class
        list3.append(line2[0].strip())#структуры
        if len(line2) > 1:
            list4.append(line2[1].strip())#interaction_modes
        else:
            list4.append(" ")


op2.close()
countok = 0
countno = 0
data = defaultdict(list)
data2 = defaultdict(list)#словарь структур, соответствующих uniprot
data4 = defaultdict(list) #словарь доменов, соответствующих семействам
#opw = open("familiesprom.txt","w")#совпадает с uniprot.txt  в check.py
#opw2 = open("familiesprom2.txt", "w")
for i in range(len(list1)):
    if str(list1[i]) == str(list3[i]):
        fileok.write(str(list1[i])+" "+str(list3[i])+" ok"+"\n")
        countok+=1
    else:
        fileok.write(str(list1[i])+" "+str(list3[i])+" no"+"\n")
        countno+=1
  #  opw.write(str(list1[i])+" "+str(list2[i])+" "+str(list9[i])+" "+str(list4[i])+"\n")
  #  opw2.write(str(list1[i])+"\t"+str(list2[i])+"\t"+str(list9[i])+"\t"+str(list4[i])+"\n")
    key2, value2 = list9[i], list1[i]
    if value2 not in data2[key2]:
        data2[key2].append(value2)
    key4, value4 = list9[i], list2[i]
    #if value4 not in data4[key4]:#не обязательно, с set то же самое, здесь, если убрать set, будут скобочки [
    data4[key4].append(value4)
    if list1[i] in list3:
        ak = list3.index(list1[i])
#opw.close()
#opw2.close()
fileok.close()
print("countok "+str(countok))
print("countno "+str(countno))


fam2 = open("/home/nooroka/backupres02102020/families/structs2.txt","w")#структуры и так не повторяются
for key3 in data2:      
     fam2.write(str(key3)+"\t"+str(data2[key3])+"\n")
fam3 = open("/home/nooroka/backupres02102020/families/domains2.txt","w")
for key5 in data4:
     data4[key5] = ' '.join(data4[key5])
     data4[key5] = set(data4[key5].split())
     fam3.write(str(key5)+"\t"+str(data4[key5])+"\n")

fam2.close()
fam3.close()
list5 = []
list6 = []
list7 = []

process3 = subprocess.Popen(["sort", "-k1", "/home/nooroka/backupres02102020/families/structs2.txt"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
data3,data33 = process3.communicate()
with open('/home/nooroka/backupres02102020/families/structsend23.txt', 'w') as f:
       f.write(data3)
process5 = subprocess.Popen(["sort", "-k1", "/home/nooroka/backupres02102020/families/domains2.txt"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
data5,data55 = process5.communicate()
with open('/home/nooroka/backupres02102020/families/domainsend23.txt', 'w') as f:
       f.write(data5)

os.remove("/home/nooroka/backupres02102020/families/structs2.txt")
os.remove("/home/nooroka/backupres02102020/families/domains2.txt")


op3 = open("/home/nooroka/backupres02102020/families/structsend23.txt","r")
op5 = open("/home/nooroka/backupres02102020/families/domainsend23.txt","r")
for line3 in op3:
    line3 = line3.split()
    list5.append(line3[0])
for line5 in op5:
    line5 = line5.split()
    list7.append(line5[0])

op3.close()
op5.close()
countok2 = 0
countno2 = 0
#проверка на то, что названия в файлах uniprot и структурами соответствуют друг другу
for k in range(len(list5)):
    if list5[k] == list7[k]:
        countok2 += 1
    else:
        countno2 += 1
print("countok2 "+str(countok2))
print("countno2 "+str(countno2)) 

list8 = []
#хотя в табличке там,a где нет stride, они учитываются
'''changes'''

dict5 = defaultdict(list) #all interaction mode for one family
op8 = open("/home/nooroka/backupres02102020/families/domainsend23.txt", "r")
opl = open("/home/nooroka/backupres02102020/families/domainsend23_red.txt","w")
for line11 in op8:
    line11 = line11.replace("set([","")
    line11 = line11.replace("'","")
    line11 = line11.replace("])","")
    line11 = line11.replace(",","")
    opl.write(str(line11))
op8.close()
opl.close()
op28 = open("/home/nooroka/backupres02102020/families/structsend23.txt", "r")
op28l = open("/home/nooroka/backupres02102020/families/structsend23_red.txt","w")
for line22 in op28:
    line22 = line22.replace("[","")
    line22 = line22.replace("'","")
    line22 = line22.replace("]","")
    line22 = line22.replace(",","")
    op28l.write(str(line22))
op28.close()
op28l.close()

'''
эта часть есть в uniprotintpfam.py
op9 = open("familiesend.txt","r")
op10 = open("familiesend_red.txt","w")
for line15 in op9:
    line15 = line15.replace("set([","")
    line15 = line15.replace("'","")
    line15 = line15.replace("])","")
    line15 = line15.replace(",","")
    op10.write(str(line15))
op9.close()
op10.close()
'''

op7 = open("/home/nooroka/backupres02102020/families/domainsend23_red.txt", "r")
for line10 in op7:
    line10 = line10.strip()
    line10 = line10.split("\t",1)
    lined = line10[1]
    lined = lined.strip()
    lined = lined.split()
    for i in range(len(lined)):
        op8 = open("/home/nooroka/backupres02102020/uniprot/familiesend_red.txt","r")
        for line11 in op8:
            line11 = line11.split("\t",1)
            if len(line11) > 1:
                line11[1] = line11[1].strip()
                if str(lined[i]) in line11[0]:
                    key11,value11 = str(line10[0]),str(line11[1])
                  #  wk2.write(str(key11)+" "+str(value11)+"\n")
                    dict5[key11].append(value11)
                elif len(line11) == 1:
                    key11,value11 = str(line10[0]), ""
                    dict5[key11].append(" ")

'''
for line in op1:
    line = line.strip()
    line = line.split("\t")
    list1.append(line[0])
'''

for key12 in dict5:
    for i in range(len(dict5[key12])):
        dict5[key12][i] = dict5[key12][i].split()
        dict5[key12][i] = set(dict5[key12][i])

d2 = {}
for k,v in dict5.items():
    d2[k] = set.intersection(*v)


wdict3 = open("/home/nooroka/backupres02102020/families/dictinter3.txt","w")
for k2 in d2:
    wdict3.write(str(k2)+"\t"+str(' '.join(sorted(d2[k2])))+"\n")
wdict3.close()
op11 = open("/home/nooroka/backupres02102020/families/dictinter4.txt","w")
wdict4 = open("/home/nooroka/backupres02102020/families/dictinter3.txt","r")
for line20 in wdict4:
    line20 = line20.replace("set([","")
    line20 = line20.replace("'","")
    line20 = line20.replace("])","")
    line20 = line20.replace(",","")
    op11.write(str(line20))
op11.close()
process3 = subprocess.Popen(["sort", "-k1", "/home/nooroka/backupres02102020/families/dictinter4.txt"], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
data3,data33 = process3.communicate()
with open('/home/nooroka/backupres02102020/families/dictinter5.txt', 'w') as f:
       f.write(data3)

#os.remove("fileok.txt")
#os.remove("/home/nooroka/backupres02102020/families/dictinter3.txt")
#os.remove("/home/nooroka/backupres02102020/families/dictinter4.txt")

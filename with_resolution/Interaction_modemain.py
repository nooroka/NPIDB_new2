#!/usr/bin/env python
# coding: utf-8

import os
import sys
import glob
import re


mj = {"A":["C5","C6","N6","N7","C8"],"T":["C4","O4","C5","C6","C7"],"G":["C5","C6","O6","N7","C8"],"C":["C4","N4","C5","C6"]}
mi = {"A":["N1","C2","N3","C4"],"T":["C2","O2","N3"],"G":["N1","C2","N2","N3","C4"],"C":["C2","O2","N3"]}
listprotein = []
listdna = []
file = sys.argv[1]

'''вытаскиваю из названия pfam-файла цифру и цепь'''    
file2 = file.split("_")
chainpfam1 = file2[0].split("_")
chainpfam2 = file2[0].split(".")
file3 = file2[1].split(".")[0] #цифры из pfam
countfile = 0
file3pfam = file3.split("-")
if file3[0]!="-":
    countfile = 0
else:
    countfile = 1

file4pfam = file3.split("-",2)


if len(file4pfam) > 2 and float(file4pfam[2]) < 0:
    countfile = 2
    file4pfam[1] = -int(file4pfam[1])
    file4pfam = file4pfam[1:] #убрать пустой элемент

chainpfam2 = str(chainpfam2[1]) #цепь из pfam



os.chdir("/home/npidb/data/pdb_new/Hbond")
#две биоединицы - две структуры, по сути
import re
dictint = {}
filesplit = file.split(".")
#print(filesplit)
if filesplit[3] != "pdb":
    filenorm = "{}.{}.pdb.hb.txt".format(filesplit[0],filesplit[3]) #в "неподходящих" файлах просто pdb
elif filesplit[3] == "pdb":
    filenorm = "pdb{}.pdb.hb.txt".format(filesplit[0])#должно быть, только если файла, не начинающегося с pdb, нет

if filenorm in sorted(os.listdir(".")): 
    op = open(filenorm)
    linefirst = op.readline()
    if "# File" in linefirst:
        for line in op:
            line2 = line.split() #line2[0] должен быть ДНК, line2[1] должен быть белок. но нужно предусмотреть случаи, когда наоборот #не было предусмотрено(
            if str.find(line, '#') == -1 and str.find(line, 'File') == -1 and str.find(line, 'Hydrogen') == -1 and str.find(line, 'Atom') == -1:    
                        if "5IU" not in line2[0]:
                            linespl = re.split(':.',line2[0]) #убираем цепь из середины #оставляем D.. и остаток
                        else:
                            continue
                        linespl1 = linespl[1].split('.')
                        if "%" not in linespl1[1]:
                            linespl2 = linespl1[1].split('/')
                        elif "%" in linespl1[1]:
                            linespl3 = linespl1[1].split('/')                            
                            linespl4 = linespl3[0][:-2]#но это строка
                            linespl2 = []
                            linespl2.append(linespl4)
                        linespl11 = line2[1].split(':')
                        linespl12 = linespl11[1].split('.')
                        linex = str(linespl11[0])+":"+str(linespl12[0])#конструирую белок из файла Hbond  белок:цепь
                        '''эта часть с linex и protein нужна для того, чтобы посмотреть, совпадают ли белки из файла со вторичной структурой (stride) и из файла Hbond'''
                        os.chdir("/home/npidb/data/pdb_new/stride")
                        listjoin = []
                        for filehb in os.listdir("."): #filehb - это файл из директории, которую мы рассматриваем, в данном случае Hbond
                            count = 0
                            if str('{}.std.txt'.format(filesplit[0])) == filehb and os.path.exists(str('{}.std.txt'.format(filesplit[0]))) == True: #если файл, который находится в списке, полученном из dna, находится и в этой директории #и существует #нет разницы
                                op3 = open(filehb,"r")
                                for line3 in op3:
                                    line3 = line3.split()       
                                    if line3[0] =="ASG":
                                        join2 = str(str(line3[1])+str(line3[3])+":"+str(line3[2])) #вытаскиваю из файла для stride инфу про белок (остатокномер:цепь)     
                                        if str(line3[2]) == str(linespl12[0]) and str(line3[2]) == chainpfam2: #eсли цепь равна той же, что и в stride и pfam
                                            count = 1
                                            if linex == join2 and "^" not in linex:#когда находим в файле со stride тот же белок, что и из hbond  
                                                protein = line3[6]#присваиваем значение белку  
                                            elif "^" in linex:
                                                linex3 = str(linex[0:5])+str(linex[6:])
                                                if linex3 == join2:
                                                    protein = line3[6]
                                        elif str(line3[2]) != str(linespl12[0]) or str(line3[2]) != chainpfam2: #если это закомментить, то 1a02 срабатывает #если цепи не равны
                                            if count == 1:
                                                pass #написать цепь из файла Hbond 
                                            else:
                                                protein = "NULL"         
                                op3.close()      
                            elif os.path.exists(str('{}.std.txt'.format(filesplit[0]))) == False:
                                protein = "NULL" 
                           

                        os.chdir("/home/nooroka/")
                        #'''dictgraph - словарь из hbond {номер в vertices:днк или белок}'''  
                        #'''line2[0][1] - это я вытаскиваю A,T,G,C'''
                        if linespl2[0]!="#" and (line2[0][1] in ["A","T","G","C"]):   
                            if  str(linespl2[0]) in  mj[str(line2[0][1])]: #mj[str(line2[0][1])] - это  азотистое основание днк #если остаток лежит в mj для соответствующего азотистого основания 
                                if  (protein == "Turn" or protein == "Coil" or protein == "Bridge"):
                                     if line2[0][0] == "D":
                                         dictint.update({str(line2[0])+" "+str(line2[1]):"L-Mj"})
                                     elif line2[1][0] == "D":
                                         dictint.update({str(line2[1])+" "+str(line2[0]):"L-Mj"})
                                elif (protein == "AlphaHelix" or protein == "310Helix"):
                                     if line2[0][0] == "D":
                                         dictint.update({str(line2[0])+" "+str(line2[1]):"H-Mj"})
                                     elif line2[1][0] == "D":
                                         dictint.update({str(line2[1])+" "+str(line2[0]):"H-Mj"})
                                elif (protein == "Strand"):
                                     if line2[0][0] == "D":
                                        dictint.update({str(line2[0])+" "+str(line2[1]):"S-Mj"})
                                     elif line2[1][0] == "D":
                                        dictint.update({str(line2[1])+" "+str(line2[0]):"S-Mj"})
                            elif str(linespl2[0]) in mi[str(line2[0][1])]:  #также, как выше  
                                if  (protein == "Turn" or protein == "Coil" or protein == "Bridge"):
                                     if line2[0][0] == "D":
                                         dictint.update({str(line2[0])+" "+str(line2[1]):"L-Mn"})
                                     elif line2[1][0] == "D":
                                         dictint.update({str(line2[1])+" "+str(line2[0]):"L-Mn"})
                                elif (protein == "AlphaHelix" or protein == "310Helix"):
                                     if line2[0][0] == "D":
                                         dictint.update({str(line2[0])+" "+str(line2[1]):"H-Mn"})
                                     elif line2[1][0] == "D":
                                         dictint.update({str(line2[1])+" "+str(line2[0]):"H-Mn"})
                                elif (protein =="Strand"):
                                     if line2[0][0] == "D":
                                         dictint.update({str(line2[0])+" "+str(line2[1]):"S-Mn"})
                                     elif line2[1][0] == "D":
                                         dictint.update({str(line2[1])+" "+str(line2[0]):"S-Mn"})
                            else:
                                if  (protein == "Turn" or protein == "Coil" or protein == "Bridge"):
                                     if line2[0][0] == "D":
                                         dictint.update({str(line2[0])+" "+str(line2[1]):"L-Bb"})
                                     elif line2[1][0] == "D":
                                         dictint.update({str(line2[1])+" "+str(line2[0]):"L-Bb"})
                                elif (protein == "AlphaHelix" or protein == "310Helix"):
                                     if line2[0][0] == "D":
                                         dictint.update({str(line2[0])+" "+str(line2[1]):"H-Bb"})
                                     elif line2[1][0] == "D":
                                         dictint.update({str(line2[1])+" "+str(line2[0]):"H-Bb"})
                                elif (protein =="Strand"):
                                     if line2[0][0] == "D":
                                         dictint.update({str(line2[0])+" "+str(line2[1]):"S-Bb"})
                                     elif line2[1][0] == "D":
                                         dictint.update({str(line2[1])+" "+str(line2[0]):"S-Bb"})

                        else:
                            continue

        op.close()

   


os.chdir("/home/npidb/data/pdb_new/hydrophobic")
import re 
dictgraph = {}
dictint2 = {}
listofdictint2keys = []
if filesplit[3] != "pdb":
    filenorm2 = "{}.{}.pdb.regraph.txt".format(filesplit[0],filesplit[3]) #в "неподходящих" файлах просто pdb
elif filesplit[3] == "pdb":
    filenorm2 = "pdb{}.pdb.regraph.txt".format(filesplit[0])#смотрим другой файл
if filenorm2 in sorted(os.listdir(".")):
            op = open(filenorm2)
            for line in op:
                line = line.strip()
                if len(line) == 0:
                    continue #не break, иначе будет печататься только до vertices
                if str.find(line,'vertices:') ==-1 and str.find(line,'edges:') == -1 and line.isspace() == False: #если в строке нет vertices и при этом строка не пустая
                    line2 = line.split()
                    if len(line2) == 2:
                        dictgraph.update({line2[0]:line2[1][1:-1]}) #срезом убираем кавычки   
                    elif len(line2) == 6:      #line2[1] - обычно цифра для  днк, line2[2] - обычно цифра для белка, но мб и не так.      
                      if line2[4] == '"WHITE:':
                            linesplhyd = re.split(':.',str(dictgraph[line2[1]])) #пишем белок или днк после white  
                            if linesplhyd[0][0] == "D":#если это днк #5IU также пропускаем  #но в hydrophobic файлах, видимо, его нет
                                dna = str(linesplhyd[0][1]) 
                                linesplhyd2 = linesplhyd[1].split('/')
                                if ";" not in linesplhyd2[0]:
                                    linesplhyd3 = linesplhyd2[0] #атомы, но с точкой .
                                elif ";" in linesplhyd2[0]:
                                    linesplhyd4 = linesplhyd2[0][:-2]
                                    linesplhyd3 = linesplhyd4
                                belok = str(dictgraph[line2[2]]) #белок
                                linespl = re.split(':',belok)
                                chain = linespl[1].split('.')
                                linespl3 = str(linespl[0][3:])+":"+str(chain[0]) #цифра белка + цепь
                                listofdictint2keys.append(linespl3)
                            elif linesplhyd[0][0] != "D" and linesplhyd[0][0:2] != "5IU" and linesplhyd[0][0:3].isalpha() == True: #если это белок
                                linesplhyd5 = re.split(':.',str(dictgraph[line2[2]])) #смотрим именно на ДНК  
                                if linesplhyd5[0][1].isalpha() == True:
                                    dna = str(linesplhyd5[0][1]) #пишем азотистое основание
                                else:
                                    dna = "N" 
                                linesplhyd2 = linesplhyd5[1].split('/')
                                if ";" not in linesplhyd2[0]:
                                    linesplhyd3 = linesplhyd2[0]
                                elif ";" in linesplhyd2[0]:
                                    linesplhyd4 = linesplhyd2[0][:-2]
                                    linesplhyd3 = linesplhyd4
                                belok  = str(dictgraph[line2[1]]) #белок, line2[1], ибо "перевернутый" случай
                                linespl = re.split(':',belok)
                                chain = linespl[1].split('.')
                                linespl3 = str(linespl[0][3:])+":"+str(chain[0])  #цифра белка + цепь
                                listofdictint2keys.append(linespl3)
                            '''зашла в stride, вытащила оттуда белки'''
                            os.chdir("/home/npidb/data/pdb_new/stride")
                            listjoin = []                                    
                            #filesplit[0] - это первая часть файла, pdbшный идентификатор, типа 2zo2 и тд
                            #filehyd - это файл в директории, которую я рассматриваю, в данном случае - hydrophobic1
                            for filehyd in os.listdir("."):
                                count2 = 0
                                if filesplit[0] in filehyd:  
                                    op3 = open(filehyd,"r")
                                    for line3 in op3:
                                        line3 = line3.split()
                                        if line3[0] =="ASG":
                                            join2 = str(str(line3[1])+str(line3[3])+":"+str(line3[2])) #вытаскиваю из файла для stride инфу про белок (остатокномер:цепь)
                                            listjoin.append(join2)  
                                            if str(line3[2]) == str(chain[0]) and str(line3[2]) == chainpfam2  and str(line3[1]) == str(linespl[0][0:3]) and str(line3[3]) == str(linespl[0][3:]):
                                                  count2 = 1  
                                                  protein = line3[6]#присвоила переменной protein значение, которое обозначает structure name
                                            else:
                                                if count2 == 1:
                                                    pass
                                                else:
                                                    protein = "NULL"
                                                                                     #смотрю равенство цепей и равенство белков и равенство цифр  в stride и hydrophobic и pfam
                                                                                     #чтобы в dictint лишние не попали

                                    op3.close()
                            if os.path.exists(str('{}.std.txt'.format(filesplit[0]))) == False:
                                    protein = "NULL"
                        
                            '''зашла в hydrophobic, посмотрела, major, minor или backbone соответствует ДНК, сравнила с белком (значение белка лежит в protein),
                            в зависимости от этого присвоила Interaction mode'''
                            os.chdir("/home/nooroka/")
                            '''dictgraph - словарь из hydrophobic {номер в vertices:днк или белок}'''  
                            '''переставляю элементы в словаре в зависимости от того, как они расположены - сначала днк, потом белок, или наоборот'''
                            if str.find(line,'vertices:') ==-1 and str.find(line,'edges:') == -1 and line.isspace() == False and dna!="N": 
                                if str(linesplhyd3[1:]) in mj[str(dna)]:                                     
                                    if  (protein == "Turn" or protein == "Coil" or protein == "Bridge"):
                                        if dictgraph[line2[1]][0] == "D":
                                            dictint2.update({dictgraph[line2[1]]+" "+dictgraph[line2[2]]:"L-Mj"}) 
                                        elif dictgraph[line2[2]][0] == "D":
                                            dictint2.update({dictgraph[line2[2]]+" "+dictgraph[line2[1]]:"L-Mj"})
                                    elif (protein == "AlphaHelix" or protein == "310Helix"):
                                        if dictgraph[line2[1]][0] == "D":
                                            dictint2.update({dictgraph[line2[1]]+" "+dictgraph[line2[2]]:"H-Mj"})
                                        elif dictgraph[line2[2]][0] =="D":
                                            dictint2.update({dictgraph[line2[2]]+" "+dictgraph[line2[1]]:"H-Mj"})
                                    elif (protein =="Strand"):
                                        if  dictgraph[line2[1]][0] == "D":
                                            dictint2.update({dictgraph[line2[1]]+" "+dictgraph[line2[2]]:"S-Mj"})    
                                        elif dictgraph[line2[2]][0] =="D":
                                            dictint2.update({dictgraph[line2[2]]+" "+dictgraph[line2[1]]:"S-Mj"}) 
                                elif str(linesplhyd3[1:]) in mi[str(dna)]:
                                    if  (protein == "Turn" or protein == "Coil" or protein == "Bridge"):
                                        if dictgraph[line2[1]][0] == "D": 
                                            dictint2.update({dictgraph[line2[1]]+" "+dictgraph[line2[2]]:"L-Mn"})
                                        elif dictgraph[line2[2]][0] == "D": 
                                           dictint2.update({dictgraph[line2[2]]+" "+dictgraph[line2[1]]:"L-Mn"})
                                    elif (protein == "AlphaHelix" or protein == "310Helix"):                                      
                                        if dictgraph[line2[1]][0] == "D":  
                                            dictint2.update({dictgraph[line2[1]]+" "+dictgraph[line2[2]]:"H-Mn"})
                                        elif dictgraph[line2[2]][0]== "D":  
                                            dictint2.update({dictgraph[line2[2]]+" "+dictgraph[line2[1]]:"H-Mn"})
                                    elif (protein =="Strand"):
                                        if dictgraph[line2[1]][0] == "D":
                                             dictint2.update({dictgraph[line2[1]]+" "+dictgraph[line2[2]]:"S-Mn"})
                                        elif dictgraph[line2[2]][0] == "D":
                                             dictint2.update({dictgraph[line2[2]]+" "+dictgraph[line2[1]]:"S-Mn"})   
                                else: 
                                    if  (protein == "Turn" or protein == "Coil" or protein == "Bridge"):
                                        if  dictgraph[line2[1]][0] == "D":
                                          dictint2.update({dictgraph[line2[1]]+" "+dictgraph[line2[2]]:"L-Bb"})
                                        elif dictgraph[line2[2]][0] == "D":
                                            dictint2.update({dictgraph[line2[2]]+" "+dictgraph[line2[1]]:"L-Bb"}) 
                                    elif (protein == "AlphaHelix" or protein == "310Helix"):
                                        if  dictgraph[line2[1]][0] == "D":
                                            dictint2.update({dictgraph[line2[1]]+" "+dictgraph[line2[2]]:"H-Bb"})
                                        elif dictgraph[line2[2]][0] == "D":
                                            dictint2.update({dictgraph[line2[2]]+" "+dictgraph[line2[1]]:"H-Bb"})
                                    elif (protein =="Strand"):
                                        if dictgraph[line2[1]][0] == "D": 
                                            dictint2.update({dictgraph[line2[1]]+" "+dictgraph[line2[2]]:"S-Bb"})
                                        elif dictgraph[line2[2]][0] == "D":
                                            dictint2.update({dictgraph[line2[2]]+" "+dictgraph[line2[1]]:"S-Bb"})
                            else:
                                continue
                            
            op.close()  


import itertools
m = list(itertools.product(listdna,listprotein)) #пишу все возможные сочетания днк и белков из pfam

set1 = set() #кажется, работает для 1crx.A_138-330.1crx.pdb1.pdb; 1crx.A_26-102.1crx.pdb1.pdb; 1crx.B_138-330.1crx.pdb1.pdb; 1crx.B_26-102.1crx.pdb1.pdb
set2 = set()

#'''Для каждого файла смотрим, есть ли связь ДНК-белок из pfam в наборе dictint и dictint2'''
#'''dictint - ДНК-белок из hbond''' словарь всех сочетаний днк-белок из hbond
#'''dictint2 - ДНК-белок из hydro''' словарь всех сочетаний днк-белок из hydrophobic
#эта часть кода должна писать все возможные сочетания белков из pfam и находить им соответствия в dictint и dictint2. Однако это не работает для 2zo2.B_422-590.2z02.pdb4.pdb, т.е. пишутся пустые множества






set3 = set()
set4 = set()
listpfam = []
listkeys = []
listkeys2 = []




#создается список цифра:номер для названия файла pfam



if countfile == 0:
    for i in range(int(file3pfam[0]),int(file3pfam[1])+1,1):
        listpfam.append(str(i)+":"+str(chainpfam2))
elif countfile == 1:
    for i in range(int(file3pfam[1]),int(file3pfam[2])+1,1):
        listpfam.append(str(i)+":"+str(chainpfam2))
elif countfile == 2: #два отрицательных числа
     for i in range(int(file4pfam[0]),int(file4pfam[1])+1,1):
        listpfam.append(str(i)+":"+str(chainpfam2))


for key in dictint.keys():  #эта цифра сравнивается со списком цифра:номер, который получается из dictint
         spl11 =  str(key).split(" ")[1] 
         spl21 = spl11.split(":")
         spl31 = spl21[0][3:]
         spl41 = spl21[1].split(".") 
         listkeys.append(str(spl31)+":"+str(spl41[0]))
         k1 = str(spl31)+":"+str(spl41[0])
         for j in range(len(sorted(listpfam))):
             if k1 == listpfam[j]:
                 set3.add(dictint[key])

for key2 in dictint2.keys(): #эта цифра сравнивается со списком цифра:номер, который получается из dictint2
         spl12 =  str(key2).split(" ")[1] 
         spl22 = spl12.split(":")
         spl32 = spl22[0][3:]
         spl42 = spl22[1].split(".")
         listkeys2.append(str(spl32)+":"+str(spl42[0]))
         k2 = str(spl32)+":"+str(spl42[0])
         for m in range(len(sorted(listpfam))):
             if k2 == listpfam[m]:
                 set4.add(dictint2[key2])

w = open("/home/nooroka/result_sqldatabase_updated.txt","a")
print(str(file)+" "+"union2"+" "+str(set3.union(set4))) #принтится верно, по порядку          

w.write(str(file)+"  "+str((set3.union(set4)))+"\n")
w.close()








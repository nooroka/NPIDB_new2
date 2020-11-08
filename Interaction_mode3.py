#!/usr/bin/env python
# coding: utf-8
import os
import sys
import subprocess
#os.chdir("/home/nooroka/pfam1/")
listtxt = []
opch = open("pfamcheck4.txt","r")
for file1 in opch:
#for file1 in os.listdir("."):
    file1 = file1.strip()
    listtxt.append(file1) #положила файлы из pfam в список
os.chdir("/home/nooroka/dna3")
#os.chdir("/home/npidb/data/pdb_new/dna")
listtxt2 = [] 
'''ниже - если файл днкшный, то добавляем в окончательный список'''
for filenew in listtxt:
    filenewsplit = filenew.split(".")
    if "pdb{}.pdb".format(filenewsplit[0]) in os.listdir("."): 
        listtxt2.append(filenew) 
os.chdir("/home/nooroka/")
print(sorted(listtxt2)) 
'''прохожу по файлам из pfam, выполняю второй скрипт'''
for file6 in sorted(listtxt2):
    command = ['python', 'Interaction_modemain.py', file6]
    process = subprocess.Popen(command)
    code = process.wait()

    #print(file6) #eсли тут print поставить, то один файл печатается
  #  program = "python"
  #  arguments = ["Interaction_modemain.py", file6]
  #  os.execvp(program, (program,) + tuple(arguments))
  #  print(file6)
 #   print("check")


#итог: останавливает проход по файлам именно os.execvp (выяснено по print("check"))

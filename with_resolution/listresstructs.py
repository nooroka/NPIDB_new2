#!/usr/bin/env python
#coding: utf-8
import os

from collections import defaultdict
dict1 = defaultdict(list)
listr = open("/home/nooroka/backupres02102020/res/listresstructs.txt","w")
ops = open("/home/nooroka/backupres02102020/result_sqldatabase_updated_new_sorted.txt","r")
for linek in ops:
    linek = linek.split()
    linekdot = linek[0].split(".")
    os.chdir("/home/npidb/data/pdb_new/dna")
    op = open("pdb{}.pdb".format(linekdot[0]),"r")
    for line2 in op:
      if "REMARK   2 RESOLUTION."  in line2:
            line2 = line2.strip()
            line2 = line2.split()
            if "NOT" not in line2 and "NULL" not in line2:
                key,value = linek[0],line2[3]
                print(str(linekdot[0])+str(line2[3]))
                dict1[key].append(value)

                if float(line2[3]) < 3.0:
                    listr.write(str(linek[0])+"\n")
#print(dict1)
listr.close()
                    


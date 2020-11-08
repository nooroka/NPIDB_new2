#!/usr/bin/env python
#coding: utf-8
import os
op = open("/home/nooroka/backupres02102020/b_pfam_struct_types2.txt","r")
listpdb = []
listxray = []
w2 = open("/home/nooroka/backupres02102020/res/xray.txt","w")
w3 = open("/home/nooroka/backupres02102020/res/electron.txt","w")
w4 = open("/home/nooroka/backupres02102020/res/nmr.txt","w")
countxray = 0 #количество структур с resolution
countel = 0
countnmr = 0
for line in op:
    if "INSERT INTO `b_pfam_struct_types` VALUES" in line:
         line = line.strip()
         line = line.split()
         lineintmode = line[4].split(",")
         os.chdir("/home/npidb/data/pdb_new/dna")          
         if os.path.exists("pdb{}.pdb".format(lineintmode[0][2:-1])): 
            os.chdir("/home/nooroka/backupres02102020/scripts")
            listpdb.append(lineintmode[0][2:-1])
op.close()
setpdb = set(listpdb)
listpdb2  = []
op2 = open("/home/nooroka/backupres02102020/res/resnmr_sorted.txt","r")
for line2 in op2:
    line2 = line2.strip()
    line2 = line2.split(" ")
    listpdb2.append(line2[0])
    if line2[0] in setpdb and 'X-RAY' in line2[1] and 'DIFFRACTION' in line2[2]:
       for item2 in line2:
           w2.write(''.join(map(str,item2))+" ")
       w2.write("\n")
       countxray+=1
    if line2[0] in setpdb and 'ELECTRON' in line2[1] and 'MICROSCOPY' in line2[2]:
       for item3 in line2:
           w3.write(''.join(map(str,item3))+" ")
       w3.write("\n")
       countel+=1
    if line2[0] in setpdb and 'SOLUTION' in line2[1] and 'NMR' in line2[2]:
       for item4 in line2:
           w4.write(''.join(map(str,item4))+" ")
       w4.write("\n")
       countnmr+=1

op2.close()
setpdb2 = set(listpdb2)
print(len(setpdb))
print(len(setpdb2))
print("countxray "+str(countxray))
print("countel "+str(countel))
print("countnmr "+str(countnmr))
#print(sorted(setpdb ^ setpdb2))
#print(sorted(setpdb2 - setpdb))
listpdbdiff = sorted(setpdb2 - setpdb)
w = open("/home/nooroka/backupres02102020/pdbcheck.txt","w")
for i in range(len(listpdbdiff)):
    os.chdir("/home/npidb/data/pdb_new/stride")
    if os.path.exists("{}.std.txt".format(listpdbdiff[i])):
        w.write("{}.std.txt".format(listpdbdiff[i])+"\n")
    else:
        w.write("no"+"\n")
w.close()
w2.close()
w3.close()
w4.close()

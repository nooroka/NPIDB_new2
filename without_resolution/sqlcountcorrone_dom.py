#!/usr/bin/env python
# coding: utf-8

from collections import defaultdict
op = open("/home/nooroka/backupnores02102020/uniprot/familiesend_red.txt","r")
op3 = open("/home/nooroka/backupnores02102020/domainsendcorr2rep_corr.txt","w")

data = defaultdict(list)
for line in op:
    line = line.strip()
    line = line.split("\t",1)
    if len(line) > 1: #печатаются с "\n", поэтому с одной длиной не бывает
        
        line[1] = line[1].strip() 
        line[1] = line[1].split()
        line[1] = sorted(line[1])
        key,value = ' '.join(map(str,line[1])),line[0]
        if value not in data[key]:
        #if value not in data[key] and str(value) in structsgood:            
            data[key].append(value)
    if len(line) == 1:
       data[" "].append(value)
       
     
#op2.write(str(data))
print(data)
for key in data:
    #op3.write(str(key)+"\t"+str(data[key])+"\n")
    op3.write(str(key)+"\t"+str(len(data[key]))+"\n")
op.close()
op3.close()

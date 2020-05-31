import os
op = open("interaction_mode_uncorr.txt","r")
op2 = open("interaction_mode_corr.txt","w")
list1 = []
list2 = []
dict1 = {}
dict2 = {}
for line in op:
    os.chdir("/home/npidb/data/pdb_new/dna/")
    line3 = line.split(".")
    if os.path.exists("pdb{}.pdb".format(line3[0])): 
        os.chdir("/home/nooroka")
        line = line.replace("|"," ")
        line = line.strip()
        line = line.split(" ",1)
        if len(line) > 1:
            line[1] = line[1].split()
            line[1] = sorted(line[1])
            list2.append(' '.join(map(str,line[1])))
            dict1[line[0]] = ' '.join(map(str, line[1]))
            op2.write(str(line[0])+"\t"+str(' '.join(map(str,line[1])))+'\n')
        else:
            dict1[line[0]] = " "
op.close()
op2.close()
#print(dict1)
op3 = open("result_sqldatabase.txt","r")
op4 = open("result_sqldatabase_corr.txt","w")
for line2 in op3:
    line2 = line2.strip()
    line2 = line2.split(" ",1)
    if len(line2) > 1:
        line2[1] = line2[1].split()
        line2[1] = sorted(line2[1])
        list1.append(' '.join(map(str,line2[1])))
        dict2[line2[0]] = ' '.join(map(str, line2[1]))
        op4.write(str(line2[0])+"\t"+str(' '.join(map(str,line2[1])))+'\n')
    else:
        dict2[line2[0]] = " "
op3.close()
op4.close()
#print(dict2)
countok = 0
countno = 0
for key in dict1:
    if dict1[key] == dict2[key]:
        countok+=1
    else:
        countno+=1

print("countok "+str(countok))
print("countno "+str(countno))


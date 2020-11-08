import os
op = open("/home/nooroka/backupres02102020/result_sqldatabase_updated_new_sorted.txt","r")
w = open("/home/nooroka/backupres02102020/structs_with_resolution.txt","w")
count = 0
list1 = []
for line in op:
    line = line.strip()
    linex = line.split(".")
    os.chdir("/home/npidb/data/pdb_new/dna")
    op2 = open("pdb{}.pdb".format(linex[0]),"r")
    for line2 in op2:
        if "REMARK   2 RESOLUTION."  in line2:
            line2 = line2.strip()
            line2 = line2.split()
            w.write(str(line)+" "+str(line2[3])+"\n")
            if line2[3]!="NOT" and line2[3]!="NULL":
                if float(line2[3]) >= 3.0:
                    count+=1
                    op6 = open("/home/nooroka/backupres02102020/res/xray.txt")
                    for line6 in op6:
                        line6 = line6.strip()
                        line6 = line6.split(" ",1)
                        if linex[0] in line6:
                           # if linex[0] not in list1:
                                line = line.split(" ",1)
                                list1.append(line[0])

                    op6.close()
    op2.close()
print(count)
print(list1)
print(len(list1))
w.close()
op.close()


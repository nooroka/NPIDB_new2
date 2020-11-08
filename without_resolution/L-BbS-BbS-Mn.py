op = open("/home/nooroka/backupnores02102020/result_sqldatabase_updated_new_sorted.txt")
count = 0
listun = []
for line in op:
    line = line.strip()
    line = line.split(" ",1)
    if len(line) > 1:
        if str(line[1]) == "L-Bb S-Bb S-Mn":
             count +=1
        op2 = open("/home/nooroka/backupnores02102020/uniprot/structsresold.txt")
        for line2 in op2:
            line2 = line2.strip()
            line2 = line2.split("\t")
            if str(line[0]) in str(line2[2]) and str(line[1]) == "L-Bb S-Bb S-Mn":
                listun.append(line2[0])

op.close()
print(count)
listunset = set(listun)
print(len(listunset))
print(listunset)

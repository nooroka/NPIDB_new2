count = 0
op = open("/home/nooroka/backupnores02102020/uniprot/familiesend_red.txt")
for line in op:
    line = line.strip()
    line = line.split("\t")
    if len(line) > 1:
        if line[1] ==  "H-Bb H-Mj H-Mn L-Bb L-Mj L-Mn S-Bb S-Mj S-Mn":
            op2 = open("/home/nooroka/backupnores02102020/uniprot/structsresold.txt")
            for line2 in op2:
                line2 = line2.strip()
                line2 = line2.split()
                if str(line2[0]) == str(line[0]):
                   print(str(line2[0]) + " "+str(line2[1]))
                   count += int(line2[1])
            op2.close()

op.close()
print(count)

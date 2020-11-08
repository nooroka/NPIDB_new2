from collections import defaultdict
#op = open("familiesendcorr2.txt","r")
op = open("/home/nooroka/backupres02102020/families/dictinter7.txt","r")
#op2 = open("familiesendcorrprom2.txt","w")
op3 = open("/home/nooroka/backupres02102020/familiesendcorr2rep_corr.txt","w")

data = defaultdict(list)
for line in op:
    line = line.strip()
    line = line.split("\t",1)
    if len(line) > 1:
        line[1] = line[1].strip() 
        line[1] = line[1].split()
        line[1] = sorted(line[1])
        key,value = ' '.join(map(str,line[1])),line[0]
        if value not in data[key]:                    
            data[key].append(value)
    if len(line) == 1:
        data[" "].append(value)

w = open("/home/nooroka/backupres02102020/data.txt","w")
w.write(str(data))
w.close()
for key in data:
    op3.write(str(key)+"\t"+str(len(data[key]))+"\n")
op.close()
op3.close()

from collections import defaultdict
op = open("/home/nooroka/backupnores02102020/result_sqldatabase_updated_new_sorted.txt","r")
op3 = open("/home/nooroka/backupnores02102020/structsendcorr2rep_corr.txt","w")
data = defaultdict(list)
for line in op:
    line = line.strip()
    line = line.split(" ",1)
    if len(line) > 1:
        line[1] = line[1].strip() 
        line[1] = line[1].split()
        line[1] = sorted(line[1])
        key,value = ' '.join(map(str,line[1])),line[0]
        if value not in data[key]:          
            data[key].append(value)
    if len(line) == 1:
       data[" "].append(value)
print(data)
for key in data:
    op3.write(str(key)+"\t"+str(len(data[key]))+"\n")
op.close()
op3.close()

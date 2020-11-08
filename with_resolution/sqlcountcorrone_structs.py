from collections import defaultdict
#op = open("familiesendcorr2.txt","r")
op = open("/home/nooroka/backupres02102020/result_sqldatabase_updated_new_sorted.txt","r")
#op2 = open("familiesendcorrprom2.txt","w")
op3 = open("/home/nooroka/backupres02102020/structsendcorr2rep_corr.txt","w")
'''
op5 = open("/home/nooroka/backupres02102020/structsgood.txt","r")
structsgood  = []
for line2 in op5:
    line2 = line2.strip()
    structsgood.append(str(line2))
op5.close()
'''
list1 = []
op5 = open("/home/nooroka/backupres02102020/res/listresstructs.txt","r")
for line in  op5:
    line = line.strip()
    line = line.split()
    list1.append(str(line[0]))
op5.close()
data = defaultdict(list)
for line in op:
    line = line.split(" ",1)
    if len(line) > 1:
        line[1] = line[1].strip() 
        line[1] = line[1].split()
        line[1] = sorted(line[1])
        key,value = ' '.join(map(str,line[1])),str(line[0])
        if str(value) not in data[key] and str(value) in list1:
           data[key].append(value)
    if len(line) == 1:
        if str(value) not in data[key] and str(value) in list1:
           data[" "].append(value)
print(data)
for key in data:
    op3.write(str(key)+"\t"+str(len(data[key]))+"\n")
op.close()
op3.close()

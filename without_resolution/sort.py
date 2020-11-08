op1 = open("/home/nooroka/backupnores02102020/result_sqldatabase_updated_new.txt","r")
op2 = open("/home/nooroka/backupnores02102020/result_sqldatabase_updated_new_sorted.txt","w")

for line in op1:
    line = line.replace("set([","")
    line = line.replace("'","")
    line = line.replace("])","")
    line = line.replace(",","")
    line = line.strip()
    line = line.split(" ",1)
    if len(line) > 1:
       line[1] = line[1].strip()
       line[1] = line[1].split()
       line[1] = sorted(line[1])      
       op2.write(str(line[0])+" "+" ".join(map(str,line[1]))+"\n")
    else:
       op2.write(str(line[0])+" "+"\n")
op1.close()
op2.close()

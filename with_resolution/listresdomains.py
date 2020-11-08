op = open("/home/nooroka/backupres02102020/res/reschern.txt","r")
opw = open("/home/nooroka/backupres02102020/res/listresdomains.txt","w")
for line in op:
    line = line.strip()
    line = line.split()
    #if line[2]!="NOT" and line[2]!="NULL":
    if float(line[2]) < 3.0:
        opw.write(str(line[0])+"\n")
op.close()
opw.close()


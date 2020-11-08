import subprocess
listint = []
setint = set()
op3 = open("/home/nooroka/backupnores02102020/families/dictinter7.txt")
for line3 in op3:
    line3 = line3.strip()
    line3 = line3.split("\t")
    if len(line3) > 1:
        setint.add(line3[1])
setint.add(" ")
print(setint)

for item in setint:
   process3 = subprocess.Popen(["python", "tablestructs.py", item], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
   data3,data33 = process3.communicate()
   with open('/home/nooroka/backupnores02102020/result_table.txt', 'a') as f:
       f.write(data3)
   #with open('result_err.txt', 'a') as f:
    #   f.write(data33)




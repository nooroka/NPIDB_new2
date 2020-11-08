import subprocess
listint = []
setint = set()
op3 = open("/home/nooroka/backupres02102020/result_sqldatabase_updated_new_sorted.txt")
for line3 in op3:
    line3 = line3.strip()
    line3 = line3.split(" ",1)
    if len(line3) > 1:
        setint.add(line3[1])
setint.add(" ")
print(setint)
for item in setint:
   process3 = subprocess.Popen(["python", "tablestructs2.py", item], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
   data3,data33 = process3.communicate()
   with open('/home/nooroka/backupres02102020/result_table2.txt', 'a') as f:
       f.write(data3)
   with open('/home/nooroka/backupres02102020/result_err2.txt', 'a') as f:
       f.write(data33)



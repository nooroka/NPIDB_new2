import subprocess
listint = []
setint = set()
op3 = open("result_sqldatabase_updated_sorted.txt")
for line3 in op3:
    line3 = line3.strip()
    line3 = line3.split(" ",1)
    if len(line3) > 1:
        setint.add(line3[1])
setint.add(" ")
print(setint)
for item in setint:
   process3 = subprocess.Popen(["python", "tablestructs2empty.py", item], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
   data3,data33 = process3.communicate()
   with open('result_table2empty.txt', 'a') as f:
       f.write(data3)
   with open('result_err2empty.txt', 'a') as f:
       f.write(data33)



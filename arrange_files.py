import os
import shutil
import time
files =[]
avilable_extension=[]
cwd = os.getcwd()
print(os.listdir())
new = cwd + "\Raw Files"
os.chdir(new)
cwd = os.getcwd()
print(cwd)

print(os.listdir())
for f in os.listdir() :
    files.append(f)
print(files)
for ex in files:
    exte=ex.split('.')[1]
    avilable_extension.append(exte)
print(avilable_extension)
print(cwd)
cwd=cwd.split("Raw Files")[0]
os.chdir(cwd)
avilable_extension=set(avilable_extension)
print(avilable_extension)

for x in avilable_extension:
    os.mkdir(x)
    for ex in files:
        exte=ex.split('.')[1]
        if exte == x:
            shutil.move('D:/Python Programs/Task2/Raw Files/' + ex ,'D:/Python Programs/Task2/' + x)

    
# os.mkdir("testing")
# time.sleep(5)
# for x in avilable_extension:
#     os.rmdir(x)

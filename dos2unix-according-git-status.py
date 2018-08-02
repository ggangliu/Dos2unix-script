import os

#os.system(r"git status > git-status-file-list")
print("\n"+23*"*"+"Files list"+23*"*")
with open("git-status-file-list", "r") as f:
    for line in f.readlines():
        if "new file:" in line or "modified:" in line:
            print(line.lstrip()[0:-1])
print("\n"+23*"*"+"Converting files"+23*"*")
with open("git-status-file-list", "r") as f:
    for line in f.readlines():
        if "new file:" in line or "modified:" in line:
            parts = line.split(':')
            os.system("dos2unix " + parts[1][0:-1])

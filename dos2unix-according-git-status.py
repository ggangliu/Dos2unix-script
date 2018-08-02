import os

#os.system(r"git status > git-status-file-list")
with open("git-status-file-list", "r") as f:
    for line in f.readlines():
        if "new file:" in line or "modified:" in line:
            parts = line.split(':')
            #print(parts[0].lstrip() + parts[1][0:-1])
            os.system("dos2unix " + parts[1][0:-1])

import subprocess
import os

select=input("enter dir\n")
path = select
os.chdir(path)

stop=0
while(stop==0):
    gitStop=0
    select = input("command now\n")
    if (select=="build"):
        subprocess.call('pyb_', shell=True)
    elif (select=="quality"):
        select = input("file to quality check\n")
        subprocess.call(['pylint', 'src/main/python/'+select], shell=True)
    elif (select=="test"):
        select=input("unit test file\n")
        subprocess.call(['python', 'src/unittest/python/'+select], shell=True)
    elif (select=="git"):
        while(gitStop==0):
            select=input("git command\n")
            if(select=="commit"):
                select=input("message\n")
                subprocess.call(['git', 'commit', '-m', select], shell=True)
            elif(select=="add"):
                select=input("dir/ file to add\n")
                subprocess.call(['git', 'add', select], shell=True)
            elif(select=="push"):
                subprocess.call(['git', 'push'], shell=True)
            elif(select=="clone"):
                select=input("url\n")
                subprocess.call(['git', 'clone', select], shell=True)
            elif(select=="checkout"):
                select=input("branch\n")
                subprocess.call(['git', 'checkout', select], shell=True)
            elif(select=="quit"):
                gitStop=1
    elif (select=="dir"):
        select=input("new dir\n")
        os.chdir(select)
        path = select
    elif (select=="quit"):
        stop=1

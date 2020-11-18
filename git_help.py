"""
First steps:
    - set identity:
    git config --global user.name "John Doe"
    git config --global user.email johndoe@example.com

    - select code editor : (optional) # https://git-scm.com/book/en/v2/ch00/ch_core_editor
    git config --global core.editor "code --wait"

    -set default branch name:
    git config --global init.defaultBranch main   # from 2.28 initial branch can have a different name then main

    -check configuration settings:
    git config --list


git init                                                           // start tracking current directory
git add -A                                                         // add all files in current directory to staging
                                                                    area, making them available for commit
git commit -m "commit message"                                     // commit your changes
git remote add origin https://github.com/username/repo-name.git    // add remote repository URL which contains the
                                                                    required details
git pull origin master                                             // always pull from remote before pushing
git push -u origin master                                          // publish changes to your remote repository


git commit -am "message":  is same to git add -A followed by git commit -m "message
git push -u remote master
git pull remote master
"""

""" cmd /c and terminate or cmd /k and remain

import os
import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300, bg='gray90', relief='raised')
canvas1.pack()


def myCmd():
    os.system('cmd /c "git status"')
    os.system('cmd /c "git add -A"')
    os.system('cmd /c "git commit -m \'message\'"')
    os.system('cmd /c "git pull origin master"')
    os.system('cmd /c "git push -u origin master"')


button1 = tk.Button(text='      Run Command      ', command=myCmd, bg='green', fg='white',
    font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=button1)

root.mainloop()


"""

import os
import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300, bg='gray90', relief='raised')
canvas1.pack()


def myCmd():
    os.system('cmd /c "cd C:\PROGRAMS\Exercises\PrivatePython"')
    os.system('cmd /c "git add -A"')
    os.system('cmd /c "git commit m \"Update From git_help\""')
    os.system('cmd /c "git pull origin master"')
    os.system('cmd /c "git push -u origin master"')


button1 = tk.Button(text='      Run Command      ', command=myCmd, bg='green', fg='white',
                    font=('helvetica', 12, 'bold'))

canvas1.create_window(150, 150, window=button1)

if __name__ == '__main__':
    root.mainloop()

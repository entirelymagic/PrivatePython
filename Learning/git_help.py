"""
First step:
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

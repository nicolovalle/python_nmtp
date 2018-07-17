#!/bin/bash

git add $1
echo ---------- $1 ADDED ------------
if [ -z "$2" ]; then
    git commit -m \"$1\"
    echo ------- COMMITTED WITH DEFAULT COMMENT --------
else
    git commit -m $2
    echo ------- COMMITTED -----------   
fi
git pull --rebase
git push -u origin master
echo ------- DONE https://github.com/nicolovalle/python_nmtp ---------

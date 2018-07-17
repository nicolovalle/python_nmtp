#!/bin/bash

git add $1
echo ---------- $1 ADDED ------------
if [ -z "$2" ]; then
    git commit -m "..."
    echo ------- COMMITTED WITH DEFAULT COMMENT --------
else
    git commit -m $2
    echo ------- COMMITTED -----------   
fi
git pull --rebase
echo ------- REBASE DONE ---------
git push -u origin master
echo ------- PUSHED ORIGIN -> MASTER ---------

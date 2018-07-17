#!/bin/bash

git add $1
if [ -z "$2"]
then
    git commit -m $2
else
    git commit -m "No comment added"
fi
git pull --rebase
git push -u origin master

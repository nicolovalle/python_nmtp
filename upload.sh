#!/bin/bash

git add $1
git commit -m $2
git pull --rebase
git push -u origin master

#!/bin/bash

if [ -z $1 ];then
    echo
    echo This program needs argument. Please use in this way:
    echo $'\t' ./upload.sh miofile.py [\"Comment...\"]
    echo $'\t' ./upload.sh mia_directory [\"Comment...\"]
    echo
else
    git add $1
    echo --------------- $1 ADDED ------------------
    if [ -z "$2" ]; then
	git commit -m $1
	echo ---------- COMMITTED WITH DEFAULT COMMENT --------
    else
	git commit -m $2
	echo ----------------- COMMITTED ----------------------   
    fi
    git pull --rebase
    git push -u origin master
    echo ------- DONE https://github.com/nicolovalle/python_nmtp ---------
fi


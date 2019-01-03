#!/bin/bash
#update daily
#Author: Solomon Amos

cd ~/projects/LearnAlgorithm
git init
git add .
git commit -m "update Today's code)"
#git remote add origin https://github.com/udohsolomon/LearnPython_Class.git
git push -u origin master
git config credential.helper store
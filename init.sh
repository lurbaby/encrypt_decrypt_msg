#!/bin/bash

echo "# bbs_generator" >> README.md
git init
git add README.md
git add .
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:lurbaby/bbs_generator.git
git push -u origin main
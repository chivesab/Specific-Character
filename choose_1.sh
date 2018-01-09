#!bin/bash

while getopts "m:d:" option;
do
     case "${option}"
     in
     m) month=${OPTARG};;
     d) duplicate=${OPTARG};;
     esac
done
python choose_1.py ${month} ${duplicate}
sudo chmod 777 ./*

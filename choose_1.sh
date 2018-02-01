#!/bin/bash
start_time=$(date +%s.%N)
while getopts "m:d:" option;
do
     case "${option}"
     in
     m) month=${OPTARG};;
     d) duplicate=${OPTARG};;
     esac
done
python choose_1.py ${month} ${duplicate}
end=$(date +%s.%N)
runtime=$(python -c "print(${end}-${start_time})")
echo "Runtime was $runtime"

echo "month= ${month}">>record_file.txt
echo "duplicate= ${duplicate}">>record_file.txt
echo "Runtime = $runtime " >> record_file.txt




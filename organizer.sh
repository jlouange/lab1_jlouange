#!/usr/bin/env bash
if [ ! -d archive ];then
    mkdir archive
fi

timestamp=$( date +"%Y%m%d-%H%M%S")  
new_name="grades_${timestamp}.csv"

if [ ! -f grades.csv ]
then
    echo "grades.csv not found."
    exit 1
fi

mv "grades.csv" "archive/$new_name"
echo "$timestamp | grades.csv --> $new_name" >> organizer.log
touch grades.csv


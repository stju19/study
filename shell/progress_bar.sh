#!/bin/bash

set +x
b=''
i=0
while [ $i -le  100 ]
do
    printf "progress:[%-50s]%d%%\r" $b $i
    sleep 0.1
    i=`expr 2 + $i`       
    b=#$b
done
echo

i=0
while [ $i -lt 100 ]
do
    for j in '-' '\' '|' '/'
    do
        printf "testing : %s\r" $j
        sleep 0.1
        ((i++))
    done
done
echo

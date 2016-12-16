#! /bin/bash

trap "exec 6>&-;exec 6<&-;exit 0;" 2

mkfifo testfifo
exec 6<>testfifo
rm -rf testfifo

for ((n=1;n<=10;n++))
do
    echo >&6
done

start=`date "+%s"`

for ((i=1;i<=100;i++))
do
    read -u6
    {
        sleep_num=`expr $RANDOM % 10`
        echo "success $i, sleep $sleep_num s"
        sleep $sleep_num
        echo >&6
    }&
done

wait

end=`date "+%s"`
echo "Time: `expr $end - $start`"

exec 6>&-
exec 6<&-


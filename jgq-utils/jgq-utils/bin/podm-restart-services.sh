#! /bin/bash

delay=0
while getopts 'd:' OPT
do
    case "$OPT" in
     d)
     delay=$OPTARG;;
     ?)
     exit 1;;
    esac
done

echo "service will be restart after $delay seconds"
sleep $delay
echo "restarting ..."
systemctl restart podm-scheduler podm-concrete podm-versioner podm-alarm podm-alarmagent podm-api

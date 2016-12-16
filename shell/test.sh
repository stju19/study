#! /bin/bash

function bbb
{
    echo
}

function aaa
{
    bbb 
    echo "byebye!"
}

echo "pro 1"
trap "aaa;exit" SIGINT
sleep 5

echo "pro 2"
trap - SIGINT
sleep 5
echo ok

#! /bin/bash

file=/etc/profile.d/set_proxy.sh

function auto_get_remote_ip
{
    remote_ip=`who | awk -F "[()]" '{print $2}' | sort | uniq -c | sort -r | sed -n '1p' | awk -F ' ' '{print $2}'`
}

function make_set_proxy
{
    ip=$1
    cat > $file <<EOF
export jgq_ip=$ip
export active_proxy=\$jgq_ip
export http_proxy=http://\$active_proxy:808
export https_proxy=https://\$active_proxy:808
export ftp_proxy=ftp://\$active_proxy:808
export socks_proxy=socks://\$active_proxy:1080
export all_proxy=socks://\$active_proxy:1080
#export no_proxy="localhost, 10.43.211.62"
EOF
}

if [ "$1" = "" ]; then
    auto_get_remote_ip
    make_set_proxy $remote_ip
    source $file
    rm -rf $file
elif [ "$1" == "-d" ]; then
    rm -rf $file
    unset remote_ip
    unset jgq_ip
    unset active_proxy
    unset http_proxy
    unset https_proxy
    unset ftp_proxy
    unset socks_proxy
    unset all_proxy
    unset no_proxy
else
    make_set_proxy $1
    source $file
    rm -rf $file
fi

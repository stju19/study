#! /bin/bash

PWD=$(cd $(dirname $0); pwd)
ztes_project_root=/home/jgq/Uniview/vDirector/ztes
ci_path=$ztes_project_root/build/ci
ci_script=./checkin_test.sh

[[ "$#" -eq 0 ]] && para="firmware 0" || para="$@"
cd $ci_path
$ci_script $para

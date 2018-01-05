#!/bin/bash

PWD=$(cd $(dirname $0); pwd)
ztes_project_root=/home/jgq/Uniview/vDirector/ztes

function help
{
    echo "Usage: Uniview-test-console <service_name>"
    echo
}

function get_scala_lib
{
    local scala_bin=$(which scala)
    scala_lib=${scala_bin%/bin/scala}/lib
}

[[ $# -eq 1 ]] || {
    echo "Error:service_name is missing"
    help
    exit 1
}

service_name=$1
cd $ztes_project_root/$service_name || { echo "$ztes_project_root/$service_name is bot exist" exit 1; }
gradle testClasses || exit 1

base_test_classpath=$(gradle -i sTC 2>/dev/null | grep classpath | awk '{print $12}')
get_scala_lib
scala_lib_jar=$(echo $scala_lib/{jline.jar,scala-compiler.jar})
scala_classpath=${scala_lib_jar//[[:space:]]/:}
test_console_classpath_str="-classpath $base_test_classpath:$scala_classpath"

trap "reset;exit" INT EXIT
java -Dscala.usejavacp=true $test_console_classpath_str -Dfile.encoding=UTF-8 scala.tools.nsc.MainGenericRunner

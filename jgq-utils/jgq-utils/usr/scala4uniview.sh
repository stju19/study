#!/bin/bash

uniview_classpath=/home/jgq/lib/uniview
uniview_depend_classpath=/home/jgq/lib/depend
[[ -d $uniview_classpath ]] || { echo "scala classpath directory $uniview_classpath is not exist"; exit 1; }
[[ -d $uniview_depend_classpath ]] || { echo "scala classpath directory $uniview_depend_classpath is not exist"; exit 1; }

if [[ $# -eq 0 ]]; then
    depend_classpath=$(ls $uniview_depend_classpath/*)
    uniview_classpath=$(ls $uniview_classpath/*)
    total_classpath="$uniview_classpath $depend_classpath"
    env_classpath_str="-classpath ${total_classpath//[[:space:]]/:}"
fi

scala $env_classpath_str $@

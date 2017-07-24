#!/bin/bash

uniview_classpath=/home/jgq/lib/uniview
[[ -d $uniview_classpath ]] || { echo "scala classpath directory /home/jgq/lib/uniview is not exist"; exit 1; }

if [[ $# -eq 0 ]]; then
    env_classpath_str="-classpath "

    for i in $(ls $uniview_classpath/*)
    do
        env_classpath_str=$env_classpath_str:$i
    done
fi

scala $env_classpath_str $@

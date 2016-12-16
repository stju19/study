#!/bin/bash

_FUNCTION_LIB_DIR=`pwd`
cd $_FUNCTION_LIB_DIR/
.  ./function_lib.sh

read -p "enter a number:" num
square num
ans=$?
echo the square of $num is $ans
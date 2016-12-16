#! /bin/bash

_FUNCTION_LIB_DIR=`pwd`
cd $_FUNCTION_LIB_DIR
.  ./function_lib.sh

echo `accumulator $1`
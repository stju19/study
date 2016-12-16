#! /bin/bash
#函数库
#if [ ! "$_FUNCTION_LIB_FILE" ]; then

function square
{
	#declare -i num
	#declare -i ans="$num * $num"
	return $(($1 * $1))
}

function reply
{
	read -p "Please input (Y/N): " yn
	if [ "$yn" == "Y" ] || [ "$yn" == "y" ]; then
		echo "OK, continue"
	elif [ "$yn" == "N" ] || [ "$yn" == "n" ]; then
		echo "Oh, interrupt!"
	else
		echo "I don't know what your choice is"
	fi
}

function accumulator
{
	s=0
	i=0

	if [ $1 -lt 10 ]; then
		echo "error: the apartment must be greater than 5!"
		exit 1
	fi

	while [ $i != $1 ]
	do
		i=$(($i+1))
		s=$(($i+$s))
	done

	echo "the result of '1+2+3+...+$1' is: $s"
}

#_FUNCTION_LIB_FILE="function_lib.sh"
#fi
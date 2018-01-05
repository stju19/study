#! /bin/bash


# function foo
# {
#     local num=$1
#     echo "job$num start"
#     sleep $num
#     echo "job$num end"
# }

# function calc_time
# {
#     if [ "$DEBUG" = "true" ]; then
#         time $@
#         echo [DEBUG] $@
#     else
#         $@
#     fi
# }

# # DEBUG=true
# # calc_time foo 5 0 && echo success5 &
# # calc_time foo 3 1 && echo success3 &
# # wait

# echo $0

para="$@"
str=
for i in "$@"
do
    if [[ "$i" = "" ]];then
        str="$str \"\""
    else {
        echo "$i" | grep " " &>/dev/null && str="$str \"$i\"" || str="$str $i"
    }
    fi
done
echo "$str"

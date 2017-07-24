#! /bin/bash

configure_file='/tmp/jgq-docker.conf'
container_on0_ip=138.1.1.3
container_on1_ip=138.1.1.20

function get_value
{
    key=$1
    value=""
    [[ `cat $configure_file |grep "^[[:space:]]*\"$key\""|wc -l` != "1" ]] && { echo "none or more than one $key in $configure_file!";return 1; }

    local line_info=`sed -n "/^[[:space:]]*\"$key\"/p" $configure_file`
    line_info=${line_info%%\#*}
    local key=${line_info#*\:}
    _key=${key#*\"}
    _key_=${_key%\"*}
    value=$_key_

    return 0
}

function show_configure_file_template
{
    local image_id=`docker images|grep -w jgq-docker|awk '{print $3}'`
    [[ "$image_id" = "" ]] && image_id=IMAGEID
    echo "configure file $configure_file maybe like:"
    cat <<EOF
{
  "docker_image":"$image_id"
  "container_name": "jgq-docker"
  "cmd": "-c /bin/sh"
  "run_opts": "--privileged -p 5080:80 -p 5022:22 -p 5336:3306 -v /home/jgq:/home/jgq"
  "exec_create_cmd": "sh /root/create.sh"
  "exec_start_cmd": "sh /root/start.sh"
  "ovs": "ovs-br0-$user_name $container_on0_ip/24"
  "ovs": "ovs-br1-$user_name $container_on1_ip/24"
}
EOF
}

function init
{
    [[ -f "$configure_file" ]] || { echo "$configure_file is not existed";show_configure_file_template;exit 1; }
    get_value container_name && container=$value
}

function show_help
{
    echo "Usage: jgq-docker COMMAND"
    echo "  command for container \"podm\":"
    echo "    create    create docker container"
    echo "    start     start docker container"
    echo "    stop      stop docker container"
    echo "    restart   restart docker container"
    echo "    enter     enter docker container"
    echo "    rm        remove docker container"
    echo
    echo "  command for image \"podm-docker\":"
    #echo "    load      load docker image podm-docker"
    #echo "    rmi       remove docker image podm-docker"
    echo
    show_configure_file_template
}

function main
{
    case "$1" in
        create)
            docker-manage create $configure_file
            ;;
        start)
            docker-manage start $container
            ;;
        stop)
            docker-manage stop $container
            ;;
        restart)
            docker-manage stop $container
            docker-manage start $container
            ;;
        rm)
            docker-manage rm $container
            ;;
        enter)
            docker-manage enter $container
            ;;
        load)
            echo "Not Implement"
            ;;
        rmi)
            echo "Not Implement"
            ;;
        "--help" | "-h" | "")
            show_help
            ;;
        *)
            echo "unknown command: $1"
            show_help
            ;;
    esac
}

init
main $@
exit 0

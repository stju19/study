#! /bin/bash

PWD=$(cd $(dirname $0); pwd)
# user define
ztes_project_root=/home/jgq/Uniview/vDirector/ztes
debug_port=11001

service_running_machine=10.43.167.125
password=ossdbg1
service_installed_path=/home/zte
debug_jvm_opt=

function show_help
{
    me="$(basename "$(test -L "$0" && readlink "$0" || echo "$0")")"
    echo "Usage: $me [service]"
    echo "       service: name of subproject under project UniView"
    echo
    # echo "while first use, please run command \"$me init\""
}

function ssh_init
{
    ssh-copy-id -i /root/.ssh/id_rsa.pub $service_running_machine
}

function parse_args
{
    local optlist="$@"
    while true
    do
        case "$1" in
            "--debug"|"-d")
                debug_jvm_opt="-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=$debug_port"
                shift
                ;;
            *)
                break
                ;;
        esac
    done

    [[ $# -gt 1 ]] && { show_help; exit 1; }

    case $1 in
        "init")
            ssh_init
            exit 0
            ;;
        "--help"|"-h")
            show_help
            exit 0
            ;;
        *) ;;
    esac

    if [[ "$1" = "" ]]; then
        service_name=$(basename `pwd`)
    else
        service_name=$1
    fi
    [[ "$service_name" = "uniView" ]] && service_name=hwm
    [[ "$service_name" = hwm ]] && compile_path=$ztes_project_root/uniView || compile_path=$ztes_project_root/$service_name
    [[ -d "$compile_path" ]] || { echo "Failed to get service $service_name, please check project path $ztes_project_root"; exit 1; }
}

function complie_service
{
    cd $compile_path
    echo "Compiling subproject repo; gralde war ... "
    gradle war || { echo "compile failed!"; return 1; }
    target_file=$(ls $compile_path/build/libs/$service_name*war 2>/dev/null)
    [[ "$target_file" = "" ]] && { echo "compile failed!"; return 1; }
    cd ->/dev/null
}

function update_service
{
    [[ "$target_file" = "" ]] && { echo "Failed to get warball achieve, stop to update service!"; return 1; }
    local service_path=$service_installed_path/zte/$service_name
    local service_file=$(ssh $service_running_machine "cd $service_path;ls $service_name*war 2>/dev/null")
    ssh $service_running_machine "cd $service_path; /usr/bin/mv -f $service_file $service_file.bak"
    scp $target_file $service_running_machine:$service_path/$service_file

    service_pid=$(ssh $service_running_machine "ps -ef|grep 'java -jar.*$service_name.*war'|grep -v grep|awk '{print \$2}'")
    echo "service $service_name pid: $service_pid"
    echo "killing process $service_name ... "
    [[ "$service_pid" != "" ]] && ssh $service_running_machine "kill -9 $service_pid"
    echo "start new process: java -jar $service_file"
    ssh $service_running_machine "cd $service_path; source /etc/profile;java -jar $debug_jvm_opt $service_file &" &>/dev/null &
    sleep 2
    kill -9 "$!" &>/dev/null
    echo "update service $service_name to $service_running_machine finished."
}

parse_args $@
complie_service || { echo "compile failed!"; exit 1; }
update_service || exit 1

#检测rpm包是否安装，使用该函数后，检测has_installed是否为yes
function check_installed
{
    has_installed="no"
    
    rpm -qi $1 &>/dev/null
    
    if [ 0 == $? ];then
        has_installed="yes"
    fi    
}
# 检查rpm包是否被依赖
function check_depend
{
    local rpm_name=$1
    # 检测依赖包是否被别人使用
    rpm -q --whatrequires $rpm_name &>/dev/null
    # 当查询不到被依赖的关系或rpm未安装，返回的是1，否则为0
    return "$?"
}

function get_config
{
    local file=$1
    local key=$2
     
    [ ! -e $file ] && return

    # 忽略井号开头的注释行以及空行之后，再grep过滤"key"所在的行 
    local line=`sed '/^[[:space:]]*#/d' $file | sed /^[[:space:]]*$/d | grep -w "$key"| grep "$key[[:space:]]*=" -m1`
    if [ -z "$line" ]; then
        config_answer=""
    else
        # 将第一个=号替换为空格，再删除第一个单词得到value
        config_answer=`echo $line | sed 's/=/ /' | sed -e 's/^\w*\ *//'`
    fi
}
function is_services_exist_in_os
{
    local services="$1"
    local component="$2"
    
    local is_local_exist=
    local is_remote_exist=
    local service=
    local remote_ip=
    local ssh_result=
    for service in $services
    do
        local service=`echo $service|awk -F '.' '{print $1}'`
        is_local_exist=`ls $systemd_service_path |grep -w "${service}.service$"`
        [ -z $is_local_exist ] && is_local_exist=`ls $lsb_service_path |grep -w "${service}$"`
        [ -z $is_local_exist ] &&  \
        { write_log "\"$service\" is not installed on local host, which is configed in $ha_conf_name"; exit 1; }
        for remote_ip in $remote_host_ip
        do
            ssh_cmd "$remote_ip" "ls $systemd_service_path |grep -w "${service}.service" &>/dev/null"
            ssh_result=$?
            if [ $ssh_result -ne 0 ];then
                ssh_cmd "$remote_ip" "ls $lsb_service_path |grep -w "${service}" &>/dev/null"
                ssh_result=$?
            fi
            [ $ssh_result -ne 0 ] && \
            { write_log "\"$service\" is not installed on $remote_ip, which is configed in $ha_conf_name"; exit 1; }
        done
    done
}
function get_value
{
    local file=$1
    local key=$2
    local allow_null=$3
    
    get_config $file "$key"
    config_answer=`echo "$config_answer"| grep -o "[^ ]\+\( \+[^ ]\+\)*"`
    if [ $allow_null = "no" ];then
       [ -z "$config_answer" ] && { write_log "can not get value of \"$key\" in $file"; exit 1; }
    fi
}
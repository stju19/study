#! /bin/bash

user_name=jgq
container_name=$user_name-image
jgq_base_conf=/tmp/jgq-base.conf
repo_file=/tmp/jgq.repo
container_on0_ip=138.1.1.20
PWD=$(cd $(dirname $0); pwd)

function err_clean
{
    docker-manage rm $container_name
    rm -rf $jgq_base_conf
    exit 1
}

function run
{
    docker exec -i --privileged "$1" bash -c "$2"
}

function check_depend
{
    rpm -q docker-manage &>/dev/null || { echo "error: docker-manage is not installed"; return 1; }
    docker inspect jgq-base:1 &>/dev/null || { echo "error: image jgq-base:1 is not exist"; return 1; }
    docker inspect $container_name &>/dev/null && { echo "error: container $container_name is already existed"; return 1; }
    echo "check depend all right"
}

function is_user_image_exist
{
    docker images|grep -qw $user_name-docker && return 0 || return 1
}

function make_user_image
{
    cat >$jgq_base_conf <<EOF
{
  "docker_image":"jgq-base:1"
  "container_name": "$container_name"
  "cmd": "/bin/sh"
  "run_opts":" --privileged --entrypoint=/sbin/init"
  "ovs": "ovs-$user_name-image $container_on0_ip/24"
}
EOF
    docker-manage create $jgq_base_conf
    rm -rf $jgq_base_conf

    cat >/tmp/pip.tmp <<EOF
[global]
trusted-host = 10.43.211.43
find-links = http://10.43.211.43/podm_install
no-index = true
EOF
    run $container_name "mkdir -p /root/.pip"
    docker cp /tmp/pip.tmp $container_name:/root/.pip/pip.conf
    rm -rf /tmp/pip.tmp

    cat >create.sh <<EOF
#! /bin/bash
sed -i '/gerrit.zte.com.cn/d' /etc/hosts
echo '10.41.124.11   gerrit.zte.com.cn' >> /etc/hosts
EOF
    chmod 755 create.sh
    docker cp create.sh $container_name:/root/create.sh
    rm -rf create.sh

    # user required rpms
    run $container_name "yum -y install git git-review dos2unix tree yum-utils"
    run $container_name "pip install pep8 flake8"

    # repair lack of locale
    run $container_name "mkdir -p /home/glibc"
    run $container_name "cd /home/glibc; yumdownloader glibc glibc-common"
    run $container_name "cd /home/glibc; rpm -Uvh --oldpackage glibc-*.x86_64.rpm"
    run $container_name "rm -rf /home/glibc"
    run $container_name "echo 'LANG=\"en_US.UTF-8\"' >> /etc/locale.conf"

    user_define_func
    commit_image
}

function commit_image
{
    local date_tag=$(date '+%Y.%m.%d')
    echo "docker commit $container_name $user_name-docker:$date_tag ..."
    docker commit -m "$user_name working docker" $container_name $user_name-docker:$date_tag || { echo "docker commit $container_name err!"; return 1;}
    docker-manage rm $container_name
}

function user_define_func
{
    # jgq utils rpms
    run $container_name "yum -y install pandoc jgq-utils"

    # jgq settings
    run $container_name "pcs cluster destroy --all"
    run $container_name "pcs cluster setup --start --enable --name jgq_work node1,$container_on0_ip"
    run $container_name "pcs resource group add podm-float-ip"
    run $container_name "pcs resource create North_float_ip ocf:heartbeat:IPaddr2 ip= nic=on0:0 cidr_netmask=24 --group podm-float-ip"
    run $container_name "pcs resource"
    sleep 10

    run $container_name "podm-stop-services"
    run $container_name "podm-link"
    run $container_name "sed -i '/keystone_admin/s/#source/source/g' /etc/profile.d/podm.sh"
    docker cp $PWD/../etc/delek_jgq.vim $container_name:/usr/share/vim/vim74/colors/delek_jgq.vim
    cat >vimrc.tmp <<EOF
syntax on
set t_Co=256
set hlsearch
set shiftwidth=4
syntax enable
set ts=4
set expandtab
set background=light
colorscheme delek_jgq
EOF
    docker cp vimrc.tmp $container_name:/root/.vimrc
    rm -rf vimrc.tmp
}

function create_working_container
{
    local image_id=$(docker images|grep -w "$user_name-docker"|sed -n 1p|awk '{print $3}')
    [[ "$image_id" = "" ]] && image_id=IMAGEID
    local create_file=/tmp/$user_name-docker.conf
    cat >$create_file <<EOF
{
  "docker_image":"$image_id"
  "container_name": "$user_name-docker"
  "cmd": "-c /bin/sh"
  "run_opts": "--privileged -p 5080:80 -p 5022:22 -p 5336:3306 -v /home/jgq:/home/jgq"
  "exec_create_cmd": "sh /root/create.sh"
  "ovs": "ovs-$user_name 138.1.1.20/24"
}
EOF
    docker-manage create $create_file
    local port=$(grep run_opts $create_file|grep -o '[[:digit:]]*:22'|awk -F: '{print $1}')
    [[ "$?" -eq 0 ]] && echo "please use ssh on port $port to connect your new container"
    return
}

function main
{
    check_depend || exit 1
    is_user_image_exist || make_user_image
    create_working_container
}

main
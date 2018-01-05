#! /bin/bash

PWD=$(cd $(dirname $0); pwd)
podm_path=/home/jgq/ZXOCSA/podm
container_name=jgq-image
repo_file=/tmp/jgq.repo
app_base_conf=/tmp/app-base.conf
container_on0_ip=138.1.1.3
nameserver=10.41.132.9
yum_repo="http://10.43.167.125/podm_install/"

function err_clean
{
    docker-manage rm $container_name
    rm -rf $repo_file
    rm -rf $app_base_conf
    exit 1
}

function run
{
    docker exec -i --privileged "$1" bash -c "$2"
}

function check_depend
{
    rpm -q docker-manage &>/dev/null || { echo "error: docker-manage is not installed"; return 1; }
    docker inspect app-base:1 &>/dev/null || { echo "error: image app-base:1 is not exist"; return 1; }
    docker inspect $container_name &>/dev/null && { echo "error: container $container_name is already existed"; return 1; }
    echo "check depend all right"
}

function make_bin
{
    cd $podm_path/make
    local current_branch=$(git branch|grep \*|awk '{print $2}')

    git stash &>/dev/null
    git checkout origin/HEAD &>/dev/null
    make podm
    make podmclient
    make dashboard
    make bin
    git checkout $current_branch &>/dev/null
    git stash pop &>/dev/null
    cd ->/dev/null
}

function make_clean
{
    cd $podm_path/make
    make cleanall
    cd ->/dev/null
}

function make_base_container
{
    cat >$app_base_conf <<EOF
{
  "docker_image":"app-base:1"
  "container_name": "$container_name"
  "cmd": "/sbin/init"
  "run_opts":" --privileged"
  "ovs": "ovs-jgq-image $container_on0_ip/24"
}
EOF
    docker-manage create $app_base_conf
    rm -rf $app_base_conf
    cat >$repo_file <<EOF
[jgq]
name=jgq
baseurl=$yum_repo
enabled=1
gpgcheck=0
EOF
    run $container_name "rm -rf /etc/yum.repos.d/*"
    docker cp $repo_file $container_name:/etc/yum.repos.d/jgq.repo
    rm -rf $repo_file
    run $container_name "yum -y install bash-completion tar passwd createrepo net-tools httpd perl \
        vim perl-DBI nmap-ncat libaio initscripts cyrus-sasl libicu logrotate python-setuptools \
        python-pyasn1 pytz python-ldap PyPAM openssl python-paste PyYAML python-decorator python-mako \
        python-chardet dhcp tftp-server syslinux nfs-utils fontpackages-filesystem cronie python-lxml \
        sudo openssh-server openssh-clients python-dateutil python-memcached vsftpd web.py man-db \
        man-pages zip unzip ntp chrony telnet wget rpm-build net-snmp net-snmp-utils"
    run $container_name "yum -y install e2fsprogs lvm2 cifs-utils psmisc xfsprogs ethtool rsync lsof expect"
    run $container_name "yum -y install cluster-glue cluster-glue-libs corosync corosynclib libqb \
        pacemaker pacemaker-cli pacemaker-cluster-libs pacemaker-libs pacemaker-remote pcs pciutils \
        net-snmp net-snmp-utils"

    install_uniview_dev

    run $container_name "echo ossdbg1 | passwd --stdin root"
    run $container_name "ln -svf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime"

    run $container_name "systemctl start httpd"
    run $container_name "systemctl enable httpd"
    run $container_name "mkdir -p /run/httpd"
    #关闭UseDNS加速ssh登录
    run $container_name "sed -i '/^UseDNS/d' /etc/ssh/sshd_config"
    run $container_name "sed -i '/^GSSAPIAuthentication/d' /etc/ssh/sshd_config"
    run $container_name "echo 'UseDNS no' >> /etc/ssh/sshd_config"
    run $container_name "echo 'GSSAPIAuthentication no' >> /etc/ssh/sshd_config"
    run $container_name "systemctl start sshd"
    run $container_name "systemctl enable sshd"

    # set zte DNS
    run $container_name "echo 'nameserver     $nameserver' >> cat /etc/resolv.conf"

    # set locale to en_US.UTF-8
    run $container_name "echo LANG=\"en_US.UTF-8\" > /etc/locale.conf"

    run $container_name "sed -i '/^server*/d' /etc/chrony.conf"
    run $container_name "sed -i '/^local *stratum*/d' /etc/chrony.conf"
    run $container_name "sed -i '/^allow */d' /etc/chrony.conf"
    run $container_name "sed -i '/^makestep */d' /etc/chrony.conf"
    run $container_name "echo 'server 10.30.1.105' >> /etc/chrony.conf"
    run $container_name "echo 'allow all' >> /etc/chrony.conf"
    run $container_name "echo 'local stratum 10' >> /etc/chrony.conf"
    run $container_name "echo 'makestep 10 -1' >> /etc/chrony.conf"
    run $container_name "systemctl disable ntpd"
    run $container_name "systemctl disable chronyd"

    # run $container_name "ssh-keygen -t rsa -P \"\" -f /root/.ssh/id_rsa"
    # run $container_name "/usr/bin/cp /root/.ssh/id_rsa.pub /root/.ssh/authorized_keys"
    docker cp $PWD/../root/.ssh $container_name:/root/
    run $container_name "chmod 600 /root/.ssh/authorized_keys /root/.ssh/id_rsa /root/.ssh/id_dsa"
    run $container_name "chmod 644 /root/.ssh/id_rsa.pub /root/.ssh/id_dsa.pub"
    run $container_name "sed -i \"s/#[[:space:]]*StrictHostKeyChecking ask/StrictHostKeyChecking no/g\" /etc/ssh/ssh_config"

    run $container_name "route del default"
    run $container_name "route add default gw 138.1.1.3"
    make_bin
    docker cp $podm_path/target/podmanager_*_el7_x86_64.bin $container_name:/home/podm.bin
    make_clean
    run $container_name "/home/podm.bin -- --docker --include-dashboard install"

    run $container_name "rm -rf /home/podm*.bin"
    # run $container_name "rm -rf /home/tmp"
}

function install_uniview_dev
{
    local gradle_download_url=$yum_repo/gradle-1.11-all.zip
    local scala_download_url=$yum_repo/scala-2.10.4.zip

    run $container_name "yum -y install jdk"
    run $container_name "wget $gradle_download_url"
    run $container_name "wget $scala_download_url"

    run $container_name "unzip gradle-1.11-all.zip"
    run $container_name "unzip scala-2.10.4.zip"
    run $container_name "mv gradle-1.11 /usr/local/"
    run $container_name "mv scala-2.10.4 /usr/local/"
    run $container_name "chmod 755 /usr/local/scala-2.10.4/bin/*"
    run $container_name "chmod 755 /usr/local/gradle-1.11/bin/*"
    run $container_name "rm -rf gradle-1.11-all.zip scala-2.10.4.zip"

    docker cp $PWD/../etc/uniview.sh $container_name:/etc/profile.d/
}

function commit_image
{
    echo "docker commit $container_name jgq-base:1 ..."
    docker commit -m "Working Base Image" $container_name jgq-base:1 || { echo "docker commit $container_name err!"; return 1;}
    docker-manage rm $container_name
}

function main
{
    check_depend || exit 1
    make_base_container || err_clean
    commit_image || err_clean
}

main

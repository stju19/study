#! /bin/bash

# jgq
alias jgq='cd /home/jgq'
alias scala='scala4uniview'
alias tree="tree --charset ascii"
alias vi="vim"
alias greptext='find . -type f | xargs grep --color=auto -ri'
alias greppy='find . -name *.py | xargs grep --color=auto -ri'

# podm
alias P='cd /home/jgq/ZXOCSA/podm'
alias ppp='cd /home/jgq/ZXOCSA/podm/podm/podm/podm/'
alias pts='cd /home/jgq/ZXOCSA/podm/tools/setup/'
alias ptd='cd /home/jgq/ZXOCSA/podm/tools/docker/'
#source /root/keystonerc_podm
#source /root/.keystone_admin
export PS1='[\u@\h \W]\$ '


# uniview
alias U='cd /home/jgq/Uniview/vDirector'
alias ci='cd /home/jgq/Uniview/vDirector/ztes/build/ci'
alias repo='cd /home/jgq/Uniview/vDirector/ztes/repo'
alias repo-scala='Uniview-test-console repo'
alias repo-log='cd /var/zte-log/testlog/zte-repo/logs/all'
alias firmware='cd /home/jgq/Uniview/vDirector/ztes/firmware'
alias firmware-scala='Uniview-test-console firmware'
alias firmware-log='cd /var/zte-log/testlog/zte-firmware/logs/all'


export PATH="$PATH:/usr/share/jgq"

echo "jgq-status: On"
cd /home/jgq
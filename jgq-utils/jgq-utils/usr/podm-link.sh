#!/bin/bash

if [ "$1" == "-h" ]; then
    echo 'podm-link [-d]'
    echo 'podm-link [-m]'
    echo ''
    exit
fi

if [ "$1" == "-m" ]; then
    rm -rf /lib/python2.7/site-packages/podm
    rm -rf /lib/python2.7/site-packages/podmclient
    ln -sv /root/podm_merge/podm/podm/podm/podm /lib/python2.7/site-packages/podm
    ln -sv /root/podm_merge/podm/podm/podmclient/podmclient /lib/python2.7/site-packages/podmclient
    exit
fi

if [ "$1" == "-d" ]; then
    rm -rf /lib/python2.7/site-packages/podm
    rm -rf /lib/python2.7/site-packages/podmclient
    #rm -rf /lib/python2.7/site-packages/horizon
    #rm -rf /usr/share/openstack-dashboard/openstack_dashboard
    exit
fi

rm -rf /lib/python2.7/site-packages/podm
rm -rf /lib/python2.7/site-packages/podmclient
#rm -rf /lib/python2.7/site-packages/horizon
#rm -rf /usr/share/openstack-dashboard/openstack_dashboard
ln -sv /home/jgq/ZXOCSA/podm/podm/podm/podm /lib/python2.7/site-packages/podm
ln -sv /home/jgq/ZXOCSA/podm/podm/podmclient/podmclient /lib/python2.7/site-packages/podmclient
#ln -sv /home/ZXOCSA/podm/podm/dashboard/horizon /lib/python2.7/site-packages/horizon
#ln -sv /home/ZXOCSA/podm/podm/dashboard/openstack_dashboard /usr/share/openstack-dashboard/openstack_dashboard

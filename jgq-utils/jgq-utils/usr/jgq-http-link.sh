#! /bin/bash

httpd_dir=/var/www/html

# yum repo server
ln -svnf /home/rpms/centos7.0 $httpd_dir/centos7.0
ln -svnf /home/rpms/centos7.2 $httpd_dir/centos7.2
ln -svnf /home/rpms/KVM.CGSL_VPLAT $httpd_dir/cgsl_vplat
ln -svnf /home/rpms/Packages/docker_install $httpd_dir/docker_install
ln -svnf /home/rpms/Packages $httpd_dir/podm_docker
ln -svnf /var/tfg-sys/tfg-depend $httpd_dir/tfg-depend
ln -svnf /home/rpms/Packages/ZXVEi.SERVER $httpd_dir/vplat_os

# Scala Doc
ln -svnf /home/jgq/doc/index.html $httpd_dir/index.html
ln -svnf /home/jgq/doc $httpd_dir/doc

# Podm Release
ln -svnf /home/PODM_RELEASE $httpd_dir/podm-docker

# common tools
ln -svnf /home/tools/http $httpd_dir/tools

Name:jgq-utils
Version: %{_version}
Release: 1.el7
Summary: utilities for myself

License: GPL
Group: Applications/Daemons
URL: http://
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_topdir}/BUILDROOT
BuildArch: noarch

%description
utilities for myself

%prep
%setup -c -n %{name}-%{version}

%build

%install
install -d -m 755 %{buildroot}%{_bindir}
install -p -D -m 755 jgq-utils/bin/podm-link.sh %{buildroot}%{_bindir}/podm-link
install -p -D -m 755 jgq-utils/bin/podm-restart-services.sh %{buildroot}%{_bindir}/podm-restart-services
install -p -D -m 755 jgq-utils/bin/podm-stop-services.sh %{buildroot}%{_bindir}/podm-stop-services
install -p -D -m 755 jgq-utils/bin/set-proxy.sh %{buildroot}%{_bindir}/set-proxy
install -p -D -m 755 jgq-utils/bin/jgq-git-config.sh %{buildroot}%{_bindir}/jgq-git-config
install -p -D -m 755 jgq-utils/bin/jgq-docker.sh %{buildroot}%{_bindir}/jgq-docker

install -d -m 755 %{buildroot}%{_sysconfdir}/profile.d
install -p -D -m 640 jgq-utils/etc/jgq-utils.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/jgq-utils
install -p -D -m 640 jgq-utils/etc/jgq.sh %{buildroot}%{_sysconfdir}/profile.d/jgq.sh
install -p -D -m 640 jgq-utils/etc/podm.sh %{buildroot}%{_sysconfdir}/profile.d/podm.sh

install -d -m 755 %{buildroot}%{_sysconfdir}/yum.repos.d
install -p -D -m 644 jgq-utils/etc/CentOS7-Base-163.repo.bak %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS7-Base-163.repo.bak
install -p -D -m 644 jgq-utils/etc/local.repo %{buildroot}%{_sysconfdir}/yum.repos.d/local.repo

%files
%{_bindir}/*
%{_sysconfdir}/profile.d/*
%{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/bash_completion.d/*

%changelog

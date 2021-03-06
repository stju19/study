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
install -d -m 755 %{buildroot}%{_bindir}/usr/share/jgq

install -p -D -m 755 jgq-utils/bin/jgq.sh %{buildroot}%{_bindir}/jgq
install -p -D -m 755 jgq-utils/usr/podm-link.sh %{buildroot}/usr/share/jgq/podm-link
install -p -D -m 755 jgq-utils/usr/podm-restart-services.sh %{buildroot}/usr/share/jgq/podm-restart-services
install -p -D -m 755 jgq-utils/usr/podm-stop-services.sh %{buildroot}/usr/share/jgq/podm-stop-services
install -p -D -m 755 jgq-utils/usr/set-proxy.sh %{buildroot}/usr/share/jgq/set-proxy
install -p -D -m 755 jgq-utils/usr/jgq-git-config.sh %{buildroot}/usr/share/jgq/jgq-git-config
install -p -D -m 755 jgq-utils/usr/jgq-docker.sh %{buildroot}/usr/share/jgq/jgq-docker
install -p -D -m 755 jgq-utils/usr/scala4uniview.sh %{buildroot}/usr/share/jgq/scala4uniview
install -p -D -m 755 jgq-utils/usr/Uniview-update-service.sh %{buildroot}/usr/share/jgq/Uniview-update-service
install -p -D -m 755 jgq-utils/usr/Uniview-check-ci.sh %{buildroot}/usr/share/jgq/Uniview-check-ci
install -p -D -m 755 jgq-utils/usr/Uniview-test-console.sh %{buildroot}/usr/share/jgq/Uniview-test-console
install -p -D -m 755 jgq-utils/usr/jgq-http-link.sh %{buildroot}/usr/share/jgq/jgq-http-link

install -d -m 755 %{buildroot}%{_sysconfdir}/profile.d
install -p -D -m 640 jgq-utils/etc/jgq-utils.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/jgq-utils
install -p -D -m 640 jgq-utils/etc/jgq.sh %{buildroot}%{_sysconfdir}/profile.d/jgq.sh

install -d -m 755 %{buildroot}%{_sysconfdir}/yum.repos.d
install -p -D -m 644 jgq-utils/etc/CentOS7-Base-163.repo.bak %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS7-Base-163.repo.bak
install -p -D -m 644 jgq-utils/etc/local.repo %{buildroot}%{_sysconfdir}/yum.repos.d/local.repo

%files
%{_bindir}/*
/usr/share/jgq/*
%{_sysconfdir}/profile.d/*
%{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/bash_completion.d/*

%changelog

Name:simian-enhanced
Version: %{_version}
Release: 1.el7
Summary: increased code duplicate check tool

License: GPL
Group: Applications/Daemons
Packager: Ju Guanqiu <ju.guanqiu@zte.com.cn>
Source: %{name}-%{version}.tar.gz
BuildRoot: %{_topdir}/BUILDROOT
BuildArch: noarch

%description
increased code duplicate check tool

%prep
%setup -c -n %{name}-%{version}

%build

%install
install -d -m 755 %{buildroot}%{_bindir}
install -p -D -m 755 simian-enhanced/bin/simian_report_analyze.py %{buildroot}%{_bindir}/simian-analyze
install -p -D -m 755 simian-enhanced/bin/simian.sh %{buildroot}%{_bindir}/simian

install -d -m 755 %{buildroot}%{_sysconfdir}/simian-enhanced

install -d -m 755 %{buildroot}/var/lib/simian-enhanced
install -p -D -m 644 simian-enhanced/tools/simian-2.5.3.jar %{buildroot}/var/lib/simian-enhanced/
install -p -D -m 644 simian-enhanced/etc/pre-push %{buildroot}/var/lib/simian-enhanced/pre-push

%files
%{_bindir}/*
%{_sysconfdir}/*
/var/lib/simian-enhanced/*

%changelog

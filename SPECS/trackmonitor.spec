Name: trackmonitor
Version: 1
Release: 1
Summary: Script for mail track linux	
Source: trackmonitor-1.1.tar.gz	
License: GPL
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-buildroot
%description
Oneshot script for logging current system state.
%prep
%setup -q
%build
%install
install -m 0755 -d ${RPM_BUILD_ROOT}/etc/trackmonitor
install -m 0755 -d ${RPM_BUILD_ROOT}/etc/systemd/system
install -m 0755 -d ${RPM_BUILD_ROOT}/var/spool/cron
install -m 0755 -d ${RPM_BUILD_ROOT}/var/log/trackmonitor
install -m 0755 trackmonitor.service ${RPM_BUILD_ROOT}/etc/systemd/system/trackmonitor.service
install -m 0755 monitoring.sh ${RPM_BUILD_ROOT}/etc/trackmonitor/monitoring.sh
install -m 0755 monitoring ${RPM_BUILD_ROOT}/var/spool/cron/monitoring
install -m 0755 monitoring.log ${RPM_BUILD_ROOT}/var/log/trackmonitor/monitoring.log

%clean
rm -rf ${RPM_BUILD_ROOT}
%files
%dir /etc/trackmonitor
/etc/trackmonitor/monitoring.sh
%dir /etc/systemd/system
/etc/systemd/system/trackmonitor.service
/var/spool/cron/monitoring
%dir /var/log/trackmonitor
/var/log/trackmonitor/monitoring.log

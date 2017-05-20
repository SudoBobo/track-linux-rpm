Name: trackmonitor
Version: 1
Release: 6
Summary: Script for mail track linux	
Source: trackmonitor-1.6.tar.gz	
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
install -m 0755 -d ${RPM_BUILD_ROOT}/etc/rsyslog.d
install -m 0755 etc/systemd/system/trackmonitor.service ${RPM_BUILD_ROOT}/etc/systemd/system/trackmonitor.service
install -m 0755 etc/trackmonitor/monitoring.sh ${RPM_BUILD_ROOT}/etc/trackmonitor/monitoring.sh
install -m 0755 var/spool/cron/monitoring ${RPM_BUILD_ROOT}/var/spool/cron/monitoring
install -m 0755 etc/rsyslog.d/trackmonitor.conf ${RPM_BUILD_ROOT}/etc/rsyslog.d/trackmonitor.conf

%post
systemctl start trackmonitor.service

%clean
rm -rf ${RPM_BUILD_ROOT}
%files
%dir /etc/trackmonitor
/etc/trackmonitor/monitoring.sh
/etc/systemd/system/trackmonitor.service
/var/spool/cron/monitoring
/etc/rsyslog.d/trackmonitor.conf
%dir /var/log/trackmonitor

Name: trackmonitor
Version: 1
Release: 18
Summary: Script for mail track linux	
Source: trackmonitor-1.18.tar.gz	
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
install -m 0755 -d ${RPM_BUILD_ROOT}/etc/cron.d
install -m 0755 -d ${RPM_BUILD_ROOT}/var/log/trackmonitor
install -m 0755 -d ${RPM_BUILD_ROOT}/etc/rsyslog.d
install -m 0644 etc/systemd/system/trackmonitor.service ${RPM_BUILD_ROOT}/etc/systemd/system/trackmonitor.service
install -m 0755 etc/trackmonitor/monitoring.sh ${RPM_BUILD_ROOT}/etc/trackmonitor/monitoring.sh
install -m 0644 etc/cron.d/trackmonitor ${RPM_BUILD_ROOT}/etc/cron.d/trackmonitor
install -m 0644 etc/rsyslog.d/trackmonitor.conf ${RPM_BUILD_ROOT}/etc/rsyslog.d/trackmonitor.conf

%post
systemctl enable trackmonitor.service

%preun
if [ $1 == 0 ]; then
systemctl disable trackmonitor.service
fi

%clean
rm -rf ${RPM_BUILD_ROOT}
%files
%dir /etc/trackmonitor
/etc/trackmonitor/monitoring.sh
/etc/systemd/system/trackmonitor.service
/etc/cron.d/trackmonitor
/etc/rsyslog.d/trackmonitor.conf
%dir /var/log/trackmonitor

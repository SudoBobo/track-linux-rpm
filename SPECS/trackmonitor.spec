Name: trackmonitor
Version: 1
Release: 0
Summary: Script for mail track linux	
Source0: trackmonitor-1.0.tar.gz	
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
install -m 0755 monitoring.sh ${RPM_BUILD_ROOT}/etc/trackmonitor/monitoring.sh
%clean
rm -rf ${RPM_BUILD_ROOT}
%post
echo . .
echo . Succesfully installed in ${RPM_BUILD_ROOT}/etc/trackmonitor
%files
%dir /etc/trackmonitor
/etc/trackmonitor/monitoring.sh

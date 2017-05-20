Name: test
Version:	0.4
Release:	1%{?dist}
Summary:	Test test

License:	GPL

%description
Test test

%pre
echo preinstall $1

%post
echo postinstall $1

%preun
echo preuninstall $1

%postun
echo postuninstall $1

%files
%doc


%define name nethserver-urbackup
%define version 0.0.2
%define release 2
Summary: Nethserver integration of urbcakup
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GNU GPL
URL: http://www.splitbrain.org/projects/dokuwiki
Source: %{name}-%{version}.tar.gz
BuildArchitectures: noarch
BuildRequires: nethserver-devtools
BuildRoot: /var/tmp/%{name}-%{version}
Requires: nethserver-httpd
Requires: urbackup-server
AutoReqProv: no

%description
Nethserver integration of urbackup
UrBackup is an easy to setup open source client/server backup system, that through a combination of image and file backups accomplishes both data safety and a fast restoration time.


%prep
%setup

%build
perl ./createlinks
%{__mkdir_p} root/var/lib/urbackup

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist \
  --dir /var/lib/urbackup 'attr(0755,urbackup,urbackup)' \
$RPM_BUILD_ROOT \
	> %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig urbackup-server on

%postun

%changelog
* Sun Mar 12 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.2-2
- GPL license

* Wed May 11 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.2
- the folder /var/lib/urbackup is created by the rpm

* Sat Apr 23 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.1
- First release to Nethserver

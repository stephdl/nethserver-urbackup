%define name nethserver-urbackup
%define version 0.1.4
%define release 1
Summary: Nethserver integration of urbackup
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
sed -i 's/_RELEASE_/%{version}/' %{name}.json

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
cp -a manifest.json %{buildroot}/usr/share/cockpit/%{name}/
cp -a logo.png %{buildroot}/usr/share/cockpit/%{name}/
cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/

rm -f %{name}-%{version}-filelist
%{genfilelist} \
  --dir /var/lib/urbackup 'attr(0755,urbackup,urbackup)' \
$RPM_BUILD_ROOT \
	> %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/systemctl enable urbackup-server

%postun

%changelog
* Tue Oct 15 2019 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.4
- cockpit. added to legacy apps

* Wed Jun 5 2019 Stephane de Labrusse  <stephdl@de-labrusse.fr> - 0.1.3
- Enable urbackup repo with  software-repos-save

* Sun Sep 10 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.2-1.ns7
- Restart httpd service on trusted-network

* Wed Mar 29 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.1-1.ns7
- Template expansion on trusted-network

* Sun Mar 12 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.0-2.ns7
- GPL license

* Mon Nov 21 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.0-1.ns7
- New version for ns7

* Wed May 11 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.2
- the folder /var/lib/urbackup is created by the rpm

* Sat Apr 23 2016 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.1
- First release to Nethserver

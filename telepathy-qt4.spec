%define _disable_ld_no_undefined 1

%define oname telepathy-qt

Name:		telepathy-qt4
Version:	0.9.3
Release:	1
Summary:	Base classes for use in connection managers, and proxy classes
License:	GPL
Group:		Networking/Instant messaging
Url:		http://telepathy.freedesktop.org/wiki/Telepathy-Qt4
Source0:	http://telepathy.freedesktop.org/releases/%{oname}/%{oname}-%{version}.tar.gz
Patch0:		telepathy-qt-0.9.3-fix-link.patch
BuildRequires:	pkgconfig(telepathy-farstream)
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(gstreamer-interfaces-0.10)
BuildRequires:	python
BuildRequires:	python-dbus
BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	qt4-devel
BuildRequires:	qt4-assistant
BuildRequires:	libxml2-utils

%description
Qt4 libraries for use in Telepathy clients and connection managers

#--------------------------------------------------------------------

%define libtelepathy_qt4_farstream_major 2
%define libtelepathy_qt4_farstream %mklibname telepathy-qt4-farstream %{libtelepathy_qt4_farstream_major}

%package -n %{libtelepathy_qt4_farstream}
Summary:	Core Decibel library
Group:		System/Libraries

%description -n %{libtelepathy_qt4_farstream}
Core Decibel library.

%files -n %{libtelepathy_qt4_farstream}
%{_libdir}/libtelepathy-qt4-farstream.so.%{libtelepathy_qt4_farstream_major}*

#--------------------------------------------------------------------

%define libtelepathy_qt4_major 2
%define libtelepathy_qt4 %mklibname telepathy-qt4_ %{libtelepathy_qt4_major}

%package -n %{libtelepathy_qt4}
Summary:	Core Decibel library
Group:		System/Libraries

%description -n %{libtelepathy_qt4}
Core Decibel library.

%files -n %{libtelepathy_qt4}
%{_libdir}/libtelepathy-qt4.so.%{libtelepathy_qt4_major}*

#--------------------------------------------------------------------

%package devel
Summary:	%{name} development files
Group:		Development/Other
Provides:	libtelepathy-qt-devel = %{version}
Requires:	%{libtelepathy_qt4} = %{version}
Requires:	%{libtelepathy_qt4_farstream} = %{version}

%description devel
Telepathy-qt development files.

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/cmake/TelepathyQt4
%{_libdir}/cmake/TelepathyQt4Farstream

#--------------------------------------------------------------------
%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1 -b .link

%build
%cmake
%make

%install
%makeinstall_std -C build


%changelog
* Mon Jul 16 2012 Andrey Bondrov <abondrov@mandriva.org> 0.9.3-1
+ Revision: 809887
- New version 0.9.3, update library names and major versions, update files

* Thu Dec 01 2011 Zé <ze@mandriva.org> 0.8.0-1
+ Revision: 735896
- version 0.8.0
- rediff link patch
- drop mkrell
- clean BR, defattr and clean section
- set to allow undefined references

* Sat May 07 2011 Funda Wang <fwang@mandriva.org> 0.5.16-1
+ Revision: 672288
- more linkage fix
- update to new version 0.5.16

* Wed Apr 27 2011 Funda Wang <fwang@mandriva.org> 0.5.15-1
+ Revision: 659525
- update to new version 0.5.15

* Sat Apr 09 2011 Funda Wang <fwang@mandriva.org> 0.5.14-1
+ Revision: 652082
- New version 0.5.14

* Thu Sep 16 2010 Funda Wang <fwang@mandriva.org> 0.3.9-1mdv2011.0
+ Revision: 578956
- update url
- drop some obsoletes, need review at a later time
- New version 0.3.9

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - import telepathy-qt4



%define _disable_ld_no_undefined 1

%define oname telepathy-qt

Name:		telepathy-qt4
Version:	0.9.5
Release:	4
Summary:	Base classes for use in connection managers, and proxy classes
License:	GPL
Group:		Networking/Instant messaging
Url:		http://telepathy.freedesktop.org/wiki/Telepathy-Qt4
Source0:	http://telepathy.freedesktop.org/releases/%{oname}/%{oname}-%{version}.tar.gz
BuildRequires:	pkgconfig(farstream-0.2)
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
%{_libdir}/*.a
%{_libdir}/cmake/TelepathyQt4
%{_libdir}/cmake/TelepathyQt4Farstream
%{_libdir}/cmake/TelepathyQt4Service

#--------------------------------------------------------------------
%prep
%setup -q -n %{oname}-%{version}
%apply_patches

%build
%cmake -DPYTHON_EXECUTABLE=%__python2
%make

%install
%makeinstall_std -C build


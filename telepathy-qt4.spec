Name:          telepathy-qt4
Version:       0.5.15
Release:       %mkrel 1
Summary:       Base classes for use in connection managers, and proxy classes
License:       GPL
Group:         Networking/Instant messaging
Url:           http://telepathy.freedesktop.org/wiki/Telepathy-Qt4
Source:        http://telepathy.freedesktop.org/releases/telepathy-qt4/%name-%version.tar.gz
Patch0:        telepathy-qt4-0.5.14-link.patch
BuildRoot:     %{_tmppath}/%{name}-buildroot
BuildRequires: qt4-devel
BuildRequires: libtelepathy-farsight-devel >= 0.0.4
BuildRequires: libtelepathy-glib-devel >= 0.13.10
BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: gstreamer0.10-devel
BuildRequires: python
BuildRequires: cmake

%description
Qt4 libraries for use in Telepathy clients and connection managers

#--------------------------------------------------------------------
%define libtelepathy_qt4_farsight_major 1
%define libtelepathy_qt4_farsight %mklibname telepathy-qt4-farsight %{libtelepathy_qt4_farsight_major}

%package -n %libtelepathy_qt4_farsight
Summary: Core Decibel library
Group: System/Libraries

%description -n %libtelepathy_qt4_farsight
Core Decibel library.

%files -n %libtelepathy_qt4_farsight
%defattr(-,root,root)
%{_libdir}/libtelepathy-qt4-farsight.so.%{libtelepathy_qt4_farsight_major}*

#--------------------------------------------------------------------

%define libtelepathy_qt4_major 1
%define libtelepathy_qt4 %mklibname telepathy-qt4_ %{libtelepathy_qt4_major}

%package -n %libtelepathy_qt4
Summary: Core Decibel library
Group: System/Libraries

%description -n %libtelepathy_qt4
Core Decibel library.

%files -n %libtelepathy_qt4
%defattr(-,root,root)
%{_libdir}/libtelepathy-qt4.so.%{libtelepathy_qt4_major}*

#--------------------------------------------------------------------

%package devel
Summary: %{name} development files
Group: Development/Other
Provides: libtelepathy-qt-devel = %{version}
Requires: %libtelepathy_qt4 = %{version}
Requires: %libtelepathy_qt4_farsight = %{version}

%description devel
Telepathy-qt development files.

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so

#--------------------------------------------------------------------

%prep
%setup -qn %name-%version
%patch0 -p0

%build
%cmake
%make

%install
rm -fr %buildroot

%makeinstall_std -C build

%clean
rm -rf %buildroot

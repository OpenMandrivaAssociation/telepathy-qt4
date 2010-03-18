%define revision 856598

Name:          telepathy-qt4
Version:       0.2.2
Release:       %mkrel 1
Epoch:         1
Summary:       Base classes for use in connection managers, and proxy classes
License:       GPL
Group:         Networking/Instant messaging
Url:           http://websvn.kde.org/trunk/kdesupport/telepathy-qt/
Source:        %name-%version.tar.gz
BuildRoot:     %{_tmppath}/%{name}-buildroot
BuildRequires: cmake
BuildRequires: qt4-devel
Provides:      TelepathyQt = %{version}
Obsoletes:     telepathy-qt
Provides:      telepathy-qt = %version-%release

%description
Qt4 libraries for use in Telepathy clients and connection managers

#--------------------------------------------------------------------

%define libtelepathy_qt4_farsight_major 0
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

%define libtelepathy_qt4_major 0
%define libtelepathy_qt4 %mklibname telepathy-qt4 %{libtelepathy_qt4_major}

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
Requires: %libtelepathy_qt4_farsight = %{epoch}:%{version}
Summary: %{name} development files
Group: Development/Other
Provides: libtelepathy-qt-devel = %{version}
Obsoletes: %{_lib}telepathy-qt-devel
Obsoletes: telepathy-qt-devel

%description devel
Telepathy-qt development files.

%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/libtelepathy-qt4-farsight.*a
%{_libdir}/libtelepathy-qt4.*a

#--------------------------------------------------------------------

%prep
%setup -q  -n %name-%version

%build
%configure2_5x

%make

%install
rm -fr %buildroot

%makeinstall_std

%clean
rm -rf %buildroot

%define name clutter-gtk
%define version 0.1.0
%define release %mkrel 1

%define api 1.0
%define major 0
%define libname %mklibname %name %api %major
%define libnamedevel %mklibname -d %name %api

%define crapname cluttergtk

Summary:       GTK Support for Clutter
Name:          %{name}
Version:       %{version}
Release:       %{release}
Source0:       %{name}-%{version}.tar.bz2
License:       LGPL
Group:         Graphics
Url:           http://clutter-project.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gtk2-devel
BuildRequires: gtk-doc

%description
GTK Support for Clutter

#----------------------------------------------------------------------------

%package -n %libname
Summary:       GTK Support for Clutter
Group:         Graphics

%description -n %libname
GTK Support for Clutter

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

#----------------------------------------------------------------------------

%package -n %libnamedevel
Summary:       Development headers/libraries for %name
Group:         Development/X11
Provides:      %name-devel = %version-%release
Requires:      %libname = %version-%release

%description -n %libnamedevel
Development headers/libraries for %name (see %libname package)

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure --enable-gtk-doc
%make

%install
rm -rf %buildroot

%makeinstall

%clean
rm -rf %buildroot

%files -n %libname
%defattr(-,root,root)
%_libdir/lib%{crapname}-%{api}.so.*

%files -n %libnamedevel
%_libdir/pkgconfig/%{name}.pc
%_libdir/lib%{crapname}-%{api}.la
%_libdir/lib%{crapname}-%{api}.so
%dir %_includedir/clutter-0.2/%{name}
%_includedir/clutter-0.2/%{name}/*.h
%dir %_datadir/gtk-doc/html/%name
%doc %_datadir/gtk-doc/html/%name/*

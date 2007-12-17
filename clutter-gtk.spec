%define name clutter-gtk
%define version 0.4.0
%define release %mkrel 1

%define api 0.4
%define major 0
%define libname %mklibname %name %api %major
%define libnamedevel %mklibname -d %name %api

Summary:       GTK Support for Clutter
Name:          %{name}
Version:       %{version}
Release:       %{release}
Source0:       %{name}-%{version}.tar.bz2
License:       LGPL
Group:         Graphics
Url:           http://clutter-project.org/
BuildRequires: clutter-devel
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

%post -n %libname
/sbin/ldconfig

%postun -n %libname
/sbin/ldconfig

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
%_libdir/lib%{name}-%{api}.so.*

%files -n %libnamedevel
%_libdir/pkgconfig/%{name}-%{api}.pc
%_libdir/lib%{name}-%{api}.la
%_libdir/lib%{name}-%{api}.so
%dir %_includedir/clutter-%{api}/%{name}
%_includedir/clutter-%{api}/%{name}/*.h
%dir %_datadir/gtk-doc/html/%name
%doc %_datadir/gtk-doc/html/%name/*

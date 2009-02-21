%define name clutter-gtk
%define version 0.8.3
%define release %mkrel 1

%define api 0.8
%define major 0
%define libname %mklibname %name %api %major
%define libnamedevel %mklibname -d %name %api

Summary:       GTK Support for Clutter
Name:          %{name}
Version:       %{version}
Release:       %{release}
Source0:       http://www.clutter-project.org/sources/clutter-gtk/%api/%{name}-%{version}.tar.bz2
License:       LGPLv2+
Group:         Graphics
Url:           http://clutter-project.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: clutter-devel
BuildRequires: gtk2-devel
BuildRequires: gtk-doc

%description
A library providing facilities to integrate Clutter into GTK+
applications. It provides a GTK+ widget, GtkClutterEmbed, for embedding the
default ClutterStage into any GtkContainer.

Because of limitations inside Clutter, it is only possible to embed a single
ClutterStage.

#----------------------------------------------------------------------------

%package -n %libname
Summary:       GTK Support for Clutter
Group:         Graphics

%description -n %libname
A library providing facilities to integrate Clutter into GTK+
applications. It provides a GTK+ widget, GtkClutterEmbed, for embedding the
default ClutterStage into any GtkContainer.

Because of limitations inside Clutter, it is only possible to embed a single
ClutterStage.

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%postun -n %libname
%if %mdkversion < 200900
/sbin/ldconfig
%endif

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
%configure2_5x --enable-gtk-doc
%make

%install
rm -rf %buildroot

%makeinstall

%clean
rm -rf %buildroot

%files -n %libname
%defattr(-,root,root)
%_libdir/lib%{name}-%{api}.so.%{major}*

%files -n %libnamedevel
%_libdir/pkgconfig/%{name}-%{api}.pc
%_libdir/lib%{name}-%{api}.la
%_libdir/lib%{name}-%{api}.so
%dir %_includedir/clutter-%{api}/%{name}
%_includedir/clutter-%{api}/%{name}/*.h
%dir %_datadir/gtk-doc/html/%name
%doc %_datadir/gtk-doc/html/%name/*

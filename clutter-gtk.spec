%define api 0.10
%define major 0
%define gir_major 1.0
%define libname		%mklibname %{name} %{api} %{major}
%define girname     %mklibname %{name}-gir %{api}
%define develname	%mklibname -d %{name} %{api}

Summary:	GTK Support for Clutter
Name:		clutter-gtk
Version:	1.1.2
Release:	1
License:	LGPLv2+
Group:		Graphics
Url:		http://clutter-project.org/
Source0:	http://www.clutter-project.org/sources/clutter-gtk/%{api}/%{name}-%{version}.tar.xz

BuildRequires: clutter-devel >= 1.0
BuildRequires: gtk2-devel
BuildRequires: gtk-doc
BuildRequires: docbook-dtd412-xml
BuildRequires: gobject-introspection-devel >= 0.6.3-0.20090616

%description
A library providing facilities to integrate Clutter into GTK+
applications. It provides a GTK+ widget, GtkClutterEmbed, for embedding the
default ClutterStage into any GtkContainer.

Because of limitations inside Clutter, it is only possible to embed a single
ClutterStage.

%package -n %{libname}
Summary:	GTK Support for Clutter
Group:		Graphics

%description -n %{libname}
A library providing facilities to integrate Clutter into GTK+
applications. It provides a GTK+ widget, GtkClutterEmbed, for embedding the
default ClutterStage into any GtkContainer.

Because of limitations inside Clutter, it is only possible to embed a single
ClutterStage.

%package -n %{girname}
Summary:    GObject Introspection interface description for %{name}
Group:      System/Libraries
Requires:   %{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Summary:       Development headers/libraries for %{name}
Group:         Development/X11
Provides:      %{name}-devel = %{version}-%{release}
Requires:      %{libname} = %{version}-%{release}

%description -n %{develname}
Development headers/libraries for %{name} (see %{libname} package)

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--enable-gtk-doc

%make

%install
rm -rf %{buildroot}
%makeinstall
find %{buildroot} -name *.la | xargs rm

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib%{name}-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GtkClutter-%{api}.typelib

%files -n %{develname}
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/lib%{name}-%{api}.so
%dir %{_includedir}/clutter-%{api}/%{name}
%{_datadir}/gir-1.0/GtkClutter-%{api}.gir
%dir %{_datadir}/gtk-doc/html/%{name}
%doc %{_datadir}/gtk-doc/html/%{name}/*


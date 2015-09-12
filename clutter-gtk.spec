%define api	1.0
%define major	0
%define libname	%mklibname %{name} %{api} %{major}
%define girname	%mklibname %{name}-gir %{api}
%define devname %mklibname -d %{name} %{api}

Summary:	GTK Support for Clutter
Name:		clutter-gtk
Version:	1.6.0
Release:	4
License:	LGPLv2+
Group:		Graphics
Url:		http://clutter-project.org/
Source0:	http://www.clutter-project.org/sources/clutter-gtk/%{api}/%{name}-%{version}.tar.xz

BuildRequires:	docbook-dtd412-xml
BuildRequires:	gtk-doc
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)

%description
A library providing facilities to integrate Clutter into GTK+
applications. It provides a GTK+ widget, GtkClutterEmbed, for embedding the
default ClutterStage into any GtkContainer.

Because of limitations inside Clutter, it is only possible to embed a single
ClutterStage.

%package -n %{libname}
Summary:       GTK Support for Clutter
Group:         Graphics

%description -n %{libname}
A library providing facilities to integrate Clutter into GTK+
applications. It provides a GTK+ widget, GtkClutterEmbed, for embedding the
default ClutterStage into any GtkContainer.

Because of limitations inside Clutter, it is only possible to embed a single
ClutterStage.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Conflicts:	%{_lib}clutter-gtk1.0_0 < 1.3.2-4

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:       Development headers/libraries for %{name}
Group:         Development/X11
Provides:      %{name}-devel = %{version}-%{release}
Requires:      %{libname} = %{version}-%{release}
Requires:      %{girname} = %{version}-%{release}

%description -n %{devname}
Development headers/libraries for %{name}

%prep
%setup -q

%build
%configure \
	--disable-static \
	--enable-gtk-doc
%make

%install
%makeinstall
%find_lang cluttergtk-%{api}

%files -n %{libname} -f cluttergtk-%{api}.lang 
%{_libdir}/lib%{name}-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/GtkClutter-%{api}.typelib

%files -n %{devname}
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/lib%{name}-%{api}.so
%dir %{_includedir}/%{name}-%{api}/%{name}
%{_includedir}/%{name}-%{api}/%{name}/*.h
%{_datadir}/gir-1.0/GtkClutter-%{api}.gir
%dir %{_datadir}/gtk-doc/html/%{name}-%{api}
%doc %{_datadir}/gtk-doc/html/%{name}-%{api}/*


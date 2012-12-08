%define api 1.0
%define clutterapi 1.0
%define major 0
%define libname %mklibname %{name} %{api} %{major}
%define libnamedevel %mklibname -d %{name} %{api}

Summary:       GTK Support for Clutter
Name:          clutter-gtk
Version:       1.3.2
Release:       3
License:       LGPLv2+
Group:         Graphics
Url:           http://clutter-project.org/
Source0:       http://www.clutter-project.org/sources/clutter-gtk/%{api}/%{name}-%{version}.tar.xz
BuildRequires: clutter-devel >= 1.0
BuildRequires: gtk2-devel
BuildRequires: gtk-doc
BuildRequires: gettext-devel
BuildRequires: docbook-dtd412-xml
BuildRequires: gobject-introspection-devel
BuildRequires: pkgconfig(gl)
#gw for Gtk-2.0.gir
BuildRequires: gir-repository

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

#----------------------------------------------------------------------------

%package -n %libnamedevel
Summary:       Development headers/libraries for %name
Group:         Development/X11
Provides:      %name-devel = %version-%release
Requires:      %libname = %version-%release

%description -n %libnamedevel
Development headers/libraries for %{name}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
autoreconf -fi
%configure2_5x --enable-gtk-doc
%make

%install
%makeinstall
%find_lang cluttergtk-%{clutterapi}

%files -f cluttergtk-%{clutterapi}.lang -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.%{major}*
%{_libdir}/girepository-1.0/GtkClutter-%api.typelib

%files -n %libnamedevel
%_libdir/pkgconfig/%{name}-%{api}.pc
%_libdir/lib%{name}-%{api}.so
%dir %_includedir/%name-%{clutterapi}/%{name}
%_includedir/%name-%{clutterapi}/%{name}/*.h
%_datadir/gir-1.0/GtkClutter-%api.gir
%dir %_datadir/gtk-doc/html/%name-%{clutterapi}
%doc %_datadir/gtk-doc/html/%name-%{clutterapi}/*


%changelog
* Tue Oct  2 2012 Arkady L. Shane <ashejn@rosalab.ru> 0.13.2-2
- rebuilt againt new cogl

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.8-3mdv2011.0
+ Revision: 663387
- mass rebuild

* Thu Mar 24 2011 Funda Wang <fwang@mandriva.org> 0.10.8-2
+ Revision: 648197
- add upstream patch to build with latest gi

* Thu Sep 16 2010 Götz Waschk <waschk@mandriva.org> 0.10.8-1mdv2011.0
+ Revision: 578979
- new version
- drop patch
- fix build with current gtk+

* Mon Sep 13 2010 Götz Waschk <waschk@mandriva.org> 0.10.6-2mdv2011.0
+ Revision: 577995
- rebuild for new g-i

* Thu Aug 12 2010 Götz Waschk <waschk@mandriva.org> 0.10.6-1mdv2011.0
+ Revision: 569292
- update to new version 0.10.6

* Fri Jul 30 2010 Funda Wang <fwang@mandriva.org> 0.10.4-2mdv2011.0
+ Revision: 563764
- rebuild for new clutter

* Mon Mar 22 2010 Götz Waschk <waschk@mandriva.org> 0.10.4-1mdv2010.1
+ Revision: 526343
- new version
- drop merged patches

* Fri Mar 12 2010 Götz Waschk <waschk@mandriva.org> 0.10.2-7mdv2010.1
+ Revision: 518428
- fix patch 1 (thanks to Keruspe)

* Fri Mar 12 2010 Götz Waschk <waschk@mandriva.org> 0.10.2-6mdv2010.1
+ Revision: 518418
- fix build with new gtk

* Fri Feb 12 2010 Götz Waschk <waschk@mandriva.org> 0.10.2-5mdv2010.1
+ Revision: 504647
- rebuild for new clutter

* Tue Aug 18 2009 Götz Waschk <waschk@mandriva.org> 0.10.2-4mdv2010.0
+ Revision: 417561
- fix introspection patch

* Mon Aug 17 2009 Götz Waschk <waschk@mandriva.org> 0.10.2-3mdv2010.0
+ Revision: 417246
- fix for new gobject-introspection
- update build deps for doc generation

* Wed Aug 12 2009 Götz Waschk <waschk@mandriva.org> 0.10.2-2mdv2010.0
+ Revision: 415263
- move typelib to library package

* Thu Jul 30 2009 Götz Waschk <waschk@mandriva.org> 0.10.2-1mdv2010.0
+ Revision: 404519
- new version
- new API
- bump clutter dep

* Tue Jun 23 2009 Götz Waschk <waschk@mandriva.org> 0.9.2-1mdv2010.0
+ Revision: 388740
- new version

* Tue Jun 16 2009 Götz Waschk <waschk@mandriva.org> 0.9.1-0.20090616.1mdv2010.0
+ Revision: 386363
- fix version

* Tue Jun 16 2009 Götz Waschk <waschk@mandriva.org> 0.9.0-0.20090616.1mdv2010.0
+ Revision: 386359
- update build deps
- new snapshot
- enable introspection

* Mon May 11 2009 Götz Waschk <waschk@mandriva.org> 0.9.0-0.20090511.1mdv2010.0
+ Revision: 374529
- git snapshot
- new api
- bump deps

* Sat Feb 21 2009 Götz Waschk <waschk@mandriva.org> 0.8.3-1mdv2009.1
+ Revision: 343558
- new version
- fix source URL
- update license
- use the right configure macro

* Thu Nov 13 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.2-3mdv2009.1
+ Revision: 302648
- rebuilt against new libxcb

* Tue Nov 11 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.2-2mdv2009.1
+ Revision: 302234
- rebuilt against new libxcb

* Sat Nov 08 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.2-1mdv2009.1
+ Revision: 301073
- 0.8.2

* Sat Sep 13 2008 Colin Guthrie <cguthrie@mandriva.org> 0.8.1-1mdv2009.0
+ Revision: 284373
- New version: 0.8.1

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.6.0-4mdv2009.0
+ Revision: 243539
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers
    - normalize call to ldconfig in %%post/%%postun

* Thu Feb 21 2008 Colin Guthrie <cguthrie@mandriva.org> 0.6.0-2mdv2008.1
+ Revision: 173782
- Improve description

* Wed Feb 20 2008 Colin Guthrie <cguthrie@mandriva.org> 0.6.0-1mdv2008.1
+ Revision: 173178
- New version

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.4.0-1mdv2008.1
+ Revision: 136322
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 08 2007 Colin Guthrie <cguthrie@mandriva.org> 0.4.0-1mdv2008.0
+ Revision: 60532
- New version: 0.4.0
- Import clutter-gtk


# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       libXfont
Summary:    X.Org X11 libXfont runtime library
Version:    1.4.3
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Source100:  libXfont.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fontcacheproto)


%description
libXfont provides the core of the legacy X11 font system, handling the
index files (fonts.dir, fonts.alias, fonts.scale), the various font file
formats, and rasterizing them



%package devel
Summary:    X.Org X11 libXfont development package
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   xorg-x11-filesystem

%description devel
the legacy X11 font system development files


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
# >> files
# FIXME:  Missing README/INSTALL - should file bug upstream.
#%doc AUTHORS COPYING README INSTALL ChangeLog NEWS
%doc AUTHORS COPYING ChangeLog
%{_libdir}/libXfont.so.1
%{_libdir}/libXfont.so.1.4.1
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%dir %{_includedir}/X11/fonts
%{_includedir}/X11/fonts/bdfint.h
%{_includedir}/X11/fonts/bitmap.h
%{_includedir}/X11/fonts/bufio.h
%{_includedir}/X11/fonts/fntfil.h
%{_includedir}/X11/fonts/fntfilio.h
%{_includedir}/X11/fonts/fntfilst.h
%{_includedir}/X11/fonts/fontconf.h
%{_includedir}/X11/fonts/fontencc.h
%{_includedir}/X11/fonts/fontmisc.h
%{_includedir}/X11/fonts/fontshow.h
%{_includedir}/X11/fonts/fontutil.h
%{_includedir}/X11/fonts/fontxlfd.h
%{_includedir}/X11/fonts/pcf.h
%{_includedir}/X11/fonts/ft.h
%{_includedir}/X11/fonts/ftfuncs.h
%{_libdir}/libXfont.so
%{_libdir}/pkgconfig/xfont.pc
# << files devel


Summary:	Frontend for xscreensaver in a dock.app
Name:		wmxss
Version:	0.1
Release:	%mkrel 16
License:	GPL
Group:		Graphical desktop/WindowMaker
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/wmxss-0.1.tar.gz
Requires:	xscreensaver-gl
BuildRequires:	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:	libxpm-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot


%description
Frontend for xscreensaver.
Right now it only runs the separate hacks in the DockApp


%prep
%setup -q

%build
make -C Src CFLAGS="$RPM_OPT_FLAGS"

%install
rm -fr %buildroot

install -m 755 -d %buildroot%{_miconsdir}
install -m 755 -d %buildroot%{_iconsdir}
install -m 755 -d %buildroot%{_liconsdir}
tar xjOf %SOURCE1 %{name}-16x16.png > %buildroot%{_miconsdir}/%{name}.png
tar xjOf %SOURCE1 %{name}-32x32.png > %buildroot%{_iconsdir}/%{name}.png
tar xjOf %SOURCE1 %{name}-48x48.png > %buildroot%{_liconsdir}/%{name}.png

mkdir -p %buildroot%{_bindir}
install -c -s -m 0755 Src/wmxss %buildroot%{_bindir}


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=WmXss
Comment=Frontend for xscreensaver in a dock.app
Exec=%{_bindir}/%{name} -e /usr/lib/xscreensaver/lament
Icon=%{name}
Terminal=false
Type=Application
Categories=Screensaver;
EOF


%clean
rm -fr %buildroot


%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif


%files
%defattr (-,root,root)
%doc COPYING
%{_bindir}/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop




%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.1-16mdv2010.0
+ Revision: 434956
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1-15mdv2009.0
+ Revision: 262123
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1-14mdv2009.0
+ Revision: 256339
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.1-12mdv2008.1
+ Revision: 129439
- kill re-definition of %%buildroot on Pixel's request
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Tue Feb 06 2007 Gustavo De Nardin <gustavodn@mandriva.com> 0.1-12mdv2007.0
+ Revision: 116930
- fixed .desktop file Comment

* Tue Jan 30 2007 Gustavo De Nardin <gustavodn@mandriva.com> 0.1-11mdv2007.1
+ Revision: 115274
- fixed and strip BuildRequires to minimum
- stop using old X prefix
- fixed menu entry
- added XDG menu entry for great compliance

* Wed Apr 27 2005 Lenny Cartier <lenny@mandriva.com> 0.1-10mdk
- rebuild

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.1-9mdk
- rebuild


Summary:	Frontend for xscreensaver in a dock.app
Name:		wmxss
Version:	0.1
Release:	%mkrel 12
License:	GPL
Group:		Graphical desktop/WindowMaker
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/wmxss-0.1.tar.gz
Requires:	xscreensaver-gl
BuildRequires:	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:	libxpm-devel


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

install -m 755 -d %buildroot%{_menudir}
cat <<EOF > %buildroot%{_menudir}/%{name}
?package(%{name}):command="%{_bindir}/%{name} -e /usr/lib/xscreensaver/lament" \
icon="%{name}.png" \
needs="X11" \
section="More Applications/Games/Toys" \
title="WmXss" \
longtitle="Frontend for xscreensaver in a small icon" \
xdg="true"
EOF

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


%post
%{update_menus}

%postun
%{clean_menus}


%files
%defattr (-,root,root)
%doc COPYING
%{_bindir}/*
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_menudir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop



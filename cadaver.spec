Summary:		Command-line WebDAV client
Name:		cadaver
Version:		0.23.3
Release:		2
License:		GPLv2+
Group:		Networking/File transfer
URL:		http://www.webdav.org/cadaver/
Source0:		http://www.webdav.org/cadaver/%{name}-%{version}.tar.gz
Source1:		http://www.webdav.org/cadaver/%{name}-%{version}.tar.gz.asc
Patch0:		cadaver-0.23.3-enable-build-with-neon-0.30.patch
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(neon)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(zlib)


%description
A command-line WebDAV client. Supports file upload, download,
on-screen display, name-space operations (move/copy), collection
creation and deletion, and locking operations.

%prep
%setup -q
%patch0 -p1 -b .neon0.30~

%build

%configure \
    --with-neon=%{_prefix} \
    --with-ssl \
    --with-libxml2

%make

%install
%makeinstall_std

%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/*
%{_mandir}/man1/*
%defattr(644,root,root,755)
%doc NEWS TODO FAQ README ChangeLog


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.23.3-2mdv2011.0
+ Revision: 610093
- rebuild

* Sun Dec 27 2009 Frederik Himpe <fhimpe@mandriva.org> 0.23.3-1mdv2010.1
+ Revision: 482735
- update to new version 0.23.3

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.23.2-5mdv2010.0
+ Revision: 436925
- rebuild

* Thu Mar 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.23.2-4mdv2009.1
+ Revision: 349192
- rebuild for latest readline

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.23.2-3mdv2009.0
+ Revision: 243420
- rebuild

* Sat Feb 16 2008 Frederik Himpe <fhimpe@mandriva.org> 0.23.2-1mdv2008.1
+ Revision: 169342
- New releaes, supports neon 0.28.0
- New license policy

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 23 2007 Oden Eriksson <oeriksson@mandriva.com> 0.23.0-1mdv2008.0
+ Revision: 69336
- fix deps
- 0.23.0


* Thu Jan 25 2007 Lenny Cartier <lenny@mandriva.com> 0.22.5-1mdv2007.0
+ Revision: 113345
- Update to 0.22.5

* Wed Jan 03 2007 GГ¶tz Waschk <waschk@mandriva.org> 0.22.4-1mdv2007.1
+ Revision: 103603
- Import cadaver

* Wed Jan 03 2007 Gцtz Waschk <waschk@mandriva.org> 0.22.4-1mdv2007.1
- fix buildrequires
- New version 0.22.4

* Wed Aug 02 2006 Lenny Cartier <lenny@mandriva.com> 0.22.3-2mdv2007.0
- rebuild

* Wed Mar 01 2006 Nicolas Lйcureuil <neoclust@mandriva.org> 0.22.3-1mdk
- New release 0.22.3

* Thu Jul 21 2005 Nicolas Lйcureuil <neoclust@mandriva.org> 0.22.2-2mdk
- mkrel

* Thu Jul 21 2005 Nicolas Lйcureuil <neoclust@mandriva.org> 0.22.2-1mdk
- New release 0.22.2

* Fri Jun 10 2005 Buchan Milne <bgmilne@linux-mandrake.com> 0.22.1-4mdk
- Rebuild for libkrb53-devel 1.4.1

* Thu Jan 20 2005 Per Г�yvind Karlsen <peroyvind@linux-mandrake.com> 0.22.1-3mdk
- rebuild for new readline

* Sat Apr 17 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.22.1-2mdk
- rebuild with new libneon

* Sat Apr 17 2004 Michael Scherer <misc@mandrake.org> 0.22.1-1mdk
- New release 0.22.1


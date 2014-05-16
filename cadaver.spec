Summary:	Command-line WebDAV client
Name:		cadaver
Version:	0.23.3
Release:	3
License:	GPLv2+
Group:		Networking/File transfer
URL:		http://www.webdav.org/cadaver/
Source0:	http://www.webdav.org/cadaver/%{name}-%{version}.tar.gz
Source1:	http://www.webdav.org/cadaver/%{name}-%{version}.tar.gz.asc
Patch0:		cadaver-0.23.3-enable-build-with-neon-0.30.patch
Patch1:		cadaver-0.23.3-update-and-fix-autofoo-mess.patch
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
%patch1 -p1 -b .autofoo~
autoreconf -fsv

%build
%configure	--with-neon=%{_prefix} \
		--with-ssl \
    		--with-libxml2 \
		--with-ca-bundle=%{_sysconfdir}/ssl/certs/ca-bundle.crt \
		--enable-threads=posix \
		--enable-threadsafe-ssl=posix
		

%make

%install
%makeinstall_std

%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/*
%{_mandir}/man1/*
%defattr(644,root,root,755)
%doc NEWS TODO FAQ README ChangeLog

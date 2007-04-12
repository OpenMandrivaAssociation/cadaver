%define	name	cadaver
%define version 0.22.5
%define release %mkrel 1

Summary:	Command-line WebDAV client
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/File transfer
Source0:	http://www.webdav.org/cadaver/%{name}-%{version}.tar.bz2
Source1:	http://www.webdav.org/cadaver/%{name}-%{version}.tar.gz.asc
URL:		http://www.webdav.org/cadaver/
BuildRequires:	openssl-devel ncurses-devel readline-devel expat-devel
BuildRequires:	libxml2-devel zlib-devel libneon0.26-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A command-line WebDAV client. Supports file upload, download,
on-screen display, namespace operations (move/copy), collection
creation and deletion, and locking operations.

%prep
%setup -q

%build

%configure2_5x \
    --with-neon=%{_prefix} \
    --with-ssl \
    --with-libxml2

%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/*
%{_mandir}/man1/*
%defattr(644,root,root,755)
%doc NEWS TODO FAQ COPYING README ChangeLog



Summary:	Command-line WebDAV client
Name:		cadaver
Version:	0.23.3
Release:	%mkrel 1
License:	GPLv2+
Group:		Networking/File transfer
URL:		http://www.webdav.org/cadaver/
Source0:	http://www.webdav.org/cadaver/%{name}-%{version}.tar.gz
Source1:	http://www.webdav.org/cadaver/%{name}-%{version}.tar.gz.asc
BuildRequires:	expat-devel
BuildRequires:	libneon0.27-devel
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	readline-devel
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A command-line WebDAV client. Supports file upload, download,
on-screen display, namespace operations (move/copy), collection
creation and deletion, and locking operations.

%prep
%setup -q

%build

%configure \
    --with-neon=%{_prefix} \
    --with-ssl \
    --with-libxml2

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/*
%{_mandir}/man1/*
%defattr(644,root,root,755)
%doc NEWS TODO FAQ README ChangeLog

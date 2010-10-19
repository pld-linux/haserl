#
Summary:	Tool that converts shell or lua code embedded in html into cgi scripts
Name:		haserl
Version:	0.9.27
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://downloads.sourceforge.net/project/haserl/haserl-devel/0.9.27/%{name}-%{version}.tar.gz
# Source0-md5:	1f692db8939858338a44e25d0190aa9e
URL:		http://haserl.sourceforge.net/
Patch0:		%{name}-lua51.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	lua51-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Haserl is a small program that uses shell or Lua script to create cgi
web scripts. It is intended for environments where PHP or ruby are too
big.

It was written for Linux, but is known to run on FreeBSD. A typical
use is to run cgi scripts in an embedded environment, using a small
web server, such as mini-httpd, lighty, or the server built into
busybox.

%prep
%setup -q

%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--with-lua-headers=%{_includedir}/lua51 \
	--with-lua=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS TODO
%attr(755,root,root) %{_bindir}/haserl
%{_mandir}/man1/haserl.1*

Summary:	LWIPV6a - light weight IPv6
Summary(pl.UTF-8):	LWIPV6a - lekkie IPv6
Name:		lwipv6
Version:	1.5a
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	https://downloads.sourceforge.net/view-os/%{name}-%{version}.tar.bz2
# Source0-md5:	d07cbd23feebe0eb749470fe49dd90cb
Patch0:		%{name}-link.patch
Patch1:		%{name}-includes.patch
Patch2:		%{name}-optflags.patch
URL:		http://wiki.v2.cs.unibo.it/wiki/index.php%3Ftitle=LWIPV6.html
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRequires:	libtool
BuildRequires:	vde2-devel >= 2
# dlopened
Suggests:	vde2-libs%{?_isa}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LWIPV6a is a TCP/IP stack, rewritten based on lwIP v1.1.0 (by Adam
Dunkels).

%description -l pl.UTF-8
LWIPV6a to stos TCP/IP napisany od nowa na podstawie lwIP (Adama
Dunkelsa) w wersji 1.1.0.

%package devel
Summary:	Header files for LWIPV6 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki LWIPV6
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for LWIPV6 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki LWIPV6.

%package static
Summary:	Static LWIPV6 library
Summary(pl.UTF-8):	Statyczna biblioteka LWIPV6
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LWIPV6 library.

%description static -l pl.UTF-8
Statyczna biblioteka LWIPV6.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README README.LICENSE
%attr(755,root,root) %{_libdir}/liblwipv6.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblwipv6.so.2

%files devel
%defattr(644,root,root,755)
%doc LWIPv6_Programming_Guide
%attr(755,root,root) %{_libdir}/liblwipv6.so
%{_libdir}/liblwipv6.la
%{_includedir}/lwipv6.h

%files static
%defattr(644,root,root,755)
%{_libdir}/liblwipv6.a

# TODO:
# - *.a and *.la? delete?
%define	orgname	iperf
Summary:	Network performance measurement tool
Summary(pl.UTF-8):	Narzędzie do szacowania wydajności sieci
Name:		iperf3
Version:	3.14
Release:	1
License:	BSD-like
Group:		Networking/Utilities
Source0:	https://downloads.es.net/pub/iperf/%{orgname}-%{version}.tar.gz
# Source0-md5:	2fcf9691a062e905204c1868686cb051
URL:		https://software.es.net/iperf/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake
BuildRequires:	libsctp-devel
BuildRequires:	libtool
BuildRequires:	linux-libc-headers >= 7:3.13
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iperf was orginally developed by NLANR/DAST as a modern alternative
for measuring maximum TCP and UDP bandwidth performance. Iperf allows
the tuning of various parameters and UDP characteristics. Iperf
reports bandwidth, delay jitter, datagram loss.

iperf3 is a new implementation from scratch, with the goal of a
smaller, simpler code base, and a library version of the functionality
that can be used in other programs. iperf3 is not backwards compatible
with iperf2.

%package libs
Summary:	Shared iperf3 libraries
Summary(pl.UTF-8):	Biblioteki współdzielone iperf3
Group:		Libraries

%description libs
Shared iperf3 libraries.

%description libs -l pl.UTF-8
Biblioteki współdzielone iperf3.

%package devel
Summary:	Header files for iperf3 libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek iperf3
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
Header files for iperf3 libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek iperf3.

%prep
%setup -q -n %{orgname}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-shared \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc INSTALL LICENSE README.md RELNOTES.md docs/
%attr(755,root,root) %{_bindir}/iperf3
%{_mandir}/man1/iperf3.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libiperf.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libiperf.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libiperf.so
%{_includedir}/iperf_api.h
%{_mandir}/man3/libiperf.3*

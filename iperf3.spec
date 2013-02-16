# TODO:
# - package library and devel files
%define	orgname	iperf
%define	beta	b4
Summary:	Network performance measurement tool
Summary(pl.UTF-8):	Narzędzie do szacowania wydajności sieci
Name:		iperf3
Version:	3.0
Release:	0.%{beta}.1
License:	BSD-like
Group:		Networking/Utilities
Source0:	http://iperf.googlecode.com/files/iperf-%{version}b4.tar.gz
# Source0-md5:	fde024a200b064b54accd1959f7e642e
Patch0:		%{name}-Werror.patch
URL:		http://code.google.com/p/iperf/
BuildRequires:	libstdc++-devel
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

%prep
%setup -q -n %{orgname}-%{version}%{beta}
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_mandir}/man1/{iperf,%{name}}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README RELEASE_NOTES TODO
%attr(755,root,root) %{_bindir}/iperf3
%{_mandir}/man1/*

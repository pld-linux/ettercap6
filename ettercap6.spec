Summary:	ettercap is a ncurses-based sniffer/interceptor utility
Summary(pl):	ettercap jest opartym o ncurses narzêdziem do sniffowania/przechwytywania
Name:		ettercap
Version:	0.6.4
Release:	1
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários
Source0:	http://ettercap.sourceforge.net/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-dont_require_root.patch
Patch1:		%{name}-ncurses.patch
Patch2:		%{name}-plugin_dir.patch
Patch3:		%{name}-kernel_version.patch
URL:		http://ettercap.sourceforge.net/
BuildRequires:	awk
BuildRequires:	textutils
BuildRequires:	grep
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ettercap is a multipurpose sniffer/interceptor/logger for switched or
"hubbed" LAN.

%description -l pl
ettercap jest wieloczynno¶ciowym snifferem/przechwytywaczem/loggerem dla sieci LAN 
opartych na switchach lub hubach.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1
#%patch2 -p1
%patch3 -p1

%build
aclocal
autoconf
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--enable-ncurses
%{__make}
%{__make} plug-ins

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
%{__make} plug-ins_install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf \
	README README.PLUGINS HISTORY CHANGELOG AUTHORS TODO \
	THANKS KNOWN-BUGS PORTINGS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%{_libdir}/ettercap
%{_datadir}/ettercap
%{_mandir}/man8/*

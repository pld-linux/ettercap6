Summary:	ettercap is a ncurses-based sniffer/interceptor utility
Name:		ettercap
Version:	0.5.4
Release:	1
Source0:	http://ettercap.sourceforge.net/download/%{name}-%{version}.tar.gz
URL:		http://ettercap.sourceforge.net/
License:	GPL
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ettercap is a multipurpose sniffer/interceptor/logger for switched or
"hubbed" LAN.

%prep
%setup -q

%build
%configure --disable-debug
%{__make}
%{__make} plug-ins

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
%{__make} plug-ins_install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_mandir}/man8/*
%doc COPYING README README.PLUGINS HISTORY CHANGELOG AUTHORS TODO THANKS KNOWN-BUGS PORTINGS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/ettercap/*

Summary:	ettercap is a ncurses-based sniffer/interceptor utility
Summary(pl):	ettercap jest opartym o ncurses narzêdziem do sniffowania/przechwytywania
Summary(pt_BR):	ettercap e um interceptador/sniffer paseado em ncurses
Name:		ettercap
Version:	0.6.b
Release:	2
Epoch:		1
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/ettercap/%{name}-%{version}.tar.gz
# Source0-md5:	f665cf82347a91f216184537f8f2c4bd
Patch0:		%{name}-dont_require_root.patch
Patch1:		%{name}-ncurses.patch
Patch2:		%{name}-plugin_dir.patch
Patch3:		%{name}-kernel_version.patch
URL:		http://ettercap.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	awk
BuildRequires:	grep
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel >= 0.9.6k
BuildRequires:	textutils
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ettercap is a network sniffer/interceptor/logger for ethernet LANs
(both switched or not). It supports active and passive dissection of
many protocols (even ciphered ones, like SSH and HTTPS). Data
injection in an established connection and filtering (substitute or
drop a packet) on the fly is also possible, keeping the connection
sincronized. Many sniffing modes were implemented to give you a
powerful and complete sniffing suite. Plugins are supported. It has
the ability to check whether you are in a switched LAN or not, and to
use OS fingerprints (active or passive) to let you know the geometry
of the LAN. The passive scan of the lan retrives infos about: hosts in
the lan, open ports, services version, type of the host (gateway,
router or simple host) and extimated distance in hop.

%description -l pl
ettercap jest wieloczynno¶ciowym snifferem/przechwytywaczem/loggerem
dla sieci LAN opartych na switchach lub hubach.

%description -l pt_BR
ettercap é um sniffer/interceptor/logger de rede para redes locais
(com uso de switches ou não). Suporta operações ativas e passivas de
vários protocolos (mesmo os criptografados, como SSH e HTTPS). Também
é possível injeção de dados em uma conexão estabelecida e filtragem
(substituição ou descarte de um pacote) em tempo real mantendo a
conexão sincronizada. Muitos modos de sniffing foram implementadas
para proporcionar a você um completo conjunto de sniffing. Plugins são
suportados. Tem a habilidade de verificar se você está em uma rede
local com switches ou não. Utiliza fingerprints do Sistema Operacional
(ativo ou passivo) para permitir que você conheça a geometria da rede
local. A varredura passiva da rede local obtém informações sobre:
hosts na rede local, portas abertas, versão de serviços, tipo de host
(gateway, router ou um computador) e a distância estimada no hop.

%prep
%setup -q
#%patch0 -p1
%patch1
#%patch2 -p1
%patch3 -p1

%build
%{__aclocal}
%{__autoconf}
CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"
%configure \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--enable-ncurses \
	--disable-gtk
%{__make}
%{__make} plug-ins

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%{__make} plug-ins_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.PLUGINS HISTORY CHANGELOG AUTHORS TODO
%doc THANKS KNOWN-BUGS PORTINGS 
%doc plugins/{H03_hydra1/HYDRA.HOWTO,H01_zaratan/ZARATAN.HOWTO,H09_roper/ROPER.HOWTO}
%attr(755,root,root) %{_sbindir}/*
%{_libdir}/ettercap
%{_datadir}/ettercap
%{_mandir}/man8/*

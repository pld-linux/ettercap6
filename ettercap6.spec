Summary:	ettercap - a ncurses-based sniffer/interceptor utility
Summary(pl.UTF-8):	ettercap - oparte o ncurses narzędzie do sniffowania/przechwytywania
Summary(pt_BR.UTF-8):	ettercap e um interceptador/sniffer paseado em ncurses
Name:		ettercap6
Version:	0.6.b
Release:	5
Epoch:		1
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/ettercap/ettercap-%{version}.tar.gz
# Source0-md5:	f665cf82347a91f216184537f8f2c4bd
Patch1:		%{name}-ncurses.patch
Patch2:		%{name}-plugin_dir.patch
Patch3:		%{name}-kernel_version.patch
Patch4:		%{name}-name.patch
URL:		http://ettercap.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-ext-devel
BuildRequires:	openssl-devel >= 0.9.7d
Provides:	ettercap = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
ettercap is a network sniffer/interceptor/logger for ethernet LANs
(both switched or not). It supports active and passive dissection of
many protocols (even ciphered ones, like SSH and HTTPS). Data
injection in an established connection and filtering (substitute or
drop a packet) on the fly is also possible, keeping the connection
synchronized. Many sniffing modes were implemented to give you a
powerful and complete sniffing suite. Plugins are supported. It has
the ability to check whether you are in a switched LAN or not, and to
use OS fingerprints (active or passive) to let you know the geometry
of the LAN. The passive scan of the LAN retrieves infos about: hosts
in the lan, open ports, services version, type of the host (gateway,
router or simple host) and extimated distance in hop.

%description -l pl.UTF-8
ettercap jest wieloczynnościowym snifferem/przechwytywaczem/loggerem
dla sieci LAN (opartych na switchach lub hubach). Obsługuje aktywną i
pasywną analizę wielu protokołów (nawet szyfrowanych, jak SSH czy
HTTPS). Możliwe jest także wstrzykiwanie lub filtrowanie danych
(podmiana lub usunięcie pakietu) w locie, przy podtrzymaniu
synchronizacji połączenia. Program ma zaimplementowane wiele trybów
sniffowania, aby dać potężne i kompletne narzędzie. Obsługiwane są
wtyczki. Program ma możliwość sprawdzania, czy pracuje w sieci ze
switchami oraz używania odcisków systemów (aktywnego lub pasywnego)
do poznania geometrii sieci. Pasywne skanowanie sieci uzyskuje
informacje o: hostach w sieci, otwartych portach, wersjach usług,
rodzajach hostów (bramki, routery lub zwykłe komputery) oraz
przybliżonych odległościach (w hopach).

%description -l pt_BR.UTF-8
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
%setup -q -n ettercap-%{version}
%patch1 -p0
#%patch2 -p1
%patch3 -p1
%patch4

%build
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%{__autoheader}
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
%configure \
	--enable-devel \
	--enable-ncurses \
	--disable-gtk \
	--%{!?debug:dis}%{?debug:en}able-debug \
	--enable-plugins \
	--enable-https
%{__make}
%{__make} plug-ins

%install
rm -rf $RPM_BUILD_ROOT

mv ettercap{,6}.8

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
%{_libdir}/ettercap6
%{_datadir}/ettercap6
%{_mandir}/man8/*

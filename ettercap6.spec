Summary:	ettercap - a ncurses-based sniffer/interceptor utility
Summary(pl):	ettercap - oparte o ncurses narzêdzie do sniffowania/przechwytywania
Summary(pt_BR):	ettercap e um interceptador/sniffer paseado em ncurses
Name:		ettercap
Version:	0.7.2
Release:	1
Epoch:		1
License:	GPL
Group:		Networking/Utilities
Source0:	http://heanet.dl.sourceforge.net/ettercap/%{name}-NG-%{version}.tar.gz
# Source0-md5:	96c85eb0acb3a1b28823012c146239b9
Patch1:		%{name}-ncurses.patch
Patch2:		%{name}-plugin_dir.patch
Patch3:		%{name}-kernel_version.patch
URL:		http://ettercap.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ncurses-ext-devel
BuildRequires:	openssl-devel >= 0.9.7d
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

%description -l pl
ettercap jest wieloczynno¶ciowym snifferem/przechwytywaczem/loggerem
dla sieci LAN (opartych na switchach lub hubach). Obs³uguje aktywn± i
pasywn± analizê wielu protoko³ów (nawet szyfrowanych, jak SSH czy
HTTPS). Mo¿liwe jest tak¿e wstrzykiwanie lub filtrowanie danych
(podmiana lub usuniêcie pakietu) w locie, przy podtrzymaniu
synchronizacji po³±czenia. Program ma zaimplementowane wiele trybów
sniffowania, aby daæ potê¿ne i kompletne narzêdzie. Obs³ugiwane s±
wtyczki. Program ma mo¿liwo¶æ sprawdzania, czy pracuje w sieci ze
switchami oraz u¿ywania odcisków systemów (aktywnego lub pasywnego)
do poznania geometrii sieci. Pasywne skanowanie sieci uzyskuje
informacje o: hostach w sieci, otwartych portach, wersjach us³ug,
rodzajach hostów (bramki, routery lub zwyk³e komputery) oraz
przybli¿onych odleg³o¶ciach (w hopach).

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
%setup -q -n %{name}-NG-%{version}
#%patch1 -p0
#%patch2 -p1
#%patch3 -p1

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
	--enable-https \
	--enable-gtk
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGELOG AUTHORS TODO doc/*
%doc THANKS README.BUGS
%attr(755,root,root) %{_bindir}/*
%{_libdir}/ettercap
%{_datadir}/ettercap
%{_mandir}/man8/*
%{_mandir}/man5/*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/etter.conf

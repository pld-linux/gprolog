Summary:	GNU Prolog - a free Prolog compiler with constraint solving over Finite Domains
Summary(es.UTF-8):	Prolog de GNU - un compilador libre de Prolog con resolución de ligaduras sobre dominios finitos
Summary(pl.UTF-8):	GNU Prolog - wolnodostępny kompilator języka Prolog
Summary(pt_BR.UTF-8):	O Prolog GNU
Name:		gprolog
Version:	1.4.0
Release:	1
License:	LGPL v3+ or GPL v2+
Group:		Development/Languages
Source0:	http://www.gprolog.org/%{name}-%{version}.tar.gz
# Source0-md5:	cc944e5637a04a9184c8aa46c947fd16
URL:		http://www.gprolog.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
ExclusiveArch:	%{ix86} %{x8664} alpha ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Prolog is a native Prolog compiler with constraint solving over
finite domains (FD) developed by Daniel Diaz
(http://loco.inria.fr/~diaz/).

GNU Prolog is a very efficient native compiler producing (small)
stand-alone executables. GNU-Prolog also offers a classical
top-level+debugger.

GNU Prolog conforms to the ISO standard for Prolog but also includes a
lot of extensions (global variables, DCG, sockets, OS interface,...).

GNU Prolog also includes a powerful constraint solver over finite
domains with many predefined constraints+heuristics.

%description -l es.UTF-8
GNU Prolog es un compilador nativo de Prolog con resolución de
ligaduras sobre dominios finitos (FD: Finite Domains), desarrollado
por Daniel Diaz (http://loco.inria.fr/~diaz/).

GNU Prolog es un compilador nativo muy eficiente que produce
ejecutables independientes (y pequeños). GNU Prolog también ofrece un
clásico nivel alto y un depurador.

GNU Prolog implementa el estándar ISO para Prolog, sin embargo incluye
un montón de extensiones (variables globales, DCG, sockets, inferfaz
de SO, ...).

GNU Prolog también habilita resolver ligaduras sobre dominios finitos
con varias ligaduras predefinidas y unas heuristicas.

%description -l pl.UTF-8
GNU Prolog jest bezpośrednim kompilatorem Prologu opartym na
rozwiązywaniu problemów z ograniczeniami z dziedziną skończoną (FD),
tworzonym przez Daniela Diaza (http://loco.inria.fr/~diaz/)

GNU Prolog jest bardzo wydajnyym bezpośrednim kompilatorem tworzącym
małe samodzielne programy wykonywalne. GNU-Prolog oferuje też
klasyczny interfejs wysokiego poziomu oraz debugger.

GNU Prolog jest zgodny z standardem ISO języka Prolog oraz oferuje
dodatkowo kilka rozszerzeń (zmienne globalne, DCG, gniazda, interfejs
do systemu operacyjnego...).

GNU Prolog zawiera też poręczny moduł rozwiązywania problemów z
ograniczeniami z dziedziną skończoną, z wieloma predefiniowanymi
ograniczeniami i heurystykami.

%description -l pt_BR.UTF-8
O GNU Prolog é um compilador nativo Prolog.

%package examples
Summary:	Examples for gprolog
Summary(pl.UTF-8):	Przykłady dla gprologa
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-examples = %{version}-%{release}

%description examples
Examples for gprolog.

%description examples -l pl.UTF-8
Przykłady dla gprologa.

%prep
%setup -q

%build
cd src
%{__aclocal}
%{__autoconf}
%configure \
	--prefix=$RPM_BUILD_ROOT \
	--with-install-dir=$RPM_BUILD_ROOT%{_libdir}/%{name}-%{version} \
	--with-c-flags="%{rpmcflags}" \
	--without-links-dir \
	--with-examples-dir=$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version} \
	--without-doc-dir \
	--without-html-dir
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C src install

install -d $RPM_BUILD_ROOT%{_bindir}
cd $RPM_BUILD_ROOT%{_libdir}/%{name}-%{version}/bin
for i in *; do
    ln -s ../%{_lib}/%{name}-%{version}/bin/$i $RPM_BUILD_ROOT%{_bindir}/$i
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING contains also licensing summary
%doc COPYING ChangeLog NEWS README doc/gprolog.ps doc/gprolog.pdf
%attr(755,root,root) %{_bindir}/fd2c
%attr(755,root,root) %{_bindir}/gplc
%attr(755,root,root) %{_bindir}/gprolog
%attr(755,root,root) %{_bindir}/hexgplc
%attr(755,root,root) %{_bindir}/ma2asm
%attr(755,root,root) %{_bindir}/pl2wam
%attr(755,root,root) %{_bindir}/wam2ma
%dir %{_libdir}/%{name}-%{version}
%dir %{_libdir}/%{name}-%{version}/bin
%attr(755,root,root) %{_libdir}/%{name}-%{version}/bin/*
%{_libdir}/%{name}-%{version}/include
%{_libdir}/%{name}-%{version}/lib

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

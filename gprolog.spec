Summary:	GNU Prolog is a free Prolog compiler with constraint solving over Finite Domains
Summary(pl):	GNU Prolog jest darmowym kompilatorem jêzyka Prolog
Name:		gprolog
Version:	1.2.1
Release:	1
License:	GPL
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Source0:	ftp://ftp.inria.fr/Projects/loco/gprolog/%{name}-%{version}.tar.gz
URL:		http://gprolog.inria.fr/
ExclusiveArch:	%{ix86}
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl
GNU Prolog jest bezpo¶rednim kompilatorem Prolog-u z narzuconymi
ograniczeniami ponad "finite domains (FD)" tworzonym przez Daniela
Diaz (http://loco.inria.fr/~diaz/)

GNU Prolog jest bardzo efektywnym bezpo¶rednim kompilatorem tworzo±cym
ma³e samodzielne programy wykonywalne. GNU-Prolog oferuje te¿
klasyczny interfejst wysokiego poziomu oraz debugger.

GNU Prolog jest zgodny z standardem ISO jêzyka Prolog oraz oferuje
dodatkowo kilka rozszerzeñ (zmienne globalne, DCG, gniazdka, interfejs
do systemu operacyjnego, ...).

GNU Prolog zawiera te¿ porêczny solver finite domains z wieloma
predefiniowanymi ograniczaczami i heurestykami.

%prep
%setup -q

%build
cd src
%configure \
	--with-install-dir=$RPM_BUILD_ROOT/%{_libdir}/%{name}-%{version} \
	--with-c-flags="%{rpmcflags}" \
	--without-links-dir \
	--without-examples-dir \
	--without-doc-dir \
	--without-html-dir
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
cd src
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
install -d $RPM_BUILD_ROOT/%{_bindir}
cd $RPM_BUILD_ROOT/%{_libdir}/%{name}-%{version}/bin
for i in *; do
 	ln -s ../lib/%{name}-%{version}/bin/$i $RPM_BUILD_ROOT/%{_bindir}/$i
done
)

cd ..
gzip -9nf ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%attr(755,root,root) %{_bindir}/*
%dir %attr(755,root,root) %{_libdir}/%{name}-%{version}/
%attr(755,root,root) %{_libdir}/%{name}-%{version}/bin/*
%{_libdir}/%{name}-%{version}/include
%{_libdir}/%{name}-%{version}/lib

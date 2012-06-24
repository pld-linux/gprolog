Summary:	GNU Prolog is a free Prolog compiler with constraint solving over Finite Domains
Summary(pl):	GNU Prolog jest darmowym kompilatorem j�zyka Prolog
Name:		gprolog
Version:	1.2.8
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	ftp://ftp.inria.fr//INRIA/Projects/contraintes/gnu-prolog/%{name}-%{version}.tar.gz
URL:		http://gprolog.inria.fr/
ExclusiveArch:	%{ix86}
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

%description -l pl
GNU Prolog jest bezpo�rednim kompilatorem Prolog-u z narzuconymi
ograniczeniami ponad "finite domains (FD)" tworzonym przez Daniela
Diaz (http://loco.inria.fr/~diaz/)

GNU Prolog jest bardzo efektywnym bezpo�rednim kompilatorem tworzo�cym
ma�e samodzielne programy wykonywalne. GNU-Prolog oferuje te�
klasyczny interfejst wysokiego poziomu oraz debugger.

GNU Prolog jest zgodny z standardem ISO j�zyka Prolog oraz oferuje
dodatkowo kilka rozszerze� (zmienne globalne, DCG, gniazdka, interfejs
do systemu operacyjnego, ...).

GNU Prolog zawiera te� por�czny solver finite domains z wieloma
predefiniowanymi ograniczaczami i heurestykami.

%package doc-ps
Summary:	PostScript documentation for GNU Prolog
Summary(pl):	Dokumentacja dla GNU Prolog w formacie PostSript
Group:		Development/Tools
Requires:	%{name} = %{version}

%description doc-ps
PostScript documentation for GNU Prolog

%description doc-ps -l pl
Dokumentacja dla GNU Prolog w formacie PostSript

%package doc-pdf
Summary:	PDF documentation for GNU Prolog
Summary(pl):	Dokumentacja dla GNU Prolog w formacie PDF
Group:		Development/Tools
Requires:	%{name} = %{version}

%description doc-pdf
PDF documentation for GNU Prolog

%description doc-pdf -l pl
Dokumentacja dla GNU Prolog w formacie PDF

%package doc-html
Summary:	HTML documentation for GNU Prolog
Summary(pl):	Dokumentacja dla GNU Prolog w formacie HTML
Group:		Development/Tools
Requires:	%{name} = %{version}

%description doc-html
HTML documentation for GNU Prolog

%description doc-html -l pl
Dokumentacja dla GNU Prolog w formacie HTML

%prep
%setup -q

%build
cd src
aclocal
%{__autoconf}
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

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -ar Examples* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf ChangeLog NEWS README doc/manual.ps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%dir %attr(755,root,root) %{_libdir}/%{name}-%{version}/
%attr(755,root,root) %{_libdir}/%{name}-%{version}/bin/*
%{_libdir}/%{name}-%{version}/include
%{_libdir}/%{name}-%{version}/lib
%{_examplesdir}/%{name}-%{version}

%files doc-html
%defattr(644,root,root,755)
%doc doc/Html

%files doc-ps
%defattr(644,root,root,755)
%doc doc/manual.ps.gz

%files doc-pdf
%defattr(644,root,root,755)
%doc doc/manual.pdf

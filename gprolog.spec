Summary:	GNU Prolog is a free Prolog compiler with constraint solving over Finite Domains
Name:		gprolog
Version:	1.2.1
Release:	1
License:	GPL
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Source0:	ftp://ftp.inria.fr/Projects/loco/gprolog/%{name}-%{version}.tar.gz
URL:		http://gprolog.inria.fr/
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}

%description 

GNU Prolog is a native Prolog compiler with constraint solving over
finite domains (FD) developed by Daniel Diaz
(http://loco.inria.fr/~diaz).

GNU Prolog is a very efficient native compiler producing (small)
stand-alone executables. GNU-Prolog also offers a classical
top-level+debugger.

GNU Prolog conforms to the ISO standard for Prolog but also includes a
lot of extensions (global variables, DCG, sockets, OS interface,...).

GNU Prolog also includes a powerful constraint solver over finite
domains with many predefined constraints+heuristics.

More information can be found at http://www.gnu.org/software/prolog or
better at http://gprolog.inria.fr.


%prep
%setup -q

%build
cd src
%configure --with-install-dir=$RPM_BUILD_ROOT/%{_libdir}/%{name}-%{version} \
            --without-links-dir --without-examples-dir \
--with-doc-dir=$RPM_BUILD_ROOT%{_datadir}/doc/%{name}-%{version}
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
cd src
%{__make} install
install -d $RPM_BUILD_ROOT/%{_bindir}
cd $RPM_BUILD_ROOT/%{_libdir}/%{name}-%{version}/bin
for i in *; do
	ln -s ../lib/%{name}-%{version}/bin/$i $RPM_BUILD_ROOT/%{_bindir}/$i
done
cd $RPM_BUILD_DIR/%{name}-%{version}
gzip -9nf COPYING ChangeLog NEWS README

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

#
%bcond_without	doc		# build without documentation
#
Summary:		Advanced commandline hexadecimal editor
Summary(pl.UTF-8):	Zaawansowany edytor szesnastkowy obsługiwany z linii poleceń
Name:			radare
Version:		1.0b
Release:		0.1
License:		GPL
Group:			Applications
Source0:		http://radare.nopcode.org/get/%{name}-%{version}.tar.gz
# Source0-md5:	68175e48964ee07ca58a16a8137f20d9
%if %{with doc}
Source1:		http://radare.nopcode.org/get/%{name}.pdf
# Source1-md5:	cb8ccb676e859680467ec6e058738a50
%endif
Patch0:			%{name}-paths.patch
Patch1:			%{name}-lua51.patch
Patch2:			%{name}-buildfails.patch
URL:			http://radare.nopcode.org/
BuildRequires:	readline-devel
BuildRequires:	vala >= 0.3.4
BuildRequires:	lua51-devel
BuildRequires:	libewf-devel
BuildRoot:		%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The project aims to create a complete free *nix-like toolchain for working with binary files.

Its core is a commandline block-based hexadecimal editor which handles everything as a file.
A process, file, disk, memory... This flexibility offers nice scripting features which can
be mixed with Lua, Lisp, Perl, Python and Vala.

%description -l pl.UTF-8
Celem projektu jest stworzenie kompletnego i darmowego zestawu narzędzi do pracy z plikami
binarnymi.

Rdzeniem jest blokowy edytor szesnastkowy obsługiwany z linii poleceń, który obsługuje
wszystkie rodzaje danych jak pliki. Procesy, pliki, dyski, pamięć... Ta elastyczność
pozwala na łatwe tworzenie skryptów w językach takich jak Lua, Lisp, Perl, Vala.

%if %{with doc}
%package doc
Summary:	Documentation for radare
Summary(pl.UTF-8):	Dokumentacja dla radare
Group:			Applications

%description doc
Documentation for radare.

%description doc -l pl.UTF-8
Dokuemntacja dla radare.
%endif

%prep
#%setup -q -n %{name}-%{release_date}
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# Won't link with --as-needed flag, so we run plain ./configure here
LUA=/usr/bin/lua51 \
./configure --prefix=/usr --exec-prefix=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_docdir}/%{name} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT%{_mandir}
%if %{with doc}
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_libdir}/libfdsniff.so
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*

%files doc
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}

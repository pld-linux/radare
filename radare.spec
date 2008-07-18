Summary:	Advanced commandline hexadecimal editor
Summary(pl.UTF-8):	Zaawansowany edytor szesnastkowy obsługiwany z linii poleceń
Name:		radare
Version:	0.9.7
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://radare.nopcode.org/get/%{name}-%{version}.tar.gz
# Source0-md5:	f346d90cc0fec433b16f646b6c2af091
Patch0:		%{name}-paths.patch
URL:		http://radare.nopcode.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%prep
%setup -q
%patch0

%build
%configure

%{__make} \
	LDFLAGS="-ldl"

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_docdir}/%{name} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_docdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/*
%{_libdir}/libfdsniff.so
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*

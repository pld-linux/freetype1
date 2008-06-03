Summary:	Truetype font rasterizer
Summary(pl.UTF-8):	Rasteryzer fontów Truetype
Name:		freetype1
Version:	1.3.1
Release:	11
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.freetype.org/freetype/freetype1/freetype-%{version}.tar.gz
# Source0-md5:	9a9e7ad00c1ef6dfbf8f8e19ceefb300
Patch0:		freetype-DESTDIR.patch
Patch1:		freetype-autoconf.patch
Patch2:		%{name}-po.patch
Patch3:		freetype-gcc33.patch
URL:		http://www.physiol.med.tu-muenchen.de/~robert/freetype.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The FreeType engine is a free and portable TrueType font rendering
engine. It has been developed to provide TrueType support to a great
variety of platforms and environments.

Note that FreeType is a *library*. It is not a font server for your
favorite platform, even though it was designed to be used in many of
them. Note also that it is *not* a complete text-rendering library.
Its purpose is simply to open and manage font files, as well as load,
hint and render individual glyphs efficiently. You can also see it as
a "TrueType driver" for a higher-level library, though rendering text
with it is extremely easy, as demo-ed by the test programs.

%description -l pl.UTF-8
FreeType jest biblioteką służącą do rasteryzacji fontów TrueType. Jest
to jedynie biblioteka, a nie serwer fontów, chociaż została ona
zaprojektowana do używania także w takich serwerach. Nie jest to też
kompletna biblioteka do rasteryzacji tekstu. Jej celem jest tylko
odczytywanie i zarządzanie plikami z fontami oraz wczytywanie i
wykonywanie hintingu i rasteryzacji poszczególnych glifów. Może być
także uważana za "sterownik TrueType" dla bibliotek wyższego poziomu,
jednak użycie samej biblioteki FreeType do rasteryzacji jest bardzo
proste, co można zobaczyć w programach demonstracyjnych.

%package devel
Summary:	Header files and development documentation
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki freetype i dokumentacja
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	freetype-devel = %{version}

%description devel
This package includes the header files documentations and libraries
necessary to develop applications that use freetype.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe oraz biblioteki niezbędne przy
kompilowaniu programów wykorzystujących bibliotekę freetype.

%package static
Summary:	Freetype static libraries
Summary(pl.UTF-8):	Biblioteki statyczne freetype
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	freetype-static = %{version}

%description static
Static freetype libraries.

%description static -l pl.UTF-8
Biblioteki statyczne freetype.

%package progs
Summary:	Freetype library utilities
Summary(pl.UTF-8):	Programy użytkowe freetype
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Provides:	freetype-progs = %{version}
Obsoletes:	freetype-utils
Obsoletes:	freetype-tools

%description progs
Freetype library utilites:
- ftimer - a simple performance timer for the engine,
- fzoom - very simple glyph viewer,
- ftlint - program will hint each glyph of a font file, at a given
  point size,
- ftwiew - display all glyphs in a given font, applying hinting to
  each one,
- fdump - a simple TrueType font or collection dumper,
- ftstring - a simple program to show off string text generation.
- ftstrpn - convert a rendered text string into the PGM or PBM format,
- fterror - small test program. Tests the gettext() functionality for
  internationalized messages.

%description progs -l pl.UTF-8
Przykładowe aplikacje wykorzystujące freetype:
- ftimer - narzędzie mierzące szybkość silnika
- fzoom - prosta przeglądarka glifów
- ftlint - program robiący hinting każdego glifu z fontu przy podanym
  rozmiarze
- ftview - program wyświetlający z hintingiem wszystkie glify z fontu
- fdump - narzędzie zrzucające dane z fontu lub zestawu fontów TT
- ftstring - prosty program obrazujący generowanie tekstu
- ftstrpn - konwerter zrenderowanego tekstu na format PGM/PBM
- fterror - prosty program testujący działanie gettext() w
  zlokalizowanych komunikatach.

%prep
%setup -q -n freetype-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
install /usr/share/automake/missing .
%{__gettextize}
# gettextize stupidity (doesn't see intl/Makefile in next lines after AC_OUTPUT)
sed -e 's@\(AC_OUTPUT.*\) intl/Makefile@\1@' configure.in > configure.in.tmp
mv -f configure.in.tmp configure.in
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
        --enable-static \
        --with-gnu-ld
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang freetype

# resolve conflict with freetype-demos-2.*
mv -f $RPM_BUILD_ROOT%{_bindir}/{ftdump,ft1dump}
mv -f $RPM_BUILD_ROOT%{_bindir}/{ftlint,ft1lint}
mv -f $RPM_BUILD_ROOT%{_bindir}/{ftview,ft1view}
mv -f $RPM_BUILD_ROOT%{_bindir}/{fttimer,ft1timer}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f freetype.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*so.*.*

%files devel
%defattr(644,root,root,755)
%doc howto/unix.txt README announce docs/{*.txt,FAQ,TODO,credits}
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/f*

Summary:	Truetype font rasterizer
Summary(pl):	Rasteryzer fontów Truetype
Name:		freetype1
Version:	1.3.1
Release:	7
License:	BSD-like
Group:		Libraries
Source0:	ftp://ftp.freetype.org/freetype/freetype1/freetype-%{version}.tar.gz
Patch0:		freetype-DESTDIR.patch
Patch1:		freetype-autoconf.patch
URL:		http://www.physiol.med.tu-muenchen.de/~robert/freetype.html
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
Provides:	freetype = %{version}
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

%description -l pl
FreeType jest bibliotek± s³u¿±c± do rasteryzacji fontów TrueType. Kody
¼ród³owe napisane s± w ANSI C oraz PASCAL'u.

%package devel
Summary:	Header files and development documentation
Summary(pl):	Pliki nag³ówkowe biblioteki freetype i dokumentacja
Group:		Development/Libraries
Requires:	%{name} = %{version}
Provides:	freetype-devel = %{version}

%description devel
This package includes the header files documentations and libraries
necessary to develop applications that use freetype.

%description devel -l pl
Pakiet ten zawiera pliki nag³ówkowe oraz biblioteki niezbêdne przy
kompilowaniu programów wykorzystuj±cych bibliotekê freetype.

%package static
Summary:	Freetype static libraries
Summary(pl):	Biblioteki statyczne freetype
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Provides:	freetype-static = %{version}

%description static
Static freetype libraries.

%description static -l pl
Biblioteki statyczne freetype.

%package progs
Summary:	Freetype library utilities
Summary(pl):	Programy u¿ytkowe freetype
Group:		Applications
Requires:	%{name} = %{version}
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

%description progs -l pl
Przyk³adowe aplikacje wykorzystuj±ce freetype:
- ftimer - narzêdzie mierz±ce szybko¶æ silnika
- fzoom - prosta przegl±darka glifów
- ftlint - program robi±cy hinting ka¿dego glifu z fontu przy podanym
  rozmiarze
- ftview - program wy¶wietlaj±cy z hintingiem wszystkie glify z fontu
- fdump - narzêdzie zrzucaj±ce dane z fontu lub zestawu fontów TT
- ftstring - prosty program obrazuj±cy generowanie tekstu
- ftstrpn - konwerter zrenderowanego tekstu na format PGM/PBM
- fterror - prosty program testuj±cy dzia³anie gettext() w
  zlokalizowanych komunikatach.
  
%prep
%setup -q -n freetype-%{version}
%patch0 -p1
%patch1 -p1

%build
install /usr/share/automake/missing .
%{__gettextize}
%{__libtoolize}
aclocal
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
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/f*

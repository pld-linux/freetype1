Summary:	Truetype font rasterizer
Summary(pl):	Rasteryzer fontÛw Truetype
Name:		freetype1
Version:	1.3.1
Release:	3
License:	BSD like
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	ftp://ftp.freetype.org/freetype/freetype1/freetype-%{version}.tar.gz
Source1:	ttmkfdir.tar.gz
Patch0:		freetype-DESTDIR.patch
Patch1:		freetype-autoconf.patch
Patch2:		freetype-foundrynames.patch
Patch3:		freetype-nospaces.patch
URL:		http://www.physiol.med.tu-muenchen.de/~robert/freetype.html
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
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
FreeType jest bibliotek± s≥uø±c± do rasteryzacji fontÛw TrueType. Kody
ºrÛd≥owe napisane s± w ANSI C oraz PASCAL'u.

%package devel
Summary:	Header files and development documentation
Summary(pl):	Pliki nag≥Ûwkowe biblioteki freetype i dokumentacja
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
This package includes the header files documentations and libraries
necessary to develop applications that use freetype.

%description -l pl devel 
Pakiet ten zawiera pliki nag≥Ûwkowe oraz biblioteki niezbÍdne przy
kompilowaniu programÛw wykorzystuj±cych bibliotekÍ freetype.

%package static
Summary:	Freetype static libraries
Summary(pl):	Biblioteki statyczne freetype
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static freetype libraries.

%description -l pl static 
Biblioteki statyczne freetype.

%package progs
Summary:	Freetype library utilities
Summary(pl):	Programy uøytkowe freetype
Group:		Applications
Group(de):	Applikationen
Group(pl):	Aplikacje
Requires:	%{name} = %{version}
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

%description -l pl progs
Przyk≥adowe aplikacje wykorzystuj±ce freetype.

%prep
%setup -q -n freetype-%{version}
mkdir ttmkfdir
tar xz -C ttmkfdir -f %{SOURCE1}
%patch0 -p1
%patch1 -p1

%build
gettextize --copy --force
libtoolize --copy --force
aclocal
autoconf
%configure \
        --enable-static \
        --with-gnu-ld
%{__make}
%{__make} -C ttmkfdir CC="%{__cc} %{rpmcflags} -I../lib" FREETYPE_LIB='-L../lib/.libs -lttf'

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
install ttmkfdir/ttmkfdir $RPM_BUILD_ROOT%{_bindir}

gzip -9nf howto/unix.txt README announce docs/{*.txt,FAQ,TODO,credits}

%find_lang freetype

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f freetype.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ttmkfdir
%attr(755,root,root) %{_libdir}/lib*so.*.*

%files devel
%defattr(644,root,root,755)
%doc howto/unix* docs/*txt* *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/f*

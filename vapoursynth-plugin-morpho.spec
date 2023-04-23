Summary:	Set of simple morphological filters for Vapoursynth
Summary(pl.UTF-8):	Zestaw prostych filtrów morfologicznych dla programu Vapoursynth
Name:		vapoursynth-plugin-morpho
Version:	1
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/vapoursynth/vs-morpho-obsolete/archive/R%{version}/vs-morpho-obsolete-R%{version}.tar.gz
# Source0-md5:	85ffe26d8fd90e58f669102e6343117a
URL:		https://github.com/vapoursynth/vs-morpho-obsolete
BuildRequires:	libtool >= 2:1.5
BuildRequires:	vapoursynth-devel >= 55
Requires:	vapoursynth >= 55
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A set of simple morphological filters. Useful for working with mask
clips.

%description -l pl.UTF-8
Zbiór prostych filtrów morfologicznych. Przydatne do pracy z
przycinaniem maskami.

%prep
%setup -q -n vs-morpho-obsolete-R%{version}

%build
for f in morpho morpho_filters morpho_selems ; do
	libtool --tag=CC --mode=compile %{__cc} -c -o src/${f}.lo %{rpmcflags} %{rpmcppflags} $(pkg-config --cflags vapoursynth) src/${f}.c
done
libtool --tag=CC --mode=link %{__cc} -shared -module -avoid-version -o src/libmorpho.la %{rpmldflags} %{rpmcflags} src/*.lo -rpath %{_libdir}/vapoursynth

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/vapoursynth

libtool --mode=install install src/libmorpho.la $RPM_BUILD_ROOT%{_libdir}/vapoursynth

%{__rm} $RPM_BUILD_ROOT%{_libdir}/vapoursynth/libmorpho.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE docs/morpho.rst
%attr(755,root,root) %{_libdir}/vapoursynth/libmorpho.so

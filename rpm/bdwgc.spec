Summary: Garbage collector for C and C++
Name:    gc
Version: 8.0.6
Release: 1

License: BSD
URL:     https://www.hboehm.info/gc/
Source0: https://github.com/ivmai/bdwgc/releases/download/v%{version}/gc-%{version}%{?pre}.tar.gz

BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: make

%description
The Boehm-Demers-Weiser conservative garbage collector can be
used as a garbage collecting replacement for C malloc or C++ new.

%package devel
Summary: Libraries and header files for %{name} development
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%setup -q -n %name-%{version}/upstream

%build
autoreconf -fi
CPPFLAGS="-DUSE_GET_STACKBASE_FOR_MAIN"; export CPPFLAGS
%configure \
  --disable-docs \
  --disable-single-obj-compilation \
  --enable-cplusplus \
  --enable-large-config \
  --enable-threads=posix
%make_build

%install
%make_install
install -p -D -m644 doc/gc.man  %{buildroot}%{_mandir}/man3/gc.3

## Unpackaged files
rm -rfv %{buildroot}%{_datadir}/gc/
rm -fv  %{buildroot}%{_libdir}/lib*.la

%files
%{_libdir}/libcord.so.1*
%{_libdir}/libgc.so.1*
%{_libdir}/libgctba.so.1*
%{_libdir}/libgccpp.so.1*

%files devel
%doc doc/README.environment doc/README.linux
%doc doc/*.md
%{_includedir}/gc.h
%{_includedir}/gc_cpp.h
%{_includedir}/gc/
%{_libdir}/libcord.so
%{_libdir}/libgc.so
%{_libdir}/libgctba.so
%{_libdir}/libgccpp.so
%{_libdir}/pkgconfig/bdw-gc.pc
%{_mandir}/man3/gc.3*

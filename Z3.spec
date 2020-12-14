#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Z3
Version  : 4.8.9
Release  : 25
URL      : https://github.com/Z3Prover/z3/archive/z3-4.8.9/z3-4.8.9.tar.gz
Source0  : https://github.com/Z3Prover/z3/archive/z3-4.8.9/z3-4.8.9.tar.gz
Summary  : .NET bindings for The Microsoft Z3 SMT solver
Group    : Development/Tools
License  : MIT
Requires: Z3-bin = %{version}-%{release}
Requires: Z3-lib = %{version}-%{release}
Requires: Z3-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : doxygen
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : python3

%description
muZ: routines related to solving satisfiability of Horn clauses and
solving Datalog programs.

%package bin
Summary: bin components for the Z3 package.
Group: Binaries
Requires: Z3-license = %{version}-%{release}

%description bin
bin components for the Z3 package.


%package dev
Summary: dev components for the Z3 package.
Group: Development
Requires: Z3-lib = %{version}-%{release}
Requires: Z3-bin = %{version}-%{release}
Provides: Z3-devel = %{version}-%{release}
Requires: Z3 = %{version}-%{release}

%description dev
dev components for the Z3 package.


%package dev32
Summary: dev32 components for the Z3 package.
Group: Default
Requires: Z3-lib32 = %{version}-%{release}
Requires: Z3-bin = %{version}-%{release}
Requires: Z3-dev = %{version}-%{release}

%description dev32
dev32 components for the Z3 package.


%package lib
Summary: lib components for the Z3 package.
Group: Libraries
Requires: Z3-license = %{version}-%{release}

%description lib
lib components for the Z3 package.


%package lib32
Summary: lib32 components for the Z3 package.
Group: Default
Requires: Z3-license = %{version}-%{release}

%description lib32
lib32 components for the Z3 package.


%package license
Summary: license components for the Z3 package.
Group: Default

%description license
license components for the Z3 package.


%prep
%setup -q -n z3-z3-4.8.9
cd %{_builddir}/z3-z3-4.8.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1599853747
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build32
pushd clr-build32
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%cmake -DLIB_INSTALL_DIR:PATH=/usr/lib32 -DCMAKE_INSTALL_LIBDIR=/usr/lib32 -DLIB_SUFFIX=32 ..
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
popd

%install
export SOURCE_DATE_EPOCH=1599853747
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Z3
cp %{_builddir}/z3-z3-4.8.9/LICENSE.txt %{buildroot}/usr/share/package-licenses/Z3/dad4e766bd1dda39916ad6d99a48f02c6884438a
pushd clr-build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/z3

%files dev
%defattr(-,root,root,-)
/usr/include/z3++.h
/usr/include/z3.h
/usr/include/z3_algebraic.h
/usr/include/z3_api.h
/usr/include/z3_ast_containers.h
/usr/include/z3_fixedpoint.h
/usr/include/z3_fpa.h
/usr/include/z3_macros.h
/usr/include/z3_optimization.h
/usr/include/z3_polynomial.h
/usr/include/z3_rcf.h
/usr/include/z3_spacer.h
/usr/include/z3_v1.h
/usr/include/z3_version.h
/usr/lib64/cmake/z3/Z3Config.cmake
/usr/lib64/cmake/z3/Z3ConfigVersion.cmake
/usr/lib64/cmake/z3/Z3Targets-relwithdebinfo.cmake
/usr/lib64/cmake/z3/Z3Targets.cmake
/usr/lib64/libz3.so
/usr/lib64/pkgconfig/z3.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/cmake/z3/Z3Config.cmake
/usr/lib32/cmake/z3/Z3ConfigVersion.cmake
/usr/lib32/cmake/z3/Z3Targets-relwithdebinfo.cmake
/usr/lib32/cmake/z3/Z3Targets.cmake
/usr/lib32/libz3.so
/usr/lib32/pkgconfig/32z3.pc
/usr/lib32/pkgconfig/z3.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libz3.so.4.8
/usr/lib64/libz3.so.4.8.9.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libz3.so.4.8
/usr/lib32/libz3.so.4.8.9.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Z3/dad4e766bd1dda39916ad6d99a48f02c6884438a

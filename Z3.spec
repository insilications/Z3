#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Z3
Version  : 4.8.3
Release  : 11
URL      : https://github.com/Z3Prover/z3/archive/z3-4.8.3.tar.gz
Source0  : https://github.com/Z3Prover/z3/archive/z3-4.8.3.tar.gz
Summary  : .NET bindings for The Microsoft Z3 SMT solver
Group    : Development/Tools
License  : MIT
Requires: Z3-bin = %{version}-%{release}
Requires: Z3-lib = %{version}-%{release}
Requires: Z3-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : cmake
BuildRequires : doxygen
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : openjdk9
BuildRequires : openjdk9-dev
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

%description dev
dev components for the Z3 package.


%package lib
Summary: lib components for the Z3 package.
Group: Libraries
Requires: Z3-license = %{version}-%{release}

%description lib
lib components for the Z3 package.


%package license
Summary: license components for the Z3 package.
Group: Default

%description license
license components for the Z3 package.


%prep
%setup -q -n z3-z3-4.8.3
pushd ..
cp -a z3-z3-4.8.3 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542704806
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export CFLAGS="$CFLAGS -O3 -march=haswell "
export FCFLAGS="$CFLAGS -O3 -march=haswell "
export FFLAGS="$CFLAGS -O3 -march=haswell "
export CXXFLAGS="$CXXFLAGS -O3 -march=haswell "
export CFLAGS="$CFLAGS -march=haswell -m64"
export CXXFLAGS="$CXXFLAGS -march=haswell -m64"
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1542704806
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Z3
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/Z3/LICENSE.txt
pushd clr-build-avx2
%make_install_avx2  || :
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/haswell/z3
/usr/bin/z3

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/cmake/z3/Z3Config.cmake
/usr/lib64/cmake/z3/Z3Targets-relwithdebinfo.cmake
/usr/lib64/cmake/z3/Z3Targets.cmake
/usr/lib64/haswell/libz3.so
/usr/lib64/libz3.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libz3.so.4.8
/usr/lib64/haswell/libz3.so.4.8.3.0
/usr/lib64/libz3.so.4.8
/usr/lib64/libz3.so.4.8.3.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Z3/LICENSE.txt

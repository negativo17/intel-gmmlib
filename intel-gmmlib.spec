Name:           intel-gmmlib
Epoch:          1
Version:        20.1.1
Release:        1%{?dist}
Summary:        Intel Graphics Memory Management Library
License:        MIT and BSD
URL:            https://01.org/linuxmedia/vaapi

Source0:        https://github.com/intel/gmmlib/archive/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
The Intel Graphics Memory Management Library provides device specific and buffer
management for the Intel Graphics Compute Runtime for OpenCL and the Intel Media
Driver for VAAPI.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n gmmlib-%{name}-%{version}

# rpmlint fixes
chmod -x LICENSE.md
find Source -name "*.cpp" -exec chmod -x {} ';'
find Source -name "*.h" -exec chmod -x {} ';'

%build
mkdir build
pushd build
%cmake \
  -DRUN_TEST_SUITE:BOOL=False \
  ..

%make_build
popd

%install
pushd build
%make_install
find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete
popd

%ldconfig_scriptlets

%files
%license LICENSE.md
%{_libdir}/libigdgmm.so.11
%{_libdir}/libigdgmm.so.11.1.0

%files devel
%{_includedir}/igdgmm
%{_libdir}/libigdgmm.so
%{_libdir}/pkgconfig/igdgmm.pc

%changelog
* Tue May 05 2020 Simone Caronni <negativo17@gmail.com> - 1:20.1.1-1
- First build.

%global __cmake_in_source_build 1

Name:           intel-gmmlib
Epoch:          1
Version:        21.1.3
Release:        1%{?dist}
Summary:        Intel Graphics Memory Management Library
License:        MIT and BSD
URL:            https://01.org/linuxmedia/vaapi

Source0:        https://github.com/intel/gmmlib/archive/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++

%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  cmake >= 3.5
%else
BuildRequires:  cmake3 >= 3.5
%endif


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
find . -name "*.cpp" -o -name "*.h" -exec chmod -x {} ';'

%build
mkdir build
pushd build
%if 0%{?fedora} || 0%{?rhel} >= 8
%cmake \
%else
%cmake3 \
%endif
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
%{_libdir}/libigdgmm.so.11.3.0

%files devel
%{_includedir}/igdgmm
%{_libdir}/libigdgmm.so
%{_libdir}/pkgconfig/igdgmm.pc

%changelog
* Wed Jun 23 2021 Simone Caronni <negativo17@gmail.com> - 1:21.1.3-1
- Update to 2021 Q1 Release 3.

* Sun Apr 04 2021 Simone Caronni <negativo17@gmail.com> - 1:21.1.1-1
- Update to 2021 Q1 Release.

* Tue Jan  5 2021 Simone Caronni <negativo17@gmail.com> - 1:20.4.1-1
- Update to 2020 Q4 Release.

* Fri Dec 04 2020 Simone Caronni <negativo17@gmail.com> - 1:20.3.3-1
- Update to 20.3.3.

* Thu Oct 29 2020 Simone Caronni <negativo17@gmail.com> - 1:20.3.2-1
- Update to 2020 Q3 Release 2.

* Tue May 05 2020 Simone Caronni <negativo17@gmail.com> - 1:20.1.1-1
- First build.

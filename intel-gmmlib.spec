%undefine       __cmake_in_source_build

Name:           intel-gmmlib
Epoch:          1
Version:        22.7.2
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
find . -name "*.cpp" -o -name "*.h" -exec chmod -x {} ';'

%build
%cmake -DRUN_TEST_SUITE:BOOL=False
%cmake_build

%install
%cmake_install

find %{buildroot} -name '*.la' -delete
find %{buildroot} -name '*.a' -delete

%files
%license LICENSE.md
%{_libdir}/libigdgmm.so.12
%{_libdir}/libigdgmm.so.12.7.0

%files devel
%{_includedir}/igdgmm
%{_libdir}/libigdgmm.so
%{_libdir}/pkgconfig/igdgmm.pc

%changelog
* Mon Jun 23 2025 Simone Caronni <negativo17@gmail.com> - 1:22.7.2-1
- Update to 22.7.2.

* Wed Apr 16 2025 Simone Caronni <negativo17@gmail.com> - 1:22.7.1-1
- Update to 22.7.1.

* Mon Mar 17 2025 Simone Caronni <negativo17@gmail.com> - 1:22.7.0-1
- Update to 22.7.0.

* Fri Dec 27 2024 Simone Caronni <negativo17@gmail.com> - 1:22.6.0-1
- Update to 22.6.0.

* Thu Nov 28 2024 Simone Caronni <negativo17@gmail.com> - 1:22.5.4-1
- Update to 22.5.4.

* Tue Sep 10 2024 Simone Caronni <negativo17@gmail.com> - 1:22.5.2-1
- Update to 22.5.2.

* Sun Aug 18 2024 Simone Caronni <negativo17@gmail.com> - 1:22.5.0-1
- Update to 22.5.0.

* Thu Jul 04 2024 Simone Caronni <negativo17@gmail.com> - 1:22.4.1-1
- Update to 22.4.1.
- Trim changelog.

* Thu Jun 06 2024 Simone Caronni <negativo17@gmail.com> - 1:22.3.20-1
- Update to 22.3.20.

* Mon Apr 15 2024 Simone Caronni <negativo17@gmail.com> - 1:22.3.19-1
- Update to 22.3.19.

* Wed Mar 20 2024 Simone Caronni <negativo17@gmail.com> - 1:22.3.18-1
- Update to 22.3.18.

* Thu Jan 25 2024 Simone Caronni <negativo17@gmail.com> - 1:22.3.17-1
- Update to 22.3.17.

* Mon Jan 08 2024 Simone Caronni <negativo17@gmail.com> - 1:22.3.16-1
- Update to 22.3.16.

* Thu Dec 14 2023 Simone Caronni <negativo17@gmail.com> - 1:22.3.15-1
- Update to 22.3.15.

* Wed Nov 15 2023 Simone Caronni <negativo17@gmail.com> - 1:22.3.13-1
- Update to 22.3.13.

* Fri Sep 29 2023 Simone Caronni <negativo17@gmail.com> - 1:22.3.12-1
- Update to 22.3.12.

* Sun Aug 20 2023 Simone Caronni <negativo17@gmail.com> - 1:22.3.10-1
- Update to 22.3.10.

* Mon Jul 17 2023 Simone Caronni <negativo17@gmail.com> - 1:22.3.9-1
- Update to 22.3.9.

* Tue Apr 11 2023 Simone Caronni <negativo17@gmail.com> - 1:22.3.5-1
- Update to 22.3.5.

* Fri Feb 24 2023 Simone Caronni <negativo17@gmail.com> - 1:22.3.4-1
- Update to 22.3.4.

* Thu Jan 26 2023 Simone Caronni <negativo17@gmail.com> - 1:22.3.3-1
- Update to 22.3.3.

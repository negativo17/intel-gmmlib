Name:           intel-gmmlib
Epoch:          1
Version:        22.3.20
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
%{_libdir}/libigdgmm.so.12.3.0

%files devel
%{_includedir}/igdgmm
%{_libdir}/libigdgmm.so
%{_libdir}/pkgconfig/igdgmm.pc

%changelog
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

* Tue Dec 13 2022 Simone Caronni <negativo17@gmail.com> - 1:22.3.2-1
- Update to 22.3.2.

* Fri Nov 18 2022 Simone Caronni <negativo17@gmail.com> - 1:22.3.1-1
- Update to 22.3.1.

* Mon Oct 24 2022 Simone Caronni <negativo17@gmail.com> - 1:22.3.0-1
- Update to 22.3.0.

* Tue Oct 04 2022 Simone Caronni <negativo17@gmail.com> - 1:22.2.0-1
- Update to 22.2.0.

* Sun Sep 04 2022 Simone Caronni <negativo17@gmail.com> - 1:22.1.8-1
- Update to 22.1.8.

* Thu Jul 21 2022 Simone Caronni <negativo17@gmail.com> - 1:22.1.7-1
- Update to 22.1.7.

* Mon Jul 04 2022 Simone Caronni <negativo17@gmail.com> - 1:22.1.4-1
- Update to 22.1.4.

* Wed May 25 2022 Simone Caronni <negativo17@gmail.com> - 1:22.1.3-1
- Update to 22.1.3.

* Mon Apr 04 2022 Simone Caronni <negativo17@gmail.com> - 1:22.1.2-2
- Split out configuration for different branches.

* Wed Mar 30 2022 Simone Caronni <negativo17@gmail.com> - 1:22.1.2-1
- Update to 22.1.2.

* Sat Mar 19 2022 Simone Caronni <negativo17@gmail.com> - 1:22.1.1-1
- Update to 22.1.1.

* Wed Mar 02 2022 Simone Caronni <negativo17@gmail.com> - 1:22.0.3-1
- Update to 22.0.3.

* Thu Feb 03 2022 Simone Caronni <negativo17@gmail.com> - 1:22.0.2-1
- Update to 22.0.2.

* Mon Dec 27 2021 Simone Caronni <negativo17@gmail.com> - 1:21.3.5-1
- Update to 21.3.5.

* Mon Oct 25 2021 Simone Caronni <negativo17@gmail.com> - 1:21.3.2-1
- Update to Intel Graphics Memory Management Library 2021 Q3 Release 2.

* Sat Sep 04 2021 Simone Caronni <negativo17@gmail.com> - 1:21.2.2-1
- Update to Intel Graphics Memory Management Library 2021 Q2 Release 2.

* Sun Aug 15 2021 Simone Caronni <negativo17@gmail.com> - 1:21.2.1-1
- Update to 21.2.1.

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

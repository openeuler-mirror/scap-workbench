Name:           scap-workbench
Version:        1.2.1
Release:        2
Summary:        Scanning, tailoring, editing and validation tool for SCAP content
License:        GPLv3+
URL:            http://www.open-scap.org/tools/scap-workbench
Source0:        https://github.com/OpenSCAP/scap-workbench/releases/download/%{version}/scap-workbench-%{version}.tar.bz2
Patch1:         Use-QT-provided-macro-function-to-version-check-depr.patch
Patch2:         Replace-obsolete-QString-SkipEmptyParts.patch
Patch3:         Do-not-set-rpath.patch

BuildRequires:  cmake >= 2.6 qt5-devel >= 5.0.0 openscap-devel >= 1.2.11 qt5-qtbase-devel >= 5.0.0 qt5-qtxmlpatterns-devel >= 5.0.0
BuildRequires:  openscap-utils >= 1.2.11 openssh-clients util-linux asciidoc
Requires:       openscap-utils >= 1.2.11 openssh-clients openssh-askpass
Requires:       util-linux polkit scap-security-guide font(:lang=en)

%description
SCAP Workbench is a GUI tool that provides scanning, tailoring and
validation functionality for SCAP content. It uses openscap library
to access SCAP functionalities.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
%if "%toolchain" == "clang"
	export CFLAGS="$CFLAGS -Wno-error=range-loop-construct -Wno-error=range-loop-construct"
	export CXXFLAGS="$CXXFLAGS -Wno-error=range-loop-construct -Wno-error=range-loop-construct"
%endif
%cmake -D CMAKE_INSTALL_DOCDIR=%{_pkgdocdir} .
%make_build

%install
%make_install

%files
%defattr(-,root,root)
%license COPYING win32-LICENSE.rtf
%{_bindir}/scap-workbench
%{_libexecdir}/*.sh
%{_datadir}/pixmaps/*
%{_datadir}/scap-workbench/*
%{_datadir}/appdata/scap-workbench.appdata.xml
%{_datadir}/applications/scap-workbench.desktop
%{_datadir}/polkit-1/actions/scap-workbench-oscap.policy
%exclude %{_pkgdocdir}/COPYING

%files help
%defattr(-,root,root)
%doc %{_pkgdocdir}/README.md
%doc %{_pkgdocdir}/user_manual.html
%{_mandir}/man8/scap-workbench.8.gz

%changelog
* Thu May 18 2023 yoo <sunyuechi@iscas.ac.cn> - 1.2.1-2
- fix clang build error

* Wed Feb 16 2022 chenchen <chen_aka_jan@163.com> - 1.2.1-1
- Update to 1.2.1

* Mon Nov 25 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.2.0-2
- Package init

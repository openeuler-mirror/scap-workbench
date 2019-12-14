Name:           scap-workbench
Version:        1.2.0
Release:        2
Summary:        Scanning, tailoring, editing and validation tool for SCAP content
License:        GPLv3+
URL:            http://www.open-scap.org/tools/scap-workbench
Source0:        https://github.com/OpenSCAP/scap-workbench/releases/download/%{version}/scap-workbench-%{version}.tar.bz2

BuildRequires:  cmake >= 2.6 qt5-devel >= 5.0.0 openscap-devel >= 1.2.11
BuildRequires:  openscap-utils >= 1.2.11 openssh-clients util-linux
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
* Mon Nov 25 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.2.0-2
- Package init

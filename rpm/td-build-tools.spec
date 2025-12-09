Name: td-build-tools
Version: 0.3.1
Release: 1
Summary: Build tools
Group: Applications/System
License: GPL-3.0-or-later
URL: https://www.nntb.no/~dreibh/td-build-tools/
Source: https://www.nntb.no/~dreibh/td-build-tools/download/%{name}-%{version}.tar.xz

AutoReqProv: on
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRoot: %{_tmppath}/%{name}-%{version}-build

BuildArch: noarch
Requires: %{name}-build-tool = %{version}-%{release}
Requires: %{name}-version-bump = %{version}-%{release}


%description
Build Tool is a tool to help creating and maintaining package
builds for Debian/Ubuntu, Fedora, FreeBSD and other systems.
It performs the following tasks:
creating a source tarball,
creating a source package (Debian/Ubuntu, Fedora, etc.),
building binary packages from the source package (including
cross-architecture builds).
This package is a metapackage for the build tools.


%prep
%setup -q

%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr
%cmake_build

%install
%cmake_install

%files


%package build-tool
Summary: Build Tool
BuildArch: noarch
Requires: mock
Requires: python3 >= 3.9
Requires: python3-distro
Requires: python3-urllib3
Requires: rpm
Requires: rpmlint
Recommends: td-system-info
Recommends: td-system-maintenance

%description build-tool
Build Tool is a tool to help creating and maintaining package
builds for Debian/Ubuntu, Fedora, FreeBSD and other systems.
It performs the following tasks:
creating a source tarball,
creating a source package (Debian/Ubuntu, Fedora, etc.),
building binary packages from the source package (including
cross-architecture builds).

%files build-tool
%{_bindir}/build-tool
%{_datadir}/bash-completion/completions/build-tool
%{_datadir}/build-tools/pbuilderrc
%{_mandir}/man1/build-tool.1.gz


%package version-bump
Summary: Version Bump
BuildArch: noarch
Requires: python3 >= 3.9
Requires: python3-distro
Requires: python3-urllib3
Recommends: %{name}-build-tool = %{version}-%{release}

%description version-bump
Version Bump is a tool to help creating versioned packages
with Git and Build Tool.

%files version-bump
%{_bindir}/version-bump
%{_datadir}/bash-completion/completions/version-bump
%{_mandir}/man1/version-bump.1.gz


%changelog
* Tue Dec 09 2025 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 0.3.1-1
- New upstream release.
* Mon Dec 08 2025 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 0.3.0-1
- New upstream release.
* Fri Nov 28 2025 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 0.2.0-1
- New upstream release.
* Wed Nov 26 2025 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 0.1.4-1
- New upstream release.
* Sun Sep 21 2025 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 0.1.3-1
- New upstream release.
* Wed Jul 09 2025 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 0.1.2
- New upstream release.
* Tue Apr 01 2025 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 0.1.1
- New upstream release.
* Thu Feb 27 2025 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 0.1.0
- New upstream release.
* Fri Dec 13 2024 Thomas Dreibholz <thomas.dreibholz@gmail.com> - 0.0.0
- New upstream release.
* Thu Nov 21 2024 Thomas Dreibholz <dreibh@simula.no> - 0.0.0~alpha4
- Created RPM package.

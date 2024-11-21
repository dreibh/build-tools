Name: td-build-tools
Version: 0.0.0~alpha5
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
Requires: mock
Requires: rpm
Requires: rpmlint

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
%{_mandir}/man1/build-tool.1.gz


%package version-bump
Summary: Version Bump
Recommends: %{name}-build-tool = %{version}-%{release}

%description version-bump
Version Bump is a tool to help creating versioned packages
with Git and Build Tool.

%files version-bump
%{_bindir}/version-bump
%{_datadir}/bash-completion/completions/version-bump
%{_mandir}/man1/version-bump.1.gz


%changelog
* Thu Nov 21 2024 Thomas Dreibholz <dreibh@simula.no> - 0.0.0~alpha4
- Created RPM package.

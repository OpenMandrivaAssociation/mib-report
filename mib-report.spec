Summary:		A tool to generate packages reports for Rosa, MDV and MGA repos
Name:		mib-report
Version:		0.22
Release:		1
License:		GPLv2+
Group:		System/Configuration/Packaging
Url:		https://github.com/OpenMandrivaAssociation/mib-report
# Self prepared sources: to make a new release change the sources,
# update ChangeLog, urls.txt and globals.h and then repackage
Source0:	%{name}-%{version}.tar.xz
BuildRequires:		qmake5
BuildRequires:		pkgconfig(Qt5Core)
BuildRequires:		pkgconfig(Qt5Gui)
BuildRequires:		pkgconfig(rpm)
BuildRequires:		qmake5
Requires:	curl
Requires:	lynx
Requires:	xz
Requires:	zstd

%description
A tool to generate packages reports and check package versions present in
various distributions. The %{version} version collects references from:
-Rosa 13.
-OpenMandriva Cooker.
-Mageia Cauldron.
-Fedora Rawhide.
-PCLinuxOS.
-Alt Linux Sisyphus.
-OpenSUSE Factory.
-PLD Linux 3.0.
-Gentoo.
-Debian.
-Ubuntu.
In the "--search" mode the program searches for a package in all reference
repositories and displays results in a: "Repository, Version, URL" format.
There is also a "--report" mode, comparing what packages some of the
distributions listed above have at disposal. There are six report modes:
1) mga-mdv: lists packages in Mageia repositories that may be interesting for
   OpenMandriva packagers;
2) mdv-mga: the same as above but for Mageia packagers;
3) mdv-rosa: lists packages in Mandriva repositories that may be interesting
   for ROSA packagers;
4) rosa-mdv: the same as above but for Mandriva;
5) mga-rosa: lists packages in Mageia repositories that may be interesting for
   ROSA packagers;
6) rosa-mga: the same as above but for Mageia packagers.
The report modes produce a table with package names and showing if there are
newer versions of them in other distros. It also gives quick links for their
source and homepages.

%files
%doc COPYING AUTHORS ChangeLog
%{_bindir}/%{name}
%{_bindir}/urls-fetcher
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/blacklist.txt
%{_datadir}/%{name}/urls.txt
%{_datadir}/bash-completion/completions/%{name}

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%qmake_qt5
%make


%install
%make_install INSTALL_ROOT=%{buildroot}

# Rename completion
mv %{buildroot}%{_datadir}/bash-completion/completions/%{name}.completion \
   %{buildroot}%{_datadir}/bash-completion/completions/%{name}

Summary:	KDE interface for PackageKit
Name:	  	kpackagekit
Version:	0.1
Release:	%mkrel 1
License:	GPLv2+
Group:		System/Configuration/Packaging
Source0: 	http://www.kde-apps.org/CONTENT/content-files/84745-kpackagekit-%{version}.tar.bz2
URL:		http://www.kde-apps.org/content/show.php/KPackageKit?content=84745
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdelibs4-devel
BuildRequires:	packagekit-qt-devel >= %version
BuildRequires:	polkit-devel
BuildRequires:	desktop-file-utils
Requires:	packagekit

%description
KDE interface for PackageKit.

%files
%defattr(-,root,root)
%{_kde_bindir}/*
%{_kde_libdir}/kde4/*.so
%{_kde_services}/*.desktop
%{_kde_services}/kded/*.desktop
%{_kde_datadir}/applications/kde4/*.desktop
%{_kde_appsdir}/KPackageKit
%{_kde_appsdir}/kpackagekit

#--------------------------------------------------------------------

%prep
%setup -q -n KPackageKit/KPackageKit

%build
%cmake_kde4
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

desktop-file-install --vendor='' \
	--dir %buildroot%_kde_datadir/applications/kde4 \
	--remove-category='System' \
	--add-category='Settings;PackageManager' \
	%buildroot%_kde_datadir/applications/kde4/*.desktop

%clean
rm -rf $RPM_BUILD_ROOT

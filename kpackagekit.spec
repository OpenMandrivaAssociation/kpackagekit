%define svnrel 949614

Summary:	KDE interface for PackageKit
Name:	  	kpackagekit
Version:	0.4.1.1
Release:	%mkrel 1
License:	GPLv2+
Group:		System/Configuration/Packaging
Source0: 	http://www.kde-apps.org/CONTENT/content-files/84745-kpackagekit-%{version}.tar.bz2
#Source0:	%name-r%{svnrel}.tar.bz2
URL:		http://www.kde-apps.org/content/show.php/KPackageKit?content=84745
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdelibs4-devel
BuildRequires:	packagekit-devel >= 0.4.7
BuildRequires:	polkit-devel
BuildRequires:	desktop-file-utils
Requires:	packagekit >= 0.4.7

%description
KDE interface for PackageKit.

%files
%defattr(-,root,root)
%{_kde_bindir}/*
%{_kde_libdir}/libkpackagekitlib.so
%{_kde_libdir}/kde4/*.so
%{_kde_services}/*.desktop
%{_kde_services}/kded/*.desktop
%{_kde_datadir}/applications/kde4/*.desktop
%{_kde_appsdir}/kpackagekit
%{_kde_libdir}/kde4/libexec/kpackagekitsmarticon
%{_kde_appsdir}/KPackageKitSmartIcon/KPackageKitSmartIcon.notifyrc
%{_datadir}/dbus-1/services/org.kde.KPackageKitSmartIcon.service

#--------------------------------------------------------------------

%prep
%setup -q -n KPackageKit

%build
%cmake_kde4
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

desktop-file-install --vendor='' \
	--dir %buildroot%_kde_datadir/applications/kde4 \
	--remove-category='System' \
	--remove-category='SoftwareManagement' \
	--add-category='Settings;PackageManager' \
	%buildroot%_kde_datadir/applications/kde4/*.desktop

%clean
rm -rf $RPM_BUILD_ROOT

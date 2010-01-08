%define svn 1071623
Summary:	KDE interface for PackageKit
Name:	  	kpackagekit
Version:	0.6.0
Release:	%mkrel 0.%svn.1
License:	GPLv2+
Group:		System/Configuration/Packaging
Source0: 	http://www.kde-apps.org/CONTENT/content-files/%name-%{version}.%svn.tar.bz2
URL:		http://www.kde-apps.org/content/show.php/KPackageKit?content=84745
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdelibs4-devel
BuildRequires:	qt4-qtdbus
BuildRequires:	packagekit-devel >= 0.5.5
BuildRequires:	polkit-devel
BuildRequires:	desktop-file-utils
Requires:	packagekit >= 0.5.5

%description
KDE interface for PackageKit.

%files -f %name.lang
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
%{_datadir}/dbus-1/services/org.freedesktop.PackageKit.service

#--------------------------------------------------------------------

%prep
%setup -q -n %name

%build
%cmake_kde4
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

desktop-file-install --vendor='' \
	--dir %buildroot%_kde_datadir/applications/kde4 \
	--remove-category='System' \
	--add-category='Settings' \
	%buildroot%_kde_datadir/applications/kde4/*.desktop

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

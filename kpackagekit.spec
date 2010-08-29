%define svn 1169414
%define oname KPackageKit

Summary:	KDE interface for PackageKit
Name:		kpackagekit
Version:	0.6.1
Release:	%mkrel 0.%svn.1
License:	GPLv2+
Group:		System/Configuration/Packaging
Source0: 	http://www.kde-apps.org/CONTENT/content-files/%name-%{version}.%svn.tar.bz2
Patch0:		PackageKit-0.6.2-fix-minimum-QPackageKit.patch
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

%files
%defattr(-,root,root)
%{_kde_bindir}/*
%{_kde_datadir}/applications/kde4/*.desktop
%{_kde_libdir}/kde4/libexec/kpackagekitsmarticon
%{_kde_appsdir}/KPackageKitSmartIcon/KPackageKitSmartIcon.notifyrc
%{_datadir}/dbus-1/services/org.kde.KPackageKitSmartIcon.service

#--------------------------------------------------------------------

%package    common
Summary:    Common files and services for KDE PackageKit
Group:      System/Configuration/Packaging
Requires:   packagekit >= 0.5.5
Provides:   packagekit-gui
Conflicts:  gnome-packagekit < 2.29.2
Conflicts:  kpackagekit < 0.6.0-0.1071623.2

%description common
Common files and services used by KDE PackageKit. This packages provides
Bus service for packages installation.

%files common -f %name.lang
%defattr(-, root, root)
%{_kde_libdir}/kde4/*.so
%{_kde_services}/kded/kpackagekitd.desktop
%{_kde_services}/*.desktop
%{_kde_appsdir}/kpackagekit
%{_kde_libdir}/libkpackagekitlib.so
%{_datadir}/dbus-1/services/kde-org.freedesktop.PackageKit.service

#--------------------------------------------------------------------

%prep
%setup -q -n %name

# .deb can't be installed in Mandriva
sed -i 's,application/x-deb;,,' Desktop/kpackagekit.desktop

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

# hack around gnome-packagekit conflict
mv $RPM_BUILD_ROOT%{_datadir}/dbus-1/services/org.freedesktop.PackageKit.service \
$RPM_BUILD_ROOT%{_datadir}/dbus-1/services/kde-org.freedesktop.PackageKit.service 

%check
desktop-file-validate $RPM_BUILD_ROOT%{_kde_datadir}/applications/kde4/kpackagekit.desktop 

%clean
rm -rf $RPM_BUILD_ROOT

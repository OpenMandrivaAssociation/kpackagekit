%define oname KPackageKit

Summary:	KDE interface for PackageKit
Name:		kpackagekit
Version:	0.6.3.3
Release:	6
License:	GPLv2+
Group:		System/Configuration/Packaging
Source0: 	http://opendesktop.org/CONTENT/content-files/84745-%{name}-%{version}.tar.bz2
URL:		http://www.kde-apps.org/content/show.php/KPackageKit?content=84745
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	kdelibs4-devel
BuildRequires:	qt4-qtdbus
BuildRequires:	packagekit-devel >= 0.6.11
BuildRequires:	polkit-devel
BuildRequires:	desktop-file-utils
Requires:	packagekit >= 0.6.11
Requires:	qt4-database-plugin-sqlite

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
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

desktop-file-install --vendor='' \
	--dir %buildroot%_kde_datadir/applications/kde4 \
	--remove-category='System' \
	--add-category='Settings' \
	--remove-mime-type='application/x-deb' \
	%buildroot%_kde_datadir/applications/kde4/*.desktop

%find_lang %name

# hack around gnome-packagekit conflict
mv $RPM_BUILD_ROOT%{_datadir}/dbus-1/services/org.freedesktop.PackageKit.service \
$RPM_BUILD_ROOT%{_datadir}/dbus-1/services/kde-org.freedesktop.PackageKit.service 

%changelog
* Sun May 22 2011 Funda Wang <fwang@mandriva.org> 0.6.3.3-3mdv2011.0
+ Revision: 677270
- requires sqlite dbdriver

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.3.3-2
+ Revision: 666042
- mass rebuild

* Wed Jan 05 2011 Funda Wang <fwang@mandriva.org> 0.6.3.3-1mdv2011.0
+ Revision: 628805
- update to new version 0.6.3.3

* Thu Dec 23 2010 Funda Wang <fwang@mandriva.org> 0.6.3.2-1mdv2011.0
+ Revision: 624078
- update to new version 0.6.3.2

* Wed Dec 22 2010 Funda Wang <fwang@mandriva.org> 0.6.3-1mdv2011.0
+ Revision: 623778
- new version 0.6.3

* Wed Oct 06 2010 Funda Wang <fwang@mandriva.org> 0.6.2-1mdv2011.0
+ Revision: 583597
- New version 0.6.2

* Sun Aug 29 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.6.1-0.1169414.1mdv2011.0
+ Revision: 574083
- New snapshot

* Fri Aug 27 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.6.0-3mdv2011.0
+ Revision: 573478
- remove application/x-deb from .desktop file, it can't be installed on Mandriva

* Sat Mar 27 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.6.0-2mdv2010.1
+ Revision: 528106
- Rebuild because of broken BS
- Update to 0.6.0 final
  add %%check section ( From kde4 policy )
  Fix conflict with gnome-packagekit
  Fix minimum QPackagekit required version

* Thu Feb 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.6.0-0.1085322.1mdv2010.1
+ Revision: 501004
- New snapshot

* Tue Feb 02 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.6.0-0.1071623.3mdv2010.1
+ Revision: 499573
- Rebuild against new packagekit
- Split kpackagekit and add a common one

* Fri Jan 08 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.6.0-0.1071623.1mdv2010.1
+ Revision: 487551
- New snapshot ( which build with pk 0.6.0)

* Tue Dec 08 2009 Funda Wang <fwang@mandriva.org> 0.5.2-1mdv2010.1
+ Revision: 474767
- fix file list
- drop patch0
- bump req
- use tbz
- new version 0.5.2

* Wed Nov 18 2009 Funda Wang <fwang@mandriva.org> 0.5.1.1-1mdv2010.1
+ Revision: 467203
- new version 0.5.1.1

* Thu Nov 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.5.0.3-2mdv2010.1
+ Revision: 465244
- Rebuild against new Qt

* Fri Nov 06 2009 Funda Wang <fwang@mandriva.org> 0.5.0.3-1mdv2010.1
+ Revision: 460647
- New version 0.5.0.3

* Thu Aug 13 2009 Funda Wang <fwang@mandriva.org> 0.4.2-1mdv2010.0
+ Revision: 415890
- fix build
- new version 0.4.2

* Sun Aug 09 2009 Funda Wang <fwang@mandriva.org> 0.4.1.1-2mdv2010.0
+ Revision: 412911
- rebuild for new pacakgekit

* Thu Jun 11 2009 Funda Wang <fwang@mandriva.org> 0.4.1.1-1mdv2010.0
+ Revision: 385016
- New version 0.4.1.1

* Fri Jun 05 2009 Funda Wang <fwang@mandriva.org> 0.4.1-1mdv2010.0
+ Revision: 382953
- New version 0.4.1
- New snapshot

* Sat Feb 07 2009 Funda Wang <fwang@mandriva.org> 0.3.1-2.922951.1mdv2009.1
+ Revision: 338429
- New snapshot

* Tue Feb 03 2009 Funda Wang <fwang@mandriva.org> 0.3.1-2.920670.2mdv2009.1
+ Revision: 336979
- new snapshot

* Fri Nov 28 2008 Funda Wang <fwang@mandriva.org> 0.3.1-2.887877.2mdv2009.1
+ Revision: 307374
- rebuild for new packagekit

* Sun Nov 23 2008 Funda Wang <fwang@mandriva.org> 0.3.1-2.887877.1mdv2009.1
+ Revision: 305978
- new snapshot
- New snapshot of kpackagekit
- rebuild for new packagekit

* Thu Oct 16 2008 Funda Wang <fwang@mandriva.org> 0.3.1-1mdv2009.1
+ Revision: 294105
- drop unused category
- New version 0.3.1

* Wed Oct 01 2008 Funda Wang <fwang@mandriva.org> 0.1-1mdv2009.0
+ Revision: 290289
- fix fiile list
- spcify correct desktop file category
- 0.1 final

* Tue Aug 19 2008 Funda Wang <fwang@mandriva.org> 0.1-0.b4.1mdv2009.0
+ Revision: 273683
- update file list
- New version 0.1 b4

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix specfile layout  according to kde policy

* Sun Jul 13 2008 Funda Wang <fwang@mandriva.org> 0.1-0.b3.1mdv2009.0
+ Revision: 234366
- import kpackagekit



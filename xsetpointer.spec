Name: xsetpointer
Version: 1.0.1
Release: 14
Summary: Set an X Input device as the main pointer
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xi) >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: x11-proto-devel >= 1.0.3-3mdv

%description
Xsetpointer sets an XInput device as the main pointer.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

#

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xsetpointer
%{_mandir}/man1/xsetpointer.1x*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-7mdv2011.0
+ Revision: 671365
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-6mdv2011.0
+ Revision: 608240
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-5mdv2010.1
+ Revision: 524467
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.1-4mdv2009.1
+ Revision: 350774
- rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-3mdv2009.0
+ Revision: 226078
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-2mdv2008.1
+ Revision: 154301
- Updated BuildRequires and resubmit package.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.1-1mdv2008.1
+ Revision: 130541
- kill re-definition of %%buildroot on Pixel's request
- do not hardcode lzma extension!!!


* Tue Nov 21 2006 Thierry Vignaud <tvignaud@mandriva.com> 1.0.1-1mdv2007.0
+ Revision: 85932
- bump requires for newer input proto
- new release
- fill in a few more missing descriptions

  + Gustavo Pichorim Boiko <boiko@mandriva.com>
    - rebuild to fix cooker uploading
    - increment release
    - Adding X.org 7.0 to the repository

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway


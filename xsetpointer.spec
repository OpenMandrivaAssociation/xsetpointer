Name: xsetpointer
Version: 1.0.1
Release: %mkrel 2
Summary: Set an X Input device as the main pointer
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-util-macros	>= 1.1.5
BuildRequires: libx11-devel	>= 1.1.3
BuildRequires: libxi-devel	>= 1.1.3

%description
Xsetpointer sets an XInput device as the main pointer.

%prep
%setup -q -n %{name}-%{version}

%build
%configure	--x-includes=%{_includedir}\
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

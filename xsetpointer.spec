Name: xsetpointer
Version: 1.0.1
Release: 21
Summary: Set an X Input device as the main pointer
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xi) >= 1.0.0
BuildRequires: pkgconfig(xfixes)
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
%makeinstall_std

%files
%{_bindir}/xsetpointer
%{_mandir}/man1/xsetpointer.1x*

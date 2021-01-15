%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          3dcanvas
Summary:       A 3-D Canvas Widget For Tcl/Tk
Version:       1.2.4
Release:       1
License:       BSD-3-Clause
Group:         Development/Libraries/Tcl
Source:        3dcanvas-1.2.4.tar.gz
URL:           http://3dcanvas.tcl.tk/index.html/doc/tip/doc/index.wiki
BuildRequires: autoconf
BuildRequires: make
BuildRequires: tcl-devel >= 8.6
BuildRequires: tk-devel >= 8.6
BuildRequires: Mesa-libGL-devel
Requires:      tcl >= 8.6
Requires:      tk >= 8.6
Requires:      Mesa-libGL1
BuildRoot:     %{buildroot}

%description
The 3-D Canvas Widget provides Tk programs with 3-D graphics capabilities
through the use of OpenGL. But the 3-D Canvas widget is not another thin
wrapper around the OpenGL interface.

This widget is a much higher-level abstraction. Just as the built-in canvas
widget of Tk is a high-level abstraction of the X11 drawing routines, so too
the 3-D Canvas widget is a high-level abstraction of OpenGL.

%prep
%setup -q -n %{name}-%{version}

%build
./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib} \
%ifarch x86_64
	--enable-64bit=yes \
%endif
	--with-tcl=%{directory}/%{_lib} \
	--with-tk=%{directory}/%{_lib}
make 

%install
make DESTDIR=%{buildroot} pkglibdir=%{tcl_archdir}/%{name}%{version} install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{tcl_archdir}
%{directory}/share/man/mann/canvas3d.n.gz


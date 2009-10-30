%define 	module	pyclutter
Summary:	Clutter Python bindings
Summary(pl.UTF-8):	Dowiązania Pythona dla Cluttera
Name:		python-%{module}
Version:	1.0.0
Release:	1
License:	LGPL v2
Group:		Libraries/Python
Source0:	http://www.clutter-project.org/sources/pyclutter/1.0/%{module}-%{version}.tar.bz2
# Source0-md5:	1cfbb64eceef6828e47e9a64689ffa41
Patch0:		%{name}-buildfix.patch
URL:		http://www.clutter-project.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	clutter-devel >= 1.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-pycairo-devel >= 1.2.0
BuildRequires:	python-pygtk-devel >= 2:2.8.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Clutter Python bindings.

%description -l pl.UTF-8
Dowiązania Pythona dla Cluttera.

%package apidocs
Summary:	pyclutter API documentation
Summary(pl.UTF-8):	Dokumentacja API pyclutter
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
pyclutter API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API pyclutter.

%package devel
Summary:	Header files for pyclutter
Summary(pl.UTF-8):	Pliki nagłówkowe pyclutter
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for pyclutter.

%description devel -l pl.UTF-8
Pliki nagłówkowe pyclutter.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I build/autotools
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT \
	TARGET_DIR=%{_gtkdocdir}/pyclutter

rm -f $RPM_BUILD_ROOT%{py_sitedir}/clutter/*.la

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%dir %{py_sitedir}/clutter
%attr(755,root,root) %{py_sitedir}/clutter/_clutter.so
%{py_sitedir}/clutter/*.py[co]
%{_datadir}/pyclutter

%files devel
%defattr(644,root,root,755)
%{_includedir}/pyclutter-1.0
%{_pkgconfigdir}/pyclutter-1.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/pyclutter

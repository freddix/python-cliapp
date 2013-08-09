Summary:	Python framework for Unix-like command line programs
Name:		python-cliapp
Version:	1.20130808
Release:	1
License:	GPL
Group:		Applications
Source0:	http://code.liw.fi/debian/pool/main/p/python-cliapp/%{name}_%{version}.orig.tar.gz
# Source0-md5:	1ba6cab0430c4a85687b2fa48a646059
URL:		http://liw.fi/cliapp/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python framework for Unix-like command line programs.

%prep
%setup -qn cliapp-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/cliapp
%{py_sitescriptdir}/cliapp/*.py[co]
%{_mandir}/man5/cliapp.5*


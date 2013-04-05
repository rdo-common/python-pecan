# Created by pyp2rpm-1.0.1
%global pypi_name pecan

Name:           python-%{pypi_name}
Version:        0.2.1
Release:        5%{?dist}
Summary:        A lean WSGI object-dispatching web framework

License:        BSD
URL:            http://github.com/dreamhost/pecan
Source0:        http://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

Requires:       python-webob >= 1.2
Requires:       python-simplegeneric >= 0.8
Requires:       python-mako >= 0.4.0
Requires:       python-webtest >= 1.3.1
Requires:       python-argparse
Requires:       python-setuptools

%description
A WSGI object-dispatching web framework, designed to be lean and
fast with few dependencies


%prep
%setup -q -n %{pypi_name}-%{version}


%build
%{__python} setup.py build


%install
%{__python} setup.py install --skip-build --root %{buildroot}


%files
%doc LICENSE README.rst
%{_bindir}/pecan
%{_bindir}/gunicorn_pecan
%{python_sitelib}/

%changelog
* Fri Apr  5 2013 Luke Macken <lmacken@redhat.com> - 0.2.1-5
- Require python-webob >= 1.2 instead of python-webob1.2

* Thu Mar 14 2013 Padraig Brady <P@draigBrady.com> - 0.2.1-4
- Initial package.

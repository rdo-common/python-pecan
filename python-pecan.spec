# Created by pyp2rpm-1.0.1
%global pypi_name pecan

Name:           python-%{pypi_name}
Version:        0.8.3
Release:        1%{?dist}
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
Requires:       python-singledispatch
Requires:       python-webtest >= 1.3.1
Requires:       python-setuptools
Requires:       python-logutils
%if 0%{?rhel} == 6
Requires:       python-argparse
%endif

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
* Thu Mar 26 2015 Pádraig Brady <pbrady@redhat.com> - 0.8.3-1
- Latest upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 23 2014 Pádraig Brady <pbrady@redhat.com> - 0.4.5-3
- Add missing dependency on python-logutils

* Tue Mar 18 2014 Pádraig Brady <pbrady@redhat.com> - 0.4.5-2
- Add missing dependency on python-singledispatch

* Mon Mar 10 2014 Pádraig Brady <pbrady@redhat.com> - 0.4.5-1
- Latest upstream

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr  5 2013 Luke Macken <lmacken@redhat.com> - 0.2.1-5
- Require python-webob >= 1.2 instead of python-webob1.2

* Thu Mar 14 2013 Padraig Brady <P@draigBrady.com> - 0.2.1-4
- Initial package.

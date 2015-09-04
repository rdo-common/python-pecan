%global pypi_name pecan
%{!?_licensedir:%global license %%doc}
%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{pypi_name}
Version:        1.0.2
Release:        1%{?dist}
Summary:        A lean WSGI object-dispatching web framework

License:        BSD
URL:            http://github.com/pecan/pecan
Source0:        http://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A WSGI object-dispatching web framework, designed to be lean and
fast with few dependencies

%package -n python2-%{pypi_name}
Summary:        A lean WSGI object-dispatching web framework
%{?python_provide:%python_provide python2-%{pypi_name}}
# python_provide does not exist in CBS Cloud buildroot
Provides:       python-%{pypi_name} = %{upstream_version}
Obsoletes:      python-%{pypi_name} < %{upstream_version}

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

Requires:       python-webob
Requires:       python-simplegeneric
Requires:       python-mako
Requires:       python-singledispatch
Requires:       python-webtest
Requires:       python-setuptools
Requires:       python-logutils
Requires:       python-six

%description -n python2-%{pypi_name}
A WSGI object-dispatching web framework, designed to be lean and
fast with few dependencies

# python3 stuff
%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        A lean WSGI object-dispatching web framework
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-webob
Requires:       python3-simplegeneric
Requires:       python3-mako
Requires:       python3-singledispatch
Requires:       python3-webtest
Requires:       python3-setuptools
Requires:       python3-logutils
Requires:       python3-six

%description -n python3-%{pypi_name}
A WSGI object-dispatching web framework, designed to be lean and
fast with few dependencies
%endif

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python2} setup.py build

%if 0%{?with_python3}
%{__python3} setup.py build
%endif

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%if 0%{?with_python3}
%{__python3} setup.py install --skip-build --root %{buildroot}
%endif

%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/pecan
%{_bindir}/gunicorn_pecan
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{_bindir}/pecan
%{_bindir}/gunicorn_pecan
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Fri Sep 04 2015 Chandan Kumar <chkumar246@gmail.com> - 1.0.2-1
- Added python2 and python3 subpackage
- Bumped to 1.0.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

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

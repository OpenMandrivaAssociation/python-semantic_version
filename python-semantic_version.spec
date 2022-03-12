%global pypi_name semantic_version

Name:		python-%{pypi_name}
Version:	2.8.4
Release:	3
Summary:	Library implementing the 'SemVer' scheme
Group:		Development/Python
License:	BSD
URL:		https://github.com/rbarrois/python-semanticversion
Source0:	https://github.com/rbarrois/python-semanticversion/archive/%{version}/python-semanticversion-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
%{?python_provide:%python_provide python-%{pypi_name}}

%description
This small python library provides a few tools to handle semantic versioning
in Python.

%prep
%autosetup -n python-semanticversion-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# documentation builds due to broken symlink
# https://github.com/rbarrois/python-semanticversion/issues/20
rm docs/credits.rst

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.rst ChangeLog
%{python_sitelib}/%{pypi_name}
%{python_sitelib}/%{pypi_name}-*.egg-info

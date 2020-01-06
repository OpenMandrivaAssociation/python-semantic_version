%global pypi_name semantic_version

Name:           python-%{pypi_name}
Version:        2.8.4
Release:        1
Summary:        Library implementing the 'SemVer' scheme
Group:          Development/Python

License:        BSD
URL:            https://github.com/rbarrois/python-semanticversion
Source0:        https://github.com/rbarrois/python-semanticversion/archive/%{version}/python-semanticversion-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-django
%{?python_provide:%python_provide python-%{pypi_name}}

%global _description \
This small python library provides a few tools to handle semantic versioning\
in Python.

%description %{_description}

%package doc
Summary:        Documentation for python-%{pypi_name}
BuildRequires:  python-sphinx

%description doc
%{summary}.

%prep
%autosetup -n python-semanticversion-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# documentation builds due to broken symlink
# https://github.com/rbarrois/python-semanticversion/issues/20
rm docs/credits.rst

%build
%py_build

# generate html docs
sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py_install

%check
# Seems like it's just stuck in koji

#{__python} setup.py test

%files
%license LICENSE
%doc README.rst ChangeLog
%{python_sitelib}/%{pypi_name}/
%{python_sitelib}/%{pypi_name}-*.egg-info/

%files doc
%license LICENSE
%doc html

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-sphinx_ansible_theme
Version  : 0.10.1
Release  : 10
URL      : https://files.pythonhosted.org/packages/b3/58/ed1dc3042cc30511e64560e377cb54c384e82e9f96e17f4c23b82c6c0ef3/sphinx-ansible-theme-0.10.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/b3/58/ed1dc3042cc30511e64560e377cb54c384e82e9f96e17f4c23b82c6c0ef3/sphinx-ansible-theme-0.10.1.tar.gz
Summary  : Ansible Sphinx Theme
Group    : Development/Tools
License  : MIT
Requires: pypi-sphinx_ansible_theme-license = %{version}-%{release}
Requires: pypi-sphinx_ansible_theme-python = %{version}-%{release}
Requires: pypi-sphinx_ansible_theme-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(alabaster)
BuildRequires : pypi(ansible_pygments)
BuildRequires : pypi(babel)
BuildRequires : pypi(certifi)
BuildRequires : pypi(charset_normalizer)
BuildRequires : pypi(docutils)
BuildRequires : pypi(idna)
BuildRequires : pypi(imagesize)
BuildRequires : pypi(importlib_metadata)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(markupsafe)
BuildRequires : pypi(packaging)
BuildRequires : pypi(py)
BuildRequires : pypi(pygments)
BuildRequires : pypi(pyparsing)
BuildRequires : pypi(pytz)
BuildRequires : pypi(requests)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(snowballstemmer)
BuildRequires : pypi(sphinx)
BuildRequires : pypi(sphinx_notfound_page)
BuildRequires : pypi(sphinx_rtd_theme)
BuildRequires : pypi(sphinxcontrib_applehelp)
BuildRequires : pypi(sphinxcontrib_devhelp)
BuildRequires : pypi(sphinxcontrib_htmlhelp)
BuildRequires : pypi(sphinxcontrib_jsmath)
BuildRequires : pypi(sphinxcontrib_qthelp)
BuildRequires : pypi(sphinxcontrib_serializinghtml)
BuildRequires : pypi(urllib3)
BuildRequires : pypi(wheel)
BuildRequires : pypi(zipp)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
sphinx_ansible_theme
--------------------
A reusable Ansible Sphinx Theme.
Demo-site at https://sphinx-ansible-theme.readthedocs.io/en/latest/

%package license
Summary: license components for the pypi-sphinx_ansible_theme package.
Group: Default

%description license
license components for the pypi-sphinx_ansible_theme package.


%package python
Summary: python components for the pypi-sphinx_ansible_theme package.
Group: Default
Requires: pypi-sphinx_ansible_theme-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinx_ansible_theme package.


%package python3
Summary: python3 components for the pypi-sphinx_ansible_theme package.
Group: Default
Requires: python3-core
Provides: pypi(sphinx_ansible_theme)
Requires: pypi(alabaster)
Requires: pypi(ansible_pygments)
Requires: pypi(babel)
Requires: pypi(certifi)
Requires: pypi(charset_normalizer)
Requires: pypi(docutils)
Requires: pypi(idna)
Requires: pypi(imagesize)
Requires: pypi(importlib_metadata)
Requires: pypi(jinja2)
Requires: pypi(markupsafe)
Requires: pypi(packaging)
Requires: pypi(pygments)
Requires: pypi(pyparsing)
Requires: pypi(pytz)
Requires: pypi(requests)
Requires: pypi(snowballstemmer)
Requires: pypi(sphinx)
Requires: pypi(sphinx_notfound_page)
Requires: pypi(sphinx_rtd_theme)
Requires: pypi(sphinxcontrib_applehelp)
Requires: pypi(sphinxcontrib_devhelp)
Requires: pypi(sphinxcontrib_htmlhelp)
Requires: pypi(sphinxcontrib_jsmath)
Requires: pypi(sphinxcontrib_qthelp)
Requires: pypi(sphinxcontrib_serializinghtml)
Requires: pypi(urllib3)
Requires: pypi(zipp)

%description python3
python3 components for the pypi-sphinx_ansible_theme package.


%prep
%setup -q -n sphinx-ansible-theme-0.10.1
cd %{_builddir}/sphinx-ansible-theme-0.10.1
pushd ..
cp -a sphinx-ansible-theme-0.10.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1670498984
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinx_ansible_theme
cp %{_builddir}/sphinx-ansible-theme-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sphinx_ansible_theme/49687825ac9028274cd37f2294743fd3d4eaf1fd || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sphinx_ansible_theme/49687825ac9028274cd37f2294743fd3d4eaf1fd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

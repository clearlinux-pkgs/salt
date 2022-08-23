#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : salt
Version  : 3004.2
Release  : 32
URL      : https://github.com/saltstack/salt/releases/download/v3004.2/salt-3004.2.tar.gz
Source0  : https://github.com/saltstack/salt/releases/download/v3004.2/salt-3004.2.tar.gz
Summary  : Portable, distributed, remote execution and configuration management system
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0
Requires: salt-bin = %{version}-%{release}
Requires: salt-license = %{version}-%{release}
Requires: salt-man = %{version}-%{release}
Requires: salt-python = %{version}-%{release}
Requires: salt-python3 = %{version}-%{release}
Requires: pypi(pycryptodomex)
BuildRequires : buildreq-distutils3
BuildRequires : distro
BuildRequires : pypi(contextvars)
BuildRequires : pypi(distro)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(markupsafe)
BuildRequires : pypi(msgpack)
BuildRequires : pypi(psutil)
BuildRequires : pypi(pycryptodomex)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(pyzmq)
BuildRequires : pypi(requests)
Patch1: 0001-Remove-dep-on-contextvars.patch

%description
Salt is a distributed remote execution system used to execute commands and
query data. It was developed in order to bring the best solutions found in
the world of remote execution together and make them better, faster and more
malleable. Salt accomplishes this via its ability to handle larger loads of
information, and not just dozens, but hundreds or even thousands of individual
servers, handle them quickly and through a simple and manageable interface.

%package bin
Summary: bin components for the salt package.
Group: Binaries
Requires: salt-license = %{version}-%{release}

%description bin
bin components for the salt package.


%package license
Summary: license components for the salt package.
Group: Default

%description license
license components for the salt package.


%package man
Summary: man components for the salt package.
Group: Default

%description man
man components for the salt package.


%package python
Summary: python components for the salt package.
Group: Default
Requires: salt-python3 = %{version}-%{release}

%description python
python components for the salt package.


%package python3
Summary: python3 components for the salt package.
Group: Default
Requires: python3-core
Provides: pypi(salt)
Requires: pypi(distro)
Requires: pypi(jinja2)
Requires: pypi(markupsafe)
Requires: pypi(msgpack)
Requires: pypi(psutil)
Requires: pypi(pycryptodomex)
Requires: pypi(pyyaml)
Requires: pypi(pyzmq)
Requires: pypi(requests)

%description python3
python3 components for the salt package.


%prep
%setup -q -n salt-3004.2
cd %{_builddir}/salt-3004.2
%patch1 -p1
pushd ..
cp -a salt-3004.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656377304
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . pyzmq
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . pyzmq
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/salt
cp %{_builddir}/salt-3004.2/LICENSE %{buildroot}/usr/share/package-licenses/salt/c0f0fb1c856a87d9fc4a59bd2ec0d6b19907a94f
cp %{_builddir}/salt-3004.2/pkg/osx/pkg-resources/license.rtf %{buildroot}/usr/share/package-licenses/salt/906ed1fd66d444e951c0f5f38131d1dd61dfcf7c
cp %{_builddir}/salt-3004.2/pkg/windows/installer/LICENSE.txt %{buildroot}/usr/share/package-licenses/salt/712d25aaeea79cb25612195315109efc884cc5d6
cp %{_builddir}/salt-3004.2/tests/pytests/unit/modules/sol10_pkg/bashs/SUNWbashS/install/copyright %{buildroot}/usr/share/package-licenses/salt/869dfc8f2ae39a287e88ffca20966beab5b08ab8
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} pyzmq
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

%files bin
%defattr(-,root,root,-)
/usr/bin/salt
/usr/bin/salt-api
/usr/bin/salt-call
/usr/bin/salt-cloud
/usr/bin/salt-cp
/usr/bin/salt-key
/usr/bin/salt-master
/usr/bin/salt-minion
/usr/bin/salt-proxy
/usr/bin/salt-run
/usr/bin/salt-ssh
/usr/bin/salt-syndic
/usr/bin/salt-unity
/usr/bin/spm

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/salt/712d25aaeea79cb25612195315109efc884cc5d6
/usr/share/package-licenses/salt/869dfc8f2ae39a287e88ffca20966beab5b08ab8
/usr/share/package-licenses/salt/906ed1fd66d444e951c0f5f38131d1dd61dfcf7c
/usr/share/package-licenses/salt/c0f0fb1c856a87d9fc4a59bd2ec0d6b19907a94f

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/salt-api.1
/usr/share/man/man1/salt-call.1
/usr/share/man/man1/salt-cloud.1
/usr/share/man/man1/salt-cp.1
/usr/share/man/man1/salt-key.1
/usr/share/man/man1/salt-master.1
/usr/share/man/man1/salt-minion.1
/usr/share/man/man1/salt-proxy.1
/usr/share/man/man1/salt-run.1
/usr/share/man/man1/salt-ssh.1
/usr/share/man/man1/salt-syndic.1
/usr/share/man/man1/salt-unity.1
/usr/share/man/man1/salt.1
/usr/share/man/man1/spm.1
/usr/share/man/man7/salt.7

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

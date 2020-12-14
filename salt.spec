#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : salt
Version  : 3002.2
Release  : 8
URL      : https://github.com/saltstack/salt/releases/download/v3002.2/salt-3002.2.tar.gz
Source0  : https://github.com/saltstack/salt/releases/download/v3002.2/salt-3002.2.tar.gz
Summary  : Portable, distributed, remote execution and configuration management system
Group    : Development/Tools
License  : Apache-2.0
Requires: salt-bin = %{version}-%{release}
Requires: salt-license = %{version}-%{release}
Requires: salt-man = %{version}-%{release}
Requires: salt-python = %{version}-%{release}
Requires: salt-python3 = %{version}-%{release}
Requires: Jinja2
Requires: MarkupSafe
Requires: PyYAML
Requires: distro
Requires: msgpack
Requires: pycryptodomex
Requires: pyzmq
Requires: requests
BuildRequires : Jinja2
BuildRequires : MarkupSafe
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : distro
BuildRequires : msgpack
BuildRequires : pycryptodomex
BuildRequires : pyzmq
BuildRequires : requests

%description
==========
        
        Built on python, Salt uses simple and human-readable YAML combined with
        event-driven automation to deploy and configure complex IT systems. In addition
        to powering SaltStack’s powerful enterprise product suite, Salt can be found
        under the hood of products from Juniper, Cisco, Cloudflare, Nutanix, SUSE, and
        Tieto, to name a few.
        
        About SaltStack
        ===============
        
        SaltStack develops award-winning software used by IT and security operations
        teams to help modern business more efficiently secure and maintain all aspects
        of their digital infrastructure. But we’re not like other legacy systems
        management or security software tools. Our software is unique in providing
        intelligent, event-driven automation for efficient control of complex business
        systems at any scale.
        
        We help enterprise IT organizations orchestrate and automate difficult IT tasks
        with speed and flexibility to ultimately deliver continuous security compliance,
        vulnerability remediation, and real IT security.
        
        Whether you need help automating the work of ITOps, DevOps, NetOps, or SecOps
        functions, SaltStack software is the answer. In addition to open source
        software, such as Salt, we offer

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
Requires: pypi(pycryptodomex)
Requires: pypi(pyyaml)
Requires: pypi(pyzmq)
Requires: pypi(requests)

%description python3
python3 components for the salt package.


%prep
%setup -q -n salt-3002.2
cd %{_builddir}/salt-3002.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605742361
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/salt
cp %{_builddir}/salt-3002.2/LICENSE %{buildroot}/usr/share/package-licenses/salt/c0f0fb1c856a87d9fc4a59bd2ec0d6b19907a94f
cp %{_builddir}/salt-3002.2/pkg/osx/pkg-resources/license.rtf %{buildroot}/usr/share/package-licenses/salt/5ac0caf8c8f8209b518d0ac5d21e5d27051d1676
cp %{_builddir}/salt-3002.2/pkg/windows/installer/LICENSE.txt %{buildroot}/usr/share/package-licenses/salt/712d25aaeea79cb25612195315109efc884cc5d6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

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
/usr/share/package-licenses/salt/5ac0caf8c8f8209b518d0ac5d21e5d27051d1676
/usr/share/package-licenses/salt/712d25aaeea79cb25612195315109efc884cc5d6
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

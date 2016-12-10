%{!?upstream_version: %global upstream_version %{version}%{?milestone}}


%global package_name masakari
%global srcname %package_name

%define debug_package %{nil}

Name:       %{package_name}
Version:    2.0.0
Release:    0.test.1%{?dist}
Summary:    Virtual Machine High Availability (VMHA) service for OpenStack.

License:    ASL 2.0
URL:        http://docs.openstack.org/developer/masakari

Source0:    https://tarballs.openstack.org/%{package_name}/%{package_name}-%{upstream_version}.tar.gz

BuildArch:  noarch

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  rdo-rpm-macros

BuildRequires:  python-oslo-sphinx
BuildRequires:  python-sphinx

%description
Masakari provides Virtual Machine High Availability (VMHA) service
for OpenStack clouds by automatically recovering the KVM-based Virtual
Machine(VM)s from failure events such as VM process down, provisioning
process down, and nova-compute host failure.
It also provides API service for manage and control the automated rescue mechanism.

Original version of Masakari: https://github.com/ntt-sic/masakari


%prep
%setup -q -n %{package_name}-%{upstream_version}

export PBR_VERSION=%{version}

# Let's handle dependencies ourseleves
rm -f *requirements.txt


%build
%py2_build


%install
%py2_install
%{__python2} setup.py build_sphinx


%files
%{_bindir}/*
%{python2_sitelib}/%{srcname}*


%changelog
* Mon Dec 12 2016 Vladislav Odintsov <odivlad@gmail.com> - 2.0.0-1
- Initial packaging.

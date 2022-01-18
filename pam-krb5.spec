%define _build_id_links none
%define _pamlibdir %{_libdir}
%define _moduledir %{_libdir}/security
%define _secconfdir %{_sysconfdir}/security
%define _pamconfdir %{_sysconfdir}/pam.d

Name:           pam-krb5
Version:        4.10
Release:        1%{?dist}
Summary:        pam-krb5 is a Kerberos PAM module for either MIT Kerberos or Heimdal. It supports ticket refreshing by screen savers, configurable authorization handling, authentication of non-local accounts for network services, password changing, and password expiration, as well as all the standard expected PAM features. It works correctly with OpenSSH, even with ChallengeResponseAuthentication and PrivilegeSeparation enabled, and supports extensive configuration either by PAM options or in krb5.conf or both. PKINIT is supported with recent versions of both MIT Kerberos and Heimdal and FAST is supported with recent MIT Kerberos.

License:        GPL
URL:            https://github.com/rra/pam-krb5
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  autoconf, m4, krb5-devel, pam-devel
Requires:       krb5-libs, libcom_err, pam

%description
pam-krb5 provides a Kerberos PAM module that supports authentication, user ticket cache handling, simple authorization (via .k5login or checking Kerberos principals against local usernames), and password changing. It can be configured through either options in the PAM configuration itself or through entries in the system krb5.conf file, and it tries to work around PAM implementation flaws in commonly-used PAM-enabled applications such as OpenSSH and xdm. It supports both PKINIT and FAST to the extent that the underlying Kerberos libraries support these features.

This is not the Kerberos PAM module maintained on Sourceforge and used on Red Hat systems. It is an independent implementation that, if it ever shared any common code, diverged long ago. It supports some features that the Sourceforge module does not (particularly around authorization), and does not support some options (particularly ones not directly related to Kerberos) that it does. This module will never support Kerberos v4 or AFS. For an AFS session module that works with this module (or any other Kerberos PAM module), see pam-afs-session.

If there are other options besides AFS and Kerberos v4 support from the Sourceforge PAM module that you're missing in this module, please let me know.

%prep
%autosetup


%build
./bootstrap
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%{_moduledir}/pam_krb5.la
%{_moduledir}/pam_krb5.so
%{_mandir}/man5/*
#%doc /usr/share/doc/%{name}/README.md
%doc README.md
#%license /usr/share/licenses/%{name}/LICENSE
%license LICENSE

%changelog
* Tue Apr 20 2021 Bryan J Smith <b.j.smith@ieee.org>
- Initial RPM from github 4.10 release 2021-03-20

- 

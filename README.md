# SPECfiles

Random RPM SPEC Files (unsorted)


## pam_krb5.spec

Pulls and builds an RPM of [Russ Allbery's pam_krb5.so](https://github.com/rra/pam-krb5), an alternative, MIT Kerberos v5 only compatible, PAM authentication module that, to quote, *"is not the Kerberos PAM module maintained on Sourceforge and used on Red Hat systems. It is an independent implementation that, if it ever shared any common code, diverged long ago."*

### Purpose

This SPEC file is to pull and build *independent* PAM module is to augement the other PAM modules, especially `pam_sss`, on RHEL8+ (and CentOS Stream 8+) systems.  It may build and work on RHEL9 (and CentOS Stream 9) as well, and probably builds on earlier RHEL versions too (but RHEL7 shouldn't need it).

Red Hat deprecated legacy `pam_krb5.so` Kerberos (and legacy `pam_ldap.so` LDAP) support in RHEL7, and removed the support entirely in RHEL8, from the PAM and support Kerberos (and LDAP) packages.  Attempting to rebuild PAM and support packages is not only an extensive exercise, but they are based on legacy code that has not been well maintained.  Red Hat (and Upstream) has focused on the superior, modular System Security Services Daemon (SSSD) that should be used if at all possible.  SSSD maintains REALM (Domain) context and other, advanced security mechanisms, with default IPA (aka IdM) support as well as a modular system that allows support for other Service Providers (not unlike the Windows NT Local Security Authority, LSA, which natively supports ActiveDirectory, AD, but is also modular via added Security Service Providers, SSPs).

The problem is that many legacy mechanisms and architectures don't support REALM (domain) context in authentication, and will choke on it.  Configuring SSSD with multiple providers for multiple systems can cause issues too, as user1 in one context is not the same as user 1 in another context, even if their passwords are the same.  This is ideal and best practice from a security standpoint but, again, legacy mechanisms and architectures don't mesh well, especially where the architecture is Windows-centric, and no proper non-Windows, POSIX (UNIX/Linux) architecture is done for Identity and RBAC.  Hence an option to build such a module, one that has **no dependencies** on PAM or other support packages (other tha MIT Kerberos libraries).

Build, install and modify `/etc/pam.d/[password|system]-auth` as appropriate.

### Example

To preempt SSSD (`pam_sss.so`) -- which always requires a REALM (Domain) context -- so Kerberos authentication can occur using a default/assumed REALM (Domain) or equivalent, with `pam_krb5.so`.  Again, this is a legacy approach which may have security implications in the case people have root on system, VM or Container instances.

```
  ... 
auth        sufficient                       pam_krb5.so minimum_uid=1000 try_first_pass
# ORIGINAL # auth        sufficient          pam_sss.so forward_pass
auth        sufficient                       pam_sss.so use_first_pass
  ... 
```

Consider yourself, and your Enterprise, warned for not architecting your enterprise correctly for non-Windows, POSIX (UNIX/Linux) enterprise with appropriate REALM (Domain) contexts if you have to use something leagacy like this.


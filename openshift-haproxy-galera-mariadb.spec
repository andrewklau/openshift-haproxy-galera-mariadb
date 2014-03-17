%global cartridgedir %{_libexecdir}/openshift/cartridges/galera-mariadb

Summary:       Provides galera mariadb cluster support
Name:          openshift-origin-cartridge-galera-mariadb
Version:       5.5
Release:       1%{?dist}
Group:         Network/Daemons
License:       ASL 2.0
URL:           http://www.openshift.com
Source0:       https://github.com/andrewklau/openshift-galera-mariadb/archive/master.zip
Requires:      MariaDB-Galera-server
Requires:      MariaDB-client

# For RHEL6 install mariadb from official repo to get Galera support
%if 0%{?rhel}
Requires:      MariaDB-Galera-server
Requires:      MariaDB-client
Requires:      MariaDB-compat
Requires:      galera
Requires:      telnet
%endif

Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
BuildArch:     noarch

%description
Provides mariadb galera cluster cartridge support to OpenShift. (Cartridge Format V2)

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}
%__rm %{buildroot}%{cartridgedir}/metadata/manifest.yml.*
 

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Sun Mar 2 2014 Andrew Lau <andrew@andrewklau.com> 5.5
- Added mariadb-galera support

* Mon Jan 27 2014 Andrew Lau <andrew@andrewklau.com> 5.5
- Added mariadb support for RHEL/EL with SCL

* Fri Sep 13 2013 Troy Dawson <tdawson@redhat.com> 1.15.1-1
- Bump up version (tdawson@redhat.com)
- Cartridge version bumps for 2.0.33 (ironcladlou@gmail.com)
- Updated cartridges and scripts for phpmyadmin-4 (mfojtik@redhat.com)
- Cartridge - Sprint 2.0.32 cartridge version bumps (jhonce@redhat.com)
- <cartridges> Additional cart version and test fixes (jolamb@redhat.com)
- Bug 968280 - Ensure Stopping/Starting messages during git push Bug 983014 -
  Unnecessary messages from mongodb cartridge (jhonce@redhat.com)
- Cartridge - Clean up manifests (jhonce@redhat.com)
- Various cleanup (dmcphers@redhat.com)
- Pulled cartridge READMEs into Cartridge Guide (hripps@redhat.com)
- Bug 985514 - Update CartridgeRepository when mcollectived restarted
  (jhonce@redhat.com)
- Bug 976921: Move cart installation to %%posttrans (ironcladlou@gmail.com)
- remove v2 folder from cart install (dmcphers@redhat.com)

* Wed May 08 2013 Krishna Raman <kraman@gmail.com> 0.0.2-1
- new package built with tito



# OpenShift HAProxy for MariaDB Galera 

This is the HAProxy component to my OpenShift MariaDB Galera cartridge [1]

**Status:** Working

**What it does:**

- This cartridge provides a single point of entry to the MariaDB Galera cartridge (I plan on adding some extra haproxy config to better combat split brain and checks, etc.)
- It provides the metadata service for the backend MariaDB galera gears which then gets exposed by a SimpleHTTP python webserver.
- It allows us to select and choose a "master" gear and login details, although our setup is a master/master environment because of the automation involved with cartridges, I've opted to take the path that only the master gear can start up first. This can be changed by logging into the haproxy gear.

**What does not work:**

- The haproxy mysql-check does not currently work properly in my test environment because of the RDNS, and I don't have enough gears to try this in Online. I'm Australian :(

[1] https://github.com/andrewklau/openshift-galera-mariadb

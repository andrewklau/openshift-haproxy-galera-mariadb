# OpenShift HAProxy for MariaDB Galera 

This is the HAProxy component to my OpenShift MariaDB Galera cartridge [1]

**Status:** Working

**What it does:**

- This cartridge provides a single point of entry to the MariaDB Galera cartridge (I plan on adding some extra haproxy config to better combat split brain and checks, etc.)
- It provides the metadata service for the backend MariaDB galera gears which then gets exposed by a SimpleHTTP python webserver.
- It allows us to select and choose a "master" gear and login details, although our setup is a master/master environment because of the automation involved with cartridges, I've opted to take the path that only the master gear can start up first. This can be changed by logging into the haproxy gear.

**What does not work:**

- Nothing so far, please let me know if something breaks..

**Disclaimer:**
- Normal disclaimer, I'm doing this for my own personal learning and gain, with the hopes that this will also help another. 
- Possibly become something which will be used in production environments. 
- However with the nature of database replication software, I'm not responssible for data loss or anything while using this cartridge. 
- Although I've tried very hard to prevent all possible common pitfalls.

[1] https://github.com/andrewklau/openshift-galera-mariadb

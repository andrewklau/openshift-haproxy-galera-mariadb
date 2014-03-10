# OpenShift HAProxy for MariaDB Galera 

The plan is to create this HaProxy to load balance the galera cluster while also providing a single point of access to the gears, prevention of accessing dead gears and also providing a metadata service for the gears (ie. so they can determine the first host).

The metadata service is important to prevent split brains during race conditions...

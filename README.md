# OpenShift HAProxy for MariaDB Galera 

The plan is to create this HaProxy to load balance the galera cluster while also providing a single point of access to the gears, prevention of accessing dead gears and also providing a metadata service for the gears (ie. so they can determine the first host).

The metadata service is important to prevent split brains during race conditions...

Steps:

 - Remove all the web functions from the haproxy (ie. slim down)
 - 
 - galera-cluster needs a ha-proxy user
CREATE USER 'haproxy'@'%';
FLUSH PRIVILEGES;

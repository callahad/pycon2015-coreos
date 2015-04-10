# Consensus

## (etcd)

***

### etcd

Key-value store

Centralized place to store cluster metadata
<!-- .element: class="fragment" -->

***

![](i/servers-trio.svg)

***

### locksmith

Must acquire a lock from etcd before rebooting

Release lock after successful boot
<!-- .element: class="fragment" -->

***

![](i/servers-trio.svg)

# Demo

***

> My etcd server is rebooting on its own, <br> how do I keep my app online?

***

![](i/servers-trio.svg)

***

![](i/servers-doublewide.svg)

***

![](i/servers-5-2.svg)

***

![](i/servers-5-2-outage.svg)

***

![](i/servers-5-24.svg)

***

![](i/servers-tripledouble.svg)

***

### Etcd is Reusable

Google Kubernetes

Pivotal CloudFoundry

Mailgun Vulcand

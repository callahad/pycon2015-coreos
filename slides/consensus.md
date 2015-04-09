# Consensus

## (Etcd)

***

    FIXME: Single CoreOS Node

***

### Problem

> My server is rebooting on its own, <br> how do I keep my app online?

Add another server!
<!-- .element: class="fragment" -->

***

    FIXME: Two CoreOS Nodes

***

### Problem

> Both my servers reboot at the same time, <br> how do I keep my app online?

Add a server to track global state!
<!-- .element: class="fragment" -->

***

    FIXME: Three CoreOS (2+etcd) Nodes

***

### etcd

Key-value store

Centralized place to store cluster metadata
<!-- .element: class="fragment" -->

***

### locksmith

Must acquire a lock from etcd before rebooting
<!-- .element: class="fragment" -->

Release lock after successful boot
<!-- .element: class="fragment" -->

Note: Prevents cascading failures

***

    FIXME: Three CoreOS (2+etcd) Nodes (Again)

***

# Demo

    FIXME: Three CoreOS (2+etcd) Nodes (Again)

***

### Problem

> My etcd server is rebooting on its own, <br> how do I keep my app online?

Distribute the centralized, single point of failure!
<!-- .element: class="fragment" -->

Note: 13 minutes

***

### Etcd is Distributed

***

    FIXME: Etcd Cluster designs

***

### Etcd is Reusable

Google Kubernetes

Pivotal CloudFoundry

Mailgun Vulcand

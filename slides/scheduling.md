# Scheduling

## (Fleet / Kubernetes)

***

### Cluster-level init

> "Always keep two of these running, <br> but not on the same machine."

***

### Schedulers

CoreOS includes Fleet, supports Kubernetes
<!-- .element: class="fragment" -->

Both independent components
<!-- .element: class="fragment" -->

Both built on etcd
<!-- .element: class="fragment" -->

***

### Fleet

Clustered interface for systemd

***

### Systemd Unit Files
```ini
[Unit]
Description=My App
After=docker.service
Requires=docker.service

[Service]
ExecStartPre=-/usr/bin/docker kill my-app-%i
ExecStartPre=-/usr/bin/docker rm my-app-%i
ExecStart=/usr/bin/docker run -rm --name my-app-%i -p 80:8080 callahad/my-app
ExecStop=/usr/bin/docker stop my-app-%i

[X-Fleet]
Conflicts=my-app@*.service
```

***

### X-Fleet attributes

- `Conflicts`
- `MachineOf`
- `MachineID`
- `MachineMetadata`
- `Global`

***

# Demo

***

### Design Considerations

Minimize state

Build "Twelve-Factor Apps"

***

### What about Databases? <br> Load balancers?

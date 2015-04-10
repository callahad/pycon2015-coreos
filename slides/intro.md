# Python on CoreOS

## Dan Callahan -- @callahad

---

<!-- .slide: data-background-size="80%" data-background-image="i/vector_v-dark-trans.svg" -->

***

<!-- .slide: data-background-size="80%" data-background-image="i/vector_v-dark-trans-dim.svg" -->

## This is not a talk about Docker

There is one of those tomorrow

***

## This is a talk about servers

And what containerization changes

***

<!-- .slide: data-background-size="40%" data-background-image="i/coreos-wordmark-vert-color-white.svg" -->

***

<!-- .slide: data-background-size="40%" data-background-image="i/coreos-wordmark-vert-color-transparent.svg" -->

Linux distribution designed for containers

Preview best practices from the future
<!-- .element: class="fragment" -->

---

## What's your ideal platform?

***

1. Stays Updated

2. Won't Break Apps

3. Survives Outages

Note: This is actually *really hard!* Think of the folks on old RHEL.

***

### We need something declarative

> "Always keep two of these running, <br> but not on the same machine."

***

### We need new technology

1. System Updates        <!-- .element: class="fragment" -->
2. Application Isolation <!-- .element: class="fragment" -->
3. Clustering            <!-- .element: class="fragment" -->
4. Task Distribution     <!-- .element: class="fragment" -->

---

### Technology in CoreOS

1. FastPatch (Updates)             <!-- .element: class="fragment" -->
2. Docker / rkt (Containers)       <!-- .element: class="fragment" -->
3. Etcd (Consensus)                <!-- .element: class="fragment" -->
4. Fleet / Kubernetes (Scheduling) <!-- .element: class="fragment" -->

All Free / Open Source Software    <!-- .element: class="fragment" -->

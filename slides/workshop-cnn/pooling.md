---
layout: two-cols
---

# Pooling Layer

so simple a single slide explains it all 🐕

<img alt="pool" src="/images/pool.jpg" />

::right::

<img alt="pool" src="/images/max-avg-pool.png" />

- two kinds of pooling layers:
  - max: get the brightest pixel to represent a group of 4
  - average: get the average _"brightness"_ for the quartet
- a $2 \times 2$ pooling layer quarters your colvolved images
  - 25% input for our `Flatten` and `Dense` layers
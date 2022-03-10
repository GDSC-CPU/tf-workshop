---
layout: two-cols
---

# The [XOR Problem][1] Boundary

<img alt="xorish" src="/images/xorish.png" style="height: 210px" />

Imagine 2 sensors in the oven, and the alarm fires if <twemoji-thermometer />temps
are uneven which will cook only half of your <twemoji-meat-on-bone /><twemoji-birthday-cake />
- both sides cold <twemoji-bell-with-slash />  $y = 0$
- both sides hot <twemoji-bell-with-slash /> $y = 0$
- left cold, right hot <twemoji-bell /> $y = 1$
- left hot, right cold <twemoji-bell /> $y = 1$

::right::

<img alt="xor-boundary" src="/images/xor-boundary.jpg" style="height: 210px" />

- Non-linear boundaries (e.g. curves) need **hidden layers**
- The NN doesn't actually do:  
  $x_1$ XOR $x_2$ = $(x_1$ OR $x_2)$ AND $(x_1$ NAND $x_2)$
- it doesn't even output `0` or `1` strictly, but more like `0.00001`, `0.99999`
- It's formula is actually <twemoji-grinning-face-with-sweat />:
  $$
  xor_{approx}(X) = \sigma(\begin{bmatrix} 1 && \sigma(Xw_{or}) & \sigma(Xw_{nand}) \end{bmatrix}w_{and})
  $$

  [1]: https://towardsdatascience.com/how-neural-networks-solve-the-xor-problem-59763136bdd7

  <style>
  .katex {
    font-size: 1em !important;
  }
  </style>
---
layout: two-cols
---

# Sigmoid function

<div></div>

💡 $z = Xw$: there are other activation functions that can transform $z$, 
so a _"temporary variaable"_ is helpful.

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

<img alt="sigmoid" src="/images/sigmoid.png" />

::right::

| $z$   | $\sigma(z)$              |
|-------|--------------------------|
| -10   | 4.5397 × 10<sup>-5</sup> |
| -8    | 0.0003353501             |
| -4    | 0.0179862010             |
| -0.5  | 0.3775406688             |
| 0     | 0.5                      |
| 0.5   | 0.6224593312             |
| 1     | 0.7310585786             |
| 5     | 0.9933071491             |
| 9     | 0.9998766054             |

- Interpret $\sigma(z)$ as probability of $y$ being a $1$.

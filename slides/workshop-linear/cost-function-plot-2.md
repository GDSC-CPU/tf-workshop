---
layout: two-cols
---

# Graph of the loss function

Paraboloid? let's remove $\theta_0$ for a simpler 2D parabola

<img alt="graph of costs" src="/images/graph-cost.jpg" style="width: 400px; height: 289px" />

- What do you see?  
  * The lowest cost is when $w_1$ is around **1.5**
  * $w_1 = 1.5, w_0 = 1.3$ seems to be a good guess

::right::

| $w_1$    | $w_0$   | MSE: $\hat{y} = (Xw - y)^T(Xw - y)$ |
|----------|---------|-------------------------------------|
| 0.5      | 0.5     | 18.864                              |
| 0.7      | 0.92    |  7.079                              |
| 0.98     | 1.2     |  2.542                              |
| 1.5      | 1.3     |  1.397                              |

<img alt="lines guess" src="/images/idea.jpg" style="width: 370px; height: 250px" />

---
layout: two-cols
---

<style>
  .neuron {
    width: 400px;
    height: 200px;
  }
</style>

# Vectorization

- addition and multiplication are commutative
  * safe to do in parallel
- so is every entry of the summation
  * we can split the load among several cores, _perhaps_:
    + Core 1: $\sum\limits_{i = 0}^{10} (y_i - \hat{y}_i)^2$
    + Core 2: $\sum\limits_{i = 11}^{20} (y_i - \hat{y}_i)^2$

<img class="neuron" alt="neuron" src="/images/single-neuron.png" />

:: right::

- also notice that:  
  $\sum\limits_{i = 0}^{3} w_ix_i = w_0x_0 + w_1x_1 + w_2x_2 + w_3x_3$
  
  $$
    X = \begin{bmatrix}
          x_0^{(1)} & x_1^{(1)} & x_2^{(1)} & x_3^{(1)} \\
          x_0^{(2)} & x_1^{(2)} & x_2^{(2)} & x_3^{(2)} \\
          x_0^{(3)} & x_1^{(3)} & x_2^{(3)} & x_3^{(3)} \\
          \vdots  & \vdots  & \vdots  & \vdots  \\
          x_0^{(m)} & x_1^{(m)} & x_2^{(m)} & x_3^{(m)} \\
        \end{bmatrix} 
      
    w = \begin{bmatrix}
          w_0 \\
          w_1 \\
          w_2 \\
          w_3
        \end{bmatrix}
  $$

  $$
    \hat{y} = Xw
  $$

- and finally $\frac{1}{2m} \sum\limits_{i = 1}^{m}(y_i - \hat{y_i})^2$
  + is vectorized as: $\frac{1}{2m}(\hat{y} - y)^T(\hat{y} - y)$
  + also equivalent to: $\frac{1}{2m}(Xw - y)^T(Xw - y)$

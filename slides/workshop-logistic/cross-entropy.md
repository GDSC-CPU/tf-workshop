---
layout: two-cols
---

# Binary Cross Entropy Loss

👇 This is the only part you need to understand

- For a single training sample:

$\hat{y} = \sigma(Xw) = \frac{1}{1 + e^{-Xw}}$

$Cost(\hat{y}, y) = -y \log(\hat{y}) - (1 - y)\log(1 - \hat{y})$

| y (0 or 1 only)   | $\hat{y}$ (0 to 1 range)  | Cost       |
|-------------------|---------------------------|------------|
| 1                 | 0.99999                   | almost 0   |
| 1                 | 0.7                       | 0.35667    |
| 1                 | 0.1                       | 2.30259    |
| 1                 | 0.000001                  | 13.81551   |
| 0                 | 0.000001                  | almost 0   |
| 0                 | 0.3                       | 0.35667    |
| 0                 | 0.9                       | 2.30259    |
| 0                 | 0.999999                  | 13.81551   |

::right::

### 👇👇 ***No need to absorb for workshop*** 😹

<kbd>Just here for completeness</kbd>

<div class="mt-4"></div>

- For the entire training set, as usual - average of costs

***Unvectorized***

$$
  J(w) = -\frac{1}{m} \sum\limits_{i = 1}^{m} y^{(i)} \log(\hat{y}^{(i)}) - (1 - y^{(i)})\log(1 - \hat{y}^{(i)})
$$

<div class="mt-2"></div>

***Vectorized***

$h = \sigma(Xw)$

$J(w) = -\frac{1}{m} \cdot (y^T\log(h) + (1 - y)^T\log(1 - h))$

***Partial Derivative of vectorized $J(w)$***: &nbsp;[<small>Derivation if interested</small>][1]

$\frac{\partial}{\partial{w}}J(w) = \frac{1}{m}X^T[\sigma(Xw) - y]$

[1]: https://medium.com/analytics-vidhya/derivative-of-log-loss-function-for-logistic-regression-9b832f025c2d

<style>
  td {
    padding: 4px !important;
  }

  th {
    padding: 8px !important;
  }

  small {
    color: green;
  }

  h3 {
    margin-bottom: 0px;
  }
</style>
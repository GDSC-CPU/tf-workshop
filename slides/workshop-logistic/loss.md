---
layout: two-cols
---

# Loss <mdi-function />: MSE still 👌?

<div></div>

$J(w) = \frac{1}{2m} \sum\limits_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})^2$

$J(w) = \frac{1}{2m} \sum\limits_{i=1}^{m} (\frac{1}{1 + e^{-Xw}} - y^{(i)})^2$

- <twemoji-person-gesturing-no /> Nope 01: The more obvious reason:
  - [It doesn't _**strongly penalize**_ misclassifications][2]
  - even for a perfect mismatch

| $y$    | $\hat{y}$   | $y - \hat{y}$   |  $(y - \hat{y})^2$  |
|--------|-------------|-----------------|---------------------| 
| 1      | 0           | 1               | 1                   |
| 1      | 0.2         | 0.8             | 0.64                |
| 1      | 0.9         | 0.1             | 0.01                |

::right::

- <twemoji-person-gesturing-no /> Nope 02: The less-obvious reason:

👈 that's a **non-convex function**, <small class="text-blue-500 italic">just research the reason why✌✌</small>

> If we try to use the cost function of the linear regression in ‘Logistic Regression’ then it would be of no use as it would end up being a [**non-convex function with many local minimums**, in which it would be ***very difficult to minimize the cost value and find the global minimum.***][1]

<img alt="convex" src="/images/non-convex.png" />

> [Cross entropy cost function with logistic function gives a **convex curve with *one local / global minima***.][3]

[1]: https://towardsdatascience.com/introduction-to-logistic-regression-66248243c148
[2]: https://towardsdatascience.com/why-not-mse-as-a-loss-function-for-logistic-regression-589816b5e03c
[3]: https://dchandra.com/machine%20learning/statistics/2019/01/07/Logistic-regression-from-scratch.html

<style>
  blockquote {
    font-size: 1em !important;
    margin-top: 12px;
    margin-bottom: 12px;
  }
</style>
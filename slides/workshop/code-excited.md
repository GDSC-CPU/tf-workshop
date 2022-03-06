---
layout: two-cols
---

# Unvectorized 🐢

<div></div>

$Cost(w_1, w_0) = \frac{1}{2m} \sum\limits_{i = 1}^{m}(y_i - \hat{y_i})^2$

```py
def cost(x1, y, w1, w0)
  total = 0
  m = len(x1)

  for i in range(m):
      y_hat_i = w1 * x1[i] + w0
      total += (y_hat_i - y[i]) ** 2

  return total * 0.5 * m
```

- sequential operations
- **will not scale**
  * $w_1x_1 + w_2x_2 + w_3x_3 + ... + w_{10000}x_{10000}$
    - **PER NEURON**
  * lots of neurons per layer

::right::

# Vectorized 🐇

<div class="mt-6"></div>

$Cost(w) = \frac{1}{2m}(Xw - y)^T(Xw - y)$

<div class="mt-8"></div>

```py
def cost(X, y, w):
    m = X.shape[0]
    return 0.5 * m * (X @ w - y).T @ (X @ w - y)
```

- parallel operations
- `X` is a matrix, `y` and `w` are vectors

```py
# working with matrices is normal in ML
some_4x3_matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, 0, 0]
])
```

***lots of training data understandable, but seriously, can we reach 10k inputs?***
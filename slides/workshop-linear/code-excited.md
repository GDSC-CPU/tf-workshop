---
layout: two-cols
---

# Unvectorized 🐢

<div></div>

$Cost(w_1, w_0) = \frac{1}{2m} \sum\limits_{i = 1}^{m}(y_i - \hat{y_i})^2$

where $\hat{y} = w_1x_{1i} + w_0$

```py
def cost(x1, y, w1, w0)
    total = 0
    m = len(x1)

    for i in range(m):
        y_hat_i = w1 * x1[i] + w0
        total += (y_hat_i - y[i]) ** 2

    return total * 0.5 * m
```

- sequential operations / single-threaded
- **will not scale**
- [writing your own custom loss functions in <logos-tensorflow /> requires vectorization][1]: 
  \~\~ ***have a "vectorized mentality"*** <twemoji-beaming-face-with-smiling-eyes />

[1]: https://towardsdatascience.com/creating-custom-loss-functions-using-tensorflow-2-96c123d5ce6c

::right::

# Vectorized 🐇

<div class="mt-6"></div>

$Cost(w) = \frac{1}{2m}(Xw - y)^T(Xw - y)$

```py
def cost(X, y, w):
    m = X.shape[0]
    return 0.5 * m * (X @ w - y).T @ (X @ w - y)
```

- parallel operations
- `X` is a matrix, `y` and `w` are vectors
- **BONUS**: more succinct code
  + almost looks like the equation
- BTW: in Python
  - `@` - **THE** matrix multiplication (*usually <mdi-check class="text-green-500" />*)
  - `*` - element-wise multiplication (*usually <mdi-close class="text-red-500" />*)
  
$$
\begin{bmatrix}a & b \\ c & d \end{bmatrix} * 
\begin{bmatrix}w & x \\ y & z \end{bmatrix} =
\begin{bmatrix}aw & bx \\ cy & dz \end{bmatrix}
$$
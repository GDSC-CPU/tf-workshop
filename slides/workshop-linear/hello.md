---
layout: two-cols
---

# Hello <logos-numpy /> NumPy

_"Numerical Python"_

* mathematical functions
* random number generators
* **inear algebra** routines
* $n$-dimensional arrays
  - generic enough to represent matrices and vectors

<div class="mt-2"></div>

#### _4x2 matrix_

$$
A = \begin{bmatrix}
  1 && 2 && 3 && 4 \\
  5 && 6 && 7 && 8 \\
\end{bmatrix}
$$

```py
A = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])
```

::right::

#### _4-element vector (a.k.a. 4x1 matrix)_

$$
v = \begin{bmatrix}
1 \\
2 \\
3 \\
4 \\
\end{bmatrix}
$$

```py
v = np.array([
    [1],
    [2],
    [3],
    [4]
]) # written to look like a vector for readability

# hate all the []? transpose from a 1x4 matrix
v = np.array([[
    1, 
    2, 
    3, 
    4
]]).T
# note we just wrote each number on a separate line
# for readability of our code. [1, 2, 3, 4] IS A ROW
```

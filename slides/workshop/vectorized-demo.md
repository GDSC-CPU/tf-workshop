---
layout: image-right
image: https://i.imgflip.com/67dvmw.jpg
---

# Vectorization

#### If the last slide is 😵💫🥴, they're the same!

- Sum of squares, unvectorized

$$
\sum\limits_{i = 1}^{4} i^2 = 1^2 + 2^2 + 3^2 + 4^2 = 30
$$

- Sum of squares of all elements in vector $v$

$$
= v^Tv
$$

$$
\begin{bmatrix}
1 & 2 & 3 & 4
\end{bmatrix}

\cdot

\begin{bmatrix}
1 \\
2 \\
3 \\
4
\end{bmatrix}
$$

$$
= 1 \cdot 1 + 2 \cdot 2 + 3 \cdot 3 + 4 \cdot4 = 30
$$
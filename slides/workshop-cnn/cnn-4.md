---
layout: two-cols
---

# GIF showing the process

<img alt="gif" src="/images/cnn.gif" />

The filter matrix used here is:
$
\begin{bmatrix}
  1 & 0 & 1 \\
  0 & 1 & 0 \\
  1 & 0 & 1
\end{bmatrix}
$

::right::

- get the middle pixel, and get **its** new value by
  getting a summation of the pixel values of **that pixel** as center
  - along w/ its 8 neighboars, multiplied element-wise $\odot$ 
  - with each element in the filter matrix as _"multiplier"_
  <img alt="shoe" src="/images/shoe.png" />
- we don't have eight neighbors around the edges 
  - (e.g. `image[0][0]` only has 3 neighbors 
    <twemoji-right-arrow /><twemoji-down-right-arrow /><twemoji-down-arrow />)
- in effect, the convolved image loses its _"1 pixel margin"_
  - ❓❓ how much margin is lost for $5\times5$ filters?
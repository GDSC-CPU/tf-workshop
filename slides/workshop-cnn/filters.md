---
layout: two-cols
---

# Convolutional Layer Filters

- <img alt="flower" src="/images/filterblur.jpg" />
- $\begin{bmatrix}
0 & 0.2 & 0 \\
0.2 & 0.2 & 0.2 \\
0 & 0.2 & 0
\end{bmatrix}$<br><br>
Soft blur

<div></div>

- <img alt="flower" src="/images/filternotsharpen.jpg" />
- $\begin{bmatrix}
1 & 1 & 1 \\
1 & -7 & 1 \\
1 & 1 & 1
\end{bmatrix}$<br><br>
Excessive sharpen

::right::

# ...are like Photoshop Filters

- <img alt="flower" src="/images/filteremboss.jpg" />
- $\begin{bmatrix}
-1 & -1 & 0 \\
-1 & 0 & 1 \\
0 & 1 & 1
\end{bmatrix}$<br><br>
Emboss

<div></div>

- <img alt="flower" src="/images/filteredge.jpg" />
- $\begin{bmatrix}
-1 & -1 & -1 \\
-1 & 8 & -1 \\
-1 & -1 & -1
\end{bmatrix}$<br><br>
Detect Edges

<style>
  img {
    margin-left: auto;
    margin-right: auto;
    height: 210px;
    display: inline;
  }

  ul {
    display: flex;
  }

  ul li {
    list-style: none;
  }
</style>
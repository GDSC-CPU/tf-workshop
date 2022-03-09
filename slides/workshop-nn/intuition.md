# Intuition and Examples for Universal Approx. Theorem

- Boolean Logic is not $y = mx + b$ right?

| $x_1$  | $x_2$  | $x_1$ AND $x_2$  | $z = w_0 + w_1x_1 + w_2x_2$  | $\sigma(z)$ | $x_1$ OR  $x_2$  | $z = w_0 + w_1x_1 + w_2x_2$  | $\sigma(z)$ |
|--------|--------|------------------|------------------------------|-------------|------------------|------------------------------|-------------|
| 0      | 0      | 0                | $-30 + 0 + 0 = -30$          | $\approx 0$ | 0                | $-10 + 0 + 0 = -10$          | $\approx 0$ |
| 0      | 1      | 0                | $-30 + 0 + 20 = -10$         | $\approx 0$ | 1                | $-10 + 0 + 20 = 10$          | $\approx 1$ |
| 1      | 0      | 0                | $-30 + 20 + 0 = -10$         | $\approx 0$ | 1                | $-10 + 20 + 0 = 10$          | $\approx 1$ |
| 1      | 1      | 1                | $-30 + 20 + 20 = 10$         | $\approx 1$ | 1                | $-10 + 20 + 20 = 30$         | $\approx 1$ |


- **weights for AND**<br /><br />
  $w = \begin{bmatrix}-30 \\ 20 \\ 20 \end{bmatrix}$

- <img alt="logic gates" src="/images/logic-gates.png" style="width: 200px; height: 200px;" />

- **weights for OR**<br /><br />
  $w = \begin{bmatrix}-10 \\ 20 \\ 20 \end{bmatrix}$

::right::

# Universal Approx. Theorem

<style>
  td {
    padding: 4px !important;
  }

  table {
    margin-bottom: 8px;
  }

  ul {
    display: flex;
  }

  ul li {
    list-style: none;
    flex: 1;
  }

  td:nth-child(6), th:nth-child(6), td:nth-child(3), th:nth-child(3) {
    border-left: 2px solid darkgray;
  }
</style>
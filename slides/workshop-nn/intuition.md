# Intuition and Examples for Universal Approx. Theorem

- Boolean Logic is not $y = mx + b$ right?  &nbsp; Single neuron can approximate AND, NAND, and OR **functions**.

| $x_1$  | $x_2$  | $z = w_0 + w_1x_1 + w_2x_2$  | $x_1$ AND $x_2$ <br /> $\sigma(z)$ | $z = w_0 + w_1x_1 + w_2x_2$  | $x_1$ NAND $x_2$ <br /> $\sigma(z)$ | $z = w_0 + w_1x_1 + w_2x_2$  | $x_1$ OR $x_2$ <br /> $\sigma(z)$  |
|--------|--------|------------------------------|------------------------------------|------------------------------|-------------------------------------|------------------------------|------------------------------------|
| 0      | 0      | $-30 + 0 + 0 = -30$          | $\approx 0$                        | $30 + 0 + 0 = 30$            | $\approx 1$                         | $-10 + 0 + 0 = -10$          | $\approx 0$                        |
| 0      | 1      | $-30 + 0 + 20 = -10$         | $\approx 0$                        | $30 + 0 + -20 = 10$          | $\approx 1$                         | $-10 + 0 + 20 = 10$          | $\approx 1$                        |
| 1      | 0      | $-30 + 20 + 0 = -10$         | $\approx 0$                        | $30 + -20 + 0 = 10$          | $\approx 1$                         | $-10 + 0 + 20 = 10$          | $\approx 1$                        |
| 1      | 1      | $-30 + 20 + 20 = 10$         | $\approx 1$                        | $30 + -20 + -20 = -10$       | $\approx 0$                         | $-10 + 0 + 20 = 10$          | $\approx 1$                        |

- <img alt="logic gates" src="/images/logic-gates.png" style="width: 200px; height: 200px;" />
- 
- **weights for AND**<br /><br />
  $w = \begin{bmatrix}-30 \\ 20 \\ 20 \end{bmatrix}$

- **weights for NAND**<br /><br />
  $w = \begin{bmatrix} 30 \\ -20 \\ -20 \end{bmatrix}$

- **weights for OR**<br /><br />
  $w = \begin{bmatrix}-10 \\ 20 \\ 20 \end{bmatrix}$

<h5 v-click class="absolute bottom-8 right-8 text-orange-500" style="width: 550px;">
  ❓ <span class="text-yellow-500 underline">For Php50 load:</span>
  How can we construct the XOR <i><b>function</b></i> using only those 3 other <b><i>functions</i></b> above
  <code>(AND, OR, and NAND)</code>?
</h5>

<style>
  td {
    padding: 4px !important;
    font-size: 0.75em;
  }

  th {
    font-size: 0.75em;
  }

  table {
    margin-bottom: 8px;
  }

  ul {
    display: flex;
  }

  ul li:first-child {
    width: 200px;
    flex: 4;
  }

  ul li {
    list-style: none;
    flex: 3;
  }

  td:nth-child(7), th:nth-child(7), td:nth-child(5), th:nth-child(5), td:nth-child(3), th:nth-child(3) {
    border-left: 2px solid darkgray;
  }

  th:nth-child(4), th:nth-child(6), th:nth-child(8) {
    color: teal;
  }

  td:nth-child(4), td:nth-child(6), td:nth-child(8) {
    color: teal;
  }
</style>
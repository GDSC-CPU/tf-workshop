# Intuition and Examples for Universal Approx. Theorem

| $x_1$  | $x_2$  | $x_1$ NAND $x_2$ <br /> $\sigma(z)$ | $x_1$ OR $x_2$ <br /> $\sigma(z)$  | $z = w_0 + w_1x_1 + w_2x_2$  | $x_1$ AND $x_2$ <br /> $\sigma(z)$ |
|--------|--------|-------------------------------------|------------------------------------|------------------------------|------------------------------------|
| 0      | 0      | $\approx 1$                         | $\approx 0$                        | $-30 + 20 + 0 = -30$         | $\approx 0$                        |
| 0      | 1      | $\approx 1$                         | $\approx 1$                        | $-30 + 20 + 20 = 10$         | $\approx 1$                        |
| 1      | 0      | $\approx 1$                         | $\approx 1$                        | $-30 + 20 + 20 = 10$         | $\approx 1$                        |
| 1      | 1      | $\approx 0$                         | $\approx 1$                        | $-30 + 0 + 20 = -10$         | $\approx 0$                        |

- <img alt="logic gates" src="/images/xor.png" style="width: 200px; height: 200px;" />
- <br>💸 💸 💸 💰 💰 💰 📱 📱 📱<br>
  $x_1$ XOR $x_2$ = $(x_1$ OR $x_2)$ AND $(x_1$ NAND $x_2)$
  
  <p class="layer pt-4 font-bold">XOR only achievable by using a hidden layer!!</p>

<style>
  td {
    padding: 8px !important;
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

  li .layer {
    font-size: 1em;
  }

  ul li:first-child {
    width: 200px;
    flex: 1;
  }

  ul li:last-child {
    flex: 1;
    font-size: 1.5em;
    flex: 2.5;
  }

  ul li {
    list-style: none;
    flex: 2;
  }

  td:nth-child(3), th:nth-child(3), td:nth-child(4), th:nth-child(4), td:nth-child(5), th:nth-child(5) {
    border-left: 2px solid darkgray;
  }

  th:nth-child(3), td:nth-child(3) {
    color: red;
  }

  th:nth-child(4), td:nth-child(4) {
    color: blue;
  }

  th:nth-child(6), td:nth-child(6), th:nth-child(5), td:nth-child(5) {
    color: green;
  }
</style>
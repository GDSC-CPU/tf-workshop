---
layout: two-cols
---

# <twemoji-man-technologist /><twemoji-woman-technologist /> You do it

<table>
  <thead>
    <tr>
      <th>Size in m<sup>2</sup></th>
      <th>Price in ₱ ×10k</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0.2</td>
      <td>0.2</td>
    </tr>
    <tr>
      <td>1</td>
      <td>1.8</td>
    </tr>
    <tr>
      <td>2</td>
      <td>4</td>
    </tr>
    <tr>
      <td>3</td>
      <td>7</td>
    </tr>
    <tr>
      <td>5</td>
      <td>11</td>
    </tr>
    <tr>
      <td>7</td>
      <td>12</td>
    </tr>
    <tr>
      <td>10</td>
      <td>13</td>
    </tr>
    <tr>
      <td>9</td>
      <td>14</td>
    </tr>
  </tbody>
</table>

::right::

<Countdown class="text-orange-500" />

* replace the $y = 2x + 1$ training set with the _"house prices"_ you see on the left
  - <small>more like _"bahay-kubo"_ prices with 10 m<sup>2</sup> as the largest</small>
* predict the prices of house sizes it's never seen before:
  - try **8** $m^2$ and **12** $m^2$ for example
* **[Optional]**: Graph the line that best fits all data points.
  - <small>💡 Examine `model.weights` to get $w_1$ and $w_0$.</small>
* **[Optional]**: Graph the costs, and see the curve flatten. 
  - <small>💡 `history = model.fit(...)` and graph `history.epoch` against
    `history.history['loss']`</small>

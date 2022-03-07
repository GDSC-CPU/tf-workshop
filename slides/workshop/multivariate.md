# Multivariate is ***almost*** the same

- if you'll predict house price based on 3 **features**: the area ($x_1$), 
  number of bedrooms ($x_2$), and age of the house ($x_3$)...
  * it's still the same formula: $\hat{y} = Xw$, but for 5 training samples,
    now our $X$ and $w$ might look like

  $$
  \hat{y} =

  \begin{bmatrix}
  x_0^{(1)} & x_2^{(1)} & x_2^{(1)} & x_3^{(1)} \\
  x_0^{(2)} & x_2^{(2)} & x_2^{(2)} & x_3^{(2)} \\
  x_0^{(3)} & x_2^{(3)} & x_2^{(3)} & x_3^{(3)} \\
  x_0^{(4)} & x_2^{(4)} & x_2^{(4)} & x_3^{(4)} \\
  x_0^{(5)} & x_2^{(5)} & x_2^{(5)} & x_3^{(5)}
  \end{bmatrix}

  \cdot

  \begin{bmatrix}
    w_0 \\
    w_1 \\
    w_2 \\
    w_3
  \end{bmatrix}
  $$

- but this introduces a _"problem"_ that the values are in different ranges
  + house size could range between 22 to 300 sq.m.
  + number of bedrooms could be 1 to 5
  + age could be 1 to 115 👻🏠
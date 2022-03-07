---
layout: center
---

# Mean-square error (MSE)

```py
loss=keras.losses.MeanSquaredError()
```

- Squaring values also make them positive, and **penalizes bigger errors.**  
  $MSE = \frac{1}{m} \sum\limits_{i = 1}^{m}(y_i - \hat{y_i})^2$ &nbsp; &nbsp; &nbsp; &nbsp; 
  where $\hat{y}_i = w_1x_{1i} + w_0$
- Some mathematicians also _"halve"_ this mean, which is still proportional, for a very cool reason 😉
  $\frac{1}{2m} \sum\limits_{i = 1}^{m}(y_i - \hat{y_i})^2$

|  $y$  | $\hat{y}$  | $\| y - \hat{y}\|$  | $(y - \hat{y})^2$ |
|-------|------------|---------------------|-------------------|
|  4    | 4          | 0                   | 0                 |
|  4    | 3          | 1                   | 1                 |
|  4    | -3         | 1                   | 1                 |
|  4    | 7          | 3                   | 9                 |
|  4    | -8         | 4                   | 16                |
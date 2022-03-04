# That seems easy to code, let's code <twemoji-man-technologist /><twemoji-woman-technologist />

```py
total = 0
for i in range(m):
    y_hat = w1 * x1[i] + w0
    total += (yhat - y[i]) ** 2

mse = total / m
```

Not so fast...<twemoji-man-running /><twemoji-woman-running />

- doing this for 10,000 inputs with 60,000 training data using a loop **will not scale**
  * we'll have more inputs ($w_1x_1 + w_2x_2 + w_3x_3 + ... + w_{10000}x_{10000}$)
  * we'll have more neurons with their own weights
    + that's another batch of $w_1x_1 + w_2x_2 + w_3x_3 + ... + w_{10000}x_{10000}$
  * that loop will execute 60k times, and each loop will perform 10k multiplications and additions

## lots of data understandable, but seriously, 10,000 inputs?

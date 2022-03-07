---
layout: two-cols
---

# Feature Normalization

<div></div>

**Normalization** is a scaling technique in which values are shifted and rescaled so that they end up ranging between 0 and 1. It is also known as **Min-Max scaling.**

$$
X_{norm} = \frac{X - X_{min}}{X_{max} - X_{min}}
$$

- the lowest value will produce $X_{min} - X_{min}$ in the numerator, and will
  become $0$.
- the highest value will produce $\frac{X_{max} - X_{min}}{X_{max} - X_{min}}$
  and will be scaled to $1$.

```py
# say our X matrix is:
X = np.array([
    [1000, 5, 70],
    [2000, 6, 90],
    [2500, 2, 95],
])
```

::right::

Using Scikit-learn:

```py
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(X) # get min and max, store internally
scaler.transform(X) # scale
```

Using NumPy only and vectorization powers 💪💪:

```py
# get min & max column-wise (axis=0 means X-axis)
X_min = np.min(X, axis=0) # array([1000, 2, 70])
X_max = np.max(X, axis=0) # array([2500, 6, 95])
X_norm = (X - X_min) / (X_max - X_min)
```

They'll produce the same matrix!

```py
array([[0.   , 0.75 , 0.   ],
       [0.667, 1.   , 0.8  ],
       [1.   , 0.   , 1.   ]])
```

---
layout: two-cols
---

# <logos-tensorflow /> / Keras Converts SCCE 

```py
y_true = np.array([
    [1],
    [2]
])

y_pred = np.array([
    [0.04, 0.95, 0.01],
    [0.1, 0.8, 0.1],
])

scce = keras.losses.SparseCategoricalCrossentropy(
    reduction=tf.keras.losses.Reduction.NONE
)
scce(y_true, y_pred).numpy()
# array([0.05129329, 2.30258512])
```

$J = -\sum\limits_{i = 1}^{n}y_i\log(p_i)$, &nbsp; &nbsp; or vectorized 
$J = y^T\log(p)$

where $n$ is the number of classes,  
and $p_i$ is the softmax probability for the $i^{th}$ class

::right::

# ...into CCE

```py
y_true_onehot = np.array([
    [0, 1, 0],
    [0, 0, 1]
])

cce = keras.losses.CategoricalCrossentropy(
    reduction=tf.keras.losses.Reduction.NONE
)
cce(y_true_onehot, y_pred).numpy()
# array([0.05129329, 2.30258512])
```

|               | correct prediction       | wrong prediction       |
|---------------|--------------------------|------------------------|
| $y_{true}$    | $[ 0, 1, 0]$ _index 1_   | $[ 0, 0, 1]$ _index 2_ |
| $y_{pred}$    | $[0.04, 0.95, 0.01]$     | $[0.1, 0.8, 0.1]$      |
| $p$           | $[0.22, 0.56, 0.22]$     | $[0.25, 0.50, 0.25]$   |
| $-\log(p)$    | $[3.22, 0.05, 4.61]$     | $[2.30, 0.22, 2.30]$   |
| $-y^T\log(p)$ | $0.05$ _(small penalty)_ | $2.3$ _(big penalty)_  |

<style>
  td {
    padding: 5px !important;
  }

  td i, td em {
    color: darkorange;
    padding-left: 16px;
  }
</style>
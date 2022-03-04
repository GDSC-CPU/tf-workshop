---
layout: two-cols
---

# The Single Neuron, again

- Let's code this in <logos-tensorflow />

<img alt="single neuron" src="/images/single-neuron.png" style="width: 350px; height: 175px" />

```py
house_prices = np.array([
  [0.2, 0.2],
  [1, 1.8],
  [2, 4],
  [3, 7],
  [4, 9],
  [5, 11],
  [7, 12],
  [10, 13],
  [9, 14]
])
```

::right::

```py
import tensorflow as tf
import numpy as np
from tensorflow import keras

x = house_prices[:, [0]]
y = house_prices[:, [1]]

model = keras.Sequential([
  keras.layers.Dense(units=1, input_shape=[1])
])

sgd = tf.keras.optimizers.SGD(learning_rate=0.005)
mse = tf.keras.losses.MeanSquaredError()

model.compile(
  loss=mse, 
  optimizer=sgd
)

model.fit(x, y, epochs=500)

model.predict(np.array([
  [8],
  [12]
]))
```
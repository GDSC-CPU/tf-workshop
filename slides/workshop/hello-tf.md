---
layout: two-cols
---

# Hello <logos-tensorflow /> Tensorflow


```py
import tensorflow as tf
import numpy as np
from tensorflow import keras

training_data = np.array([
    [ 1,  3],
    [ 2,  5],
    [ 3,  7],
    [ 4,  9],
    [ 5, 11],
    [ 7, 15],
    [ 8, 17],
    [ 9, 19],
    [11, 23]
])
```

- If you observe carefully:
  * the relationship between columns 1 and 2 is $2x + 1$
- Can a machine possibly figure out this relationship?
  * nowhere in our code is this relationship mentioned

::right::

```py
# separate matrix into input (x) and output (y)
x = training_data[:, [0]]
y = training_data[:, [1]]

# just one unit, an output neuron and one input
model = keras.Sequential([
    keras.layers.Dense(units=1, input_shape=[1])
])
model.compile(
    loss=keras.losses.MeanSquaredError(),
    optimizer=keras.optimizers.SGD(learning_rate=.02)
)

# train our model
model.fit(x, y, epochs=500)

# test with values it's never seen before
model.predict(np.array([
    [13],
    [-5]
]))

# produces the following.  that's pretty close!!
# array([[27.00273 ],
#        [-9.005974]], dtype=float32)
```

<style>
  .slidev-code {
    overflow: hidden;
  }
</style>
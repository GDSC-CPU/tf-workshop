---
layout: two-cols
---

# Building a Binary Classifier

It's not much different from linear regression.  We just change a couple of things:

1. we now **add** an activation function to our **NEURON** 
   - _actually the entire layer_
   - only that right now, our layer has only one neuron
    ```py {4|all}
    keras.layers.Dense(
        units=1, 
        input_shape=[1], 
        activation='sigmoid'
    )
    ```

2. change the loss function
   ```diff
   - loss=keras.losses.MeanSquaredError(),
   + loss=keras.losses.BinaryCrossEntropy(),
   ```

::right::

### Full example (NN part only)

```py {5|9|all}
model = keras.Sequential([
    keras.layers.Dense(
        units=1, 
        input_shape=[1], 
        activation='sigmoid'
    )
])
model.compile(
    loss=keras.losses.BinaryCrossEntropy(),
    optimizer=keras.optimizers.SGD()
)
```

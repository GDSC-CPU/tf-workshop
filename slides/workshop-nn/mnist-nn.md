---
layout: two-cols
---

# ML Model Code

```py
model = tf.keras.models.Sequential([
    keras.layers.Flatten(), # ❓
    keras.layers.Dense(128, activation='sigmoid'), 
    keras.layers.Dense(10, activation='softmax') # ❓
])

model.compile(
    optimizer=keras.optimizers.SGD(),
    loss='sparse_categorical_crossentropy', # ❓
    metrics=['accuracy']
)

# you should get around 89% accuracy w/ just 5 epochs
model.fit(training_images, training_labels, epochs=5)
``` 

What's `keras.layers.Flatten()`?

```py
training_images.shape # (60000, 28, 28)

keras.layers.Flatten()(training_images).shape
# (60000, 784)
```

::right::

# Flatten Layer

(a.k.a. _[let's not have a $60000 \times 28 \times 28$ ~~matrix~~ tensor][1]_)

Turns one training image from this:

$\begin{bmatrix}1 & 0 & 2 \\ 4 & 6 & 1 \\ 3 & 1 & 5 \end{bmatrix}$
&nbsp; &nbsp; into this &nbsp; &nbsp; 
$\begin{bmatrix}1 & 0 & 2 & 4 & 6 & 1 & 3 & 1 & 5 \end{bmatrix}$

_but we usually draw layer neurons vertically, it's more like_

<img alt="flatten" src="/images/flatten.png" style="height: 230px; margin-left: auto; margin-right: auto" />

[1]: https://www.tensorflow.org/guide/tensor

<style>
  .slidev-code {
    overflow: hidden;
  }
</style>
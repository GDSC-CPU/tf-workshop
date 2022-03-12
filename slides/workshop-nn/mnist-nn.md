---
layout: two-cols
---

# ML Model Code

```py
# we can normalize pixel brightness w/o MinMaxScaler
training_images_norm  = training_images / 255.0
test_images_norm = test_images / 255.0

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
model.fit(
    training_images_norm, # used to call this `X_norm`
    training_labels,      # used to call this `y`
    epochs=5
)
```

::right::

# Flatten Layer

(a.k.a. _[let's not have a $60000 \times 28 \times 28$ ~~matrix~~ tensor][1]_)

```py
training_images.shape # (60000, 28, 28)

keras.layers.Flatten()(training_images).shape
# (60000, 784)      # 👆 Python __call__ (callables)
```

Converts
$\begin{bmatrix}1 & 0 & 2 \\ 4 & 6 & 1 \\ 3 & 1 & 5 \end{bmatrix}$
&nbsp; &nbsp; into &nbsp; &nbsp; 
$\begin{bmatrix}1 & 0 & 2 & 4 & 6 & 1 & 3 & 1 & 5 \end{bmatrix}$

<div class="flex p-0 m-0">
  <img alt="flatten" src="/images/flatten.png" style="height: 220px; margin-left: auto; margin-right: auto; flex: 5" />

  <p style="flex: 3" class="pl-2">
    but we usually <strike>draw</strike> visualize layer neurons vertically, 
    so the <b>input layer</b> <i>kinda</i> receives pixel values from <b>one</b>
    training image <i>like this 👈</i> 
  </p>
</div>

[1]: https://www.tensorflow.org/guide/tensor

<style>
  .slidev-code {
    overflow: hidden;
  }

  .katex {
    font-size: 0.85em !important;
  }
</style>
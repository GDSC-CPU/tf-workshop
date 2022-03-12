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
    optimizer=keras.optimizers.SGD(),      # 👇🔻❓
    loss=keras.losses.SparseCategoricalCrossentropy(), 
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

<style>
  .slidev-code {
    overflow: hidden;
  }

  .katex {
    font-size: 0.85em !important;
  }
</style>
---
layout: two-cols
---

# ML Model Code

```py
# we can normalize pixel brightness w/o MinMaxScaler
training_images_norm  = training_images / 255.0
test_images_norm = test_images / 255.0

model = tf.keras.models.Sequential([
    keras.layers.Flatten(), # 🧘🌞💡
    keras.layers.Dense(128, activation='sigmoid'), 
    keras.layers.Dense(10, activation='softmax') # 🌞
])

model.compile(
    optimizer=keras.optimizers.SGD(),      # 👇🔻🌞
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

```py
# Evaluate the model on unseen data, see how many
# `test_labels` it predicts correctly.  I got ~89%
model.evaluate(test_images_norm, test_labels)

np.set_printoptions(precision=4, suppress=True)
def predict(index):
    plt.rcParams['figure.figsize'] = (4, 4)
    print(f'TEST LABEL: {test_labels[index]}', '\n')
    plt.imshow(test_images[index], cmap='gray')

    single_image = np.array([
        test_images[index] # just 28 x 28 (2D array)
    ]) # need to be a (something x 28 x 28) matrix

    probabilities = model.predict(single_image)
    print('PROBABILITIES: \n', probabilities)

    # np.max -> highest probability like 0.998, def.
    # not what we want, we're after THE INDEX (0-9)
    print('IMAGE IS A: ', np.argmax(probabilities))

# try in separate notebook cells
predict(4241)
predict(5555)
predict(1319)
predict(9888)
```

<style>
  .slidev-code {
    overflow: hidden;
  }

  .katex {
    font-size: 0.85em !important;
  }
</style>
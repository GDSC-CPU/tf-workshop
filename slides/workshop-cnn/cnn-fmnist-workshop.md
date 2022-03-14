# <twemoji-man-technologist /><twemoji-woman-technologist /> You do it!

You already have this vanilla neural network:

```py
model = keras.models.Sequential([
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'), 
    keras.layers.Dense(10, activation='softmax')
])
```

Now add the convolution and pooling layers like so:

```py
model = keras.models.Sequential([
    # colored images would be `input_shape=(28, 28, 3)`
    keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28, 28, 1)),
    keras.layers.MaxPooling2D(2, 2),
    keras.layers.Conv2D(32, (3,3), activation='relu'),
    keras.layers.MaxPooling2D(2,2),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'), 
    keras.layers.Dense(10, activation='softmax')
]) # what would be the accuracy on `model.fit(...)` and `model.evaluate(...)`??
```

<Countdown class="absolute right-4 top-8 text-orange-600" style="font-size: 2em; width: 40%;" />

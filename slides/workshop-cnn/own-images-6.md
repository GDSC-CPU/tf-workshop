# Using your own images

```py
test_generator = test_datagen.flow_from_directory(
    './cats_and_dogs_filtered/validation',
    target_size=(150, 150),
    batch_size=63,
    class_mode='binary'
)

history = model.fit(
    train_generator,
    steps_per_epoch=8,
    epochs=30,
    validation_data=test_generator,
    validation_steps=8
)
```

10.  Determine what number TF assigns to your labels.
      ```py
      print(train_generator.class_indices)
      ```

      ```
      {'cats': 0, 'dogs': 1}
      ```

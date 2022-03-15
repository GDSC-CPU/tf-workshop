# Using your own images

8.  Compiile as usual
    ```py
    model.compile(
        loss='binary_crossentropy',
        optimizer=keras.optimizers.Adam(),
        metrics=['accuracy']
    )
    ```

9. The training is a little different.  You get labeled images instead of giving `X` and `y`
    separately:
    ```py
    from tensorflow.keras.preprocessing.image import ImageDataGenerator

    train_datagen = ImageDataGenerator(rescale=1/255)
    test_datagen = ImageDataGenerator(rescale=1/255)

    train_generator = train_datagen.flow_from_directory(
        './cats_and_dogs_filtered/train',
        target_size=(150, 150),
        batch_size=125,
        class_mode='binary'
    )
    ```
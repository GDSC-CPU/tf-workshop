# Avoid Waiting for `480` Unnecessary Epochs

Sometimes, the accuracy reaches an accepteable %, say after 20 epochs

```py
class AccuracyWatcherCallback(tf.keras.callbacks.Callback):
    def __init__(self, threshold = 0.9):
        self.threshold = threshold

    # inherited and overriden method from superclass
    def on_epoch_end(self, epoch, logs = {}):
        # logs['c'] throws an exception, while logs.get('c') doesn't 
        if logs.get('accuracy') >= self.threshold:
            print(f"\nReached desired accuracy, stopping training.")
            self.model.stop_training = True

# during training, add this 👇👇
model.fit(X, y, epochs=500, callbacks=[AccuracyWatcherCallback(0.72)])
```

### Output

```
Epoch 6/30
8/8 [==============================] - 5s 681ms/step - loss: 0.5617 - accuracy: 0.6950 - val_loss: 0.6052 - val_accuracy: 0.6627
Epoch 7/30
8/8 [==============================] - ETA: 0s - loss: 0.4918 - accuracy: 0.7760
Reached desired accuracy, stopping training.
```

<style>
  .slidev-code {
    overflow: hidden;
  }
</style>
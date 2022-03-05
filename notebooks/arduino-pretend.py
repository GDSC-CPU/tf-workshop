import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('notebooks/for-arduino.h5')

print(model.predict(np.array([[8], [12]])))
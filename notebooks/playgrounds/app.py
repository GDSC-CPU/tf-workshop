import numpy as np
import tensorflow as tf
import joblib   # pip install joblib on your PC

from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler

model = keras.models.load_model('admission.h5')
exam1 = float(input("Enter score for Exam 1: "))
exam2 = float(input("Enter score for Exam 2: "))

scaler = joblib.load('admission-scaler.gz')
scaled_inputs = scaler.transform(np.array([
    [exam1, exam2]
]))

# this will be a 1x1 MATRIX containing True/False
result = model.predict(scaled_inputs) >= 0.5 

# a 1x1 matrix is a SCALAR! get it with bool()
should_admit = bool(result) # won't work if not 1x1

print('Admitted' if should_admit else 'Sorry 😭')
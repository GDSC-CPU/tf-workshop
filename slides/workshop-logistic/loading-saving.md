---
layout: two-cols
---

# Loading and Saving Models

1. If happy with the accuracy, save as:
   - `admission` - TF native format (SavedModel)
   - `admission.h5` - HDF5 format &nbsp; &nbsp; [<small>differences w/ 👆</small>][1]
   - [others formats][2] friendlier to other languages <small><i>e.g. JSON</i></small>

  ```py
  model.save('admission.h5')
  ```

2. If you feature-scaled, save your MinMaxScaler as well:
  ```py
  import joblib
  # some other imports ...

  scaler = MinMaxScaler()
  # fit, transform...
  joblib.dump(scaler, 'admission-scaler.gz')

  # 👇👇 only for notebooks on Google Colab
  from google.colab import files 
  files.download('admission.h5')
  files.download('admission-scaler.gz')
  ```

[1]: https://www.tensorflow.org/tutorials/keras/save_and_load#saving_custom_objects
[2]: https://www.tensorflow.org/js/tutorials/conversion/import_keras

::right::

#### In your vanilla Python app:

```py
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
```

<style>
  small {
    color: green;
    font-style: italic;
  }
</style>
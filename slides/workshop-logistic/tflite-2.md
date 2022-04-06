# <logos-tensorflow /> Lite <twemoji-red-heart /><twemoji-blue-heart /><twemoji-green-heart /><twemoji-yellow-heart /> <logos-flutter /> (<logos-python /> Python side)

- save the min max values as JSON:
  - yup, `joblib` is only for <logos-python /> to <logos-python /> _"serialization"_

```py
import json
min_max = { 'x_min': scaler.data_min_.tolist(), 'x_max': scaler.data_max_.tolist()}

with open('min-max.json', 'w') as json_file:
  json.dump(min_max, json_file)
```
- save the model as a TF Lite model:
```py
converter = tf.lite.TFLiteConverter.from_keras_model(model)

with open('model.tflite', 'wb') as tflite_file:
  tflite_file.write(converter.convert())  
```
- download if on Google Colab
```py
from google.colab import files

files.download('min-max.json')
files.download('model.tflite')
```
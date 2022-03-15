# Using your own images:

11.  Optional:  play with it on Colab.  The following code is Colab-exclusive.  It won't work
     on any other Jupyter notebooks.
      ```py
      import numpy as np
      from google.colab import files
      from keras.preprocessing import image

      uploaded = files.upload()

      for filename in uploaded.keys():
          path = '/content/' + filename
          uploaded_image = image.load_img(path, target_size=(150, 150))
          X = image.img_to_array(uploaded_image)
          X_norm = X / 255
          X_norm_3d = np.expand_dims(X_norm, axis=0)

          classes = model.predict(X_norm_3d, batch_size=8)

          if classes[0] >= 0.5:
              print('doggie')
          else:
              print('ugly kitty')
        ```
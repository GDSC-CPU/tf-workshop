# Using own images

You should see the extrated folders.
  ```
  total 8.0K
  drwxr-x--- 4 1002 1003 4.0K Sep 22  2016 train
  drwxr-x--- 4 1002 1003 4.0K Sep 22  2016 validation
  ```

6.  Verify that the folders contain the correct number of files:
    ```py
    import os

    train_dogs_dir = os.listdir('./cats_and_dogs_filtered/train/dogs')
    train_cats_dir = os.listdir('./cats_and_dogs_filtered/train/cats')
    test_dogs_dir = os.listdir('./cats_and_dogs_filtered/validation/dogs')
    test_cats_dir = os.listdir('./cats_and_dogs_filtered/validation/cats')

    len(train_dogs_dir), len(train_cats_dir), len(test_dogs_dir), len(test_cats_dir)
    ```

    ```
    (1000, 1000, 500, 500)
    ```
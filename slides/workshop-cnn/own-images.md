# Using a Training Set from Google Drive

1. Make sure your directory structure is something like this:
    ```sh
    ├── train
    │   ├── cats
    │   └── dogs
    └── validation
        ├── cats
        └── dogs
    ```

2. Easiest way is to upload this to Google Drive, and have Colab download it.
   Get its File ID:

   ```sh
   https://drive.google.com/file/d/1gMzpFgGyF1KMJhsMJ2pqDOGYgg98_ghJ/view?usp=sharing
   #                               ^___________THIS ONE____________^
   ```

3. Download it from Colab using the [`gdown`][1] command preinstalled by Colab.  Write this
   command on a Jupyter cell.  `!` means a Linux command, since the Colab VM
   is an Ubuntu Linux machine.

  ```sh
  !gdown --id 1gMzpFgGyF1KMJhsMJ2pqDOGYgg98_ghJ
  ```

[1]: https://pypi.org/project/gdown/
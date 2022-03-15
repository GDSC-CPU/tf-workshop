# Using your own images

You should see something like this for the output cell.
```
Downloading...
From: https://drive.google.com/uc?id=1-OsSKExQU7JJP-4PuXYerBA5-rlt_qpB
To: /content/cats_and_dogs_filtered.tar.xz
100% 66.9M/66.9M [00:00<00:00, 288MB/s]
```

4. Unzip (or untar in my case) the training samples.  Use the `zipfile` module
   if you used a ZIP file.

    ```py
    import tarfile

    cats_dogs_tar = tarfile.open('./cats_and_dogs_filtered.tar.xz', 'r')
    cats_dogs_tar.extractall('')
    cats_dogs_tar.close()
    ```

5. You can check if the file was really untarred or unzipped using the `ls`
   command in Linux.
   ```sh
   !ls -lh cats_and_dogs_filtered
   ```

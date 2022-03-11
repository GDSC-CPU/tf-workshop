---
layout: two-cols
---

# Visualizing the first 100 images from the training set

```py
import matplotlib.pyplot as plt

# taller vertical size coz of Label: <digit>
plt.rcParams['figure.figsize'] = (16, 20) 

for i in range(100):
    # 10x10 grid, draw at index `i` (1-based)
    plt.subplot(10, 10, i + 1)

    # without `cmap='gray'`, it will be greenish
    plt.imshow(training_images[i], cmap='gray')
    plt.title(f"Label: {training_labels[i]}")
```

Notice the axes labels.  It shows that the images are 28x28
pixels in size.

::right::

<img alt="digits" src="/images/digits.jpg" style="height: 480px" />

---
layout: two-cols
---

# Visualize a single image

```py
# Play with this in your notebook
index = 4241 # indices are from 0 to 59_999

# Set number of characters per row when printing
np.set_printoptions(linewidth=320)

# Print the traiing label 
print(f'LABEL: {training_labels[index]}')

# and the image's matrix representation
print(f'\nIMAGE MATRIX:\n {training_images[index]}')

plt.imshow(training_images[index], cmap='gray')
```

Here you see the image's actual image, and its matrix representation.
- 0 is black, it gets brighter with values nearer 255
- also notice the axes (too small), it's still showing 28x28

::right::

<img alt="matrix" src="/images/image-matrix.png" />
<img alt="digit" src="/images/single-digit.jpg" style="height: 230px; margin-left: auto; margin-right: auto;" />
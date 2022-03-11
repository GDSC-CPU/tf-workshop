---
layout: two-cols
---

# Visualize a single image

```py
# Set number of characters per row when printing
np.set_printoptions(linewidth=320)

def show_image(index):# Print the traiing label 
    print(f'LABEL: {training_labels[index]}', '\n')

    # and the image's matrix representation
    print(f'MATRIX:\n {training_images[index]}')

    plt.imshow(training_images[index], cmap='gray')

# Play with this in your notebook
show_image(14_344) # indices are from 0 to 59_999
show_image(4_241)  # yeah lucky number
```

- Here you see the image's actual image, and its matrix representation.
- minus the numbers to indicate the pixels' brightness, the matrix does look 
  like the handwritten digit image right?

::right::

<img alt="matrix" src="/images/image-matrix.png" />
<img alt="digit" src="/images/single-digit.jpg" style="height: 230px; margin-left: auto; margin-right: auto;" />
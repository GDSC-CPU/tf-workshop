---
layout: two-cols
---

# Convolutional Neural Nets

[From Wikipedia](https://en.wikipedia.org/wiki/Convolutional_neural_network):

> In deep learning, a convolutional neural network (CNN, or ConvNet) is a class of Artificial Neural Network(ANN), most commonly applied to analyze visual imagery.

- CNNs are often used in image recognition systems. 
- In 2012 an error rate of 0.23% on the MNIST database was reported.
- When applied to facial recognition, CNNs achieved a large decrease in error rate.
- Another paper reported a 97.6% recognition rate on "5,600 still images of more than 10 subjects".
- In 2015 a CNN demonstrated the ability to spot faces from a wide range of angles, including upside down, even when partially occluded, with competitive performance...

::right::

### *or **CNN** for short*

- involves two special layers:
  - **convolutional layer**: the core building block of a CNN, and it is where the majority of computation occurs.  It essentially applies a **filter** (or a kernal) to an image
    - GOAL: highlight important parts of the image (***high-level features***)
    - e.g. for a flight of stairs, your brain _"kinda ignores"_ its color and materials.
      - but do they look like _"rectangles"_ or _"bars"_ stacked on top of each other?
  - **pooling layer**:  also known as downsampling, conducts dimensionality reduction, reducing the number of parameters in the input.
    - GOAL: reduce the size of the convolved image

<style>
  blockquote {
    font-size: 1em;
  }

  h3 {
    margin-bottom: 4px;
  }
</style>
---
layout: two-cols
---

# Experiments

Notebook: 

- Try breaking your code
  1. What if you remove the `Flatten()` layer?
  2. What if you only specify `5` neurons in the output layer?

::right::

- Try reconfiguring the NN:
  1. Change the optimizer from `SGD()` to `Adam()`.
  2. Change the activation from `sigmoid` to `relu`.
  3. Try changing both.
  4. Try increasing the number of neurons to 512, and to 1024.
  5. Try adding another hidden layer with 128 neurons.
  6. Try increasing the epochs to 15, and to 30.
  7. Try turning off feature normalization.
  8. Try changing the dataset from MNIST to Fashion MNIST.
     - more complicated data, accuracy should lower
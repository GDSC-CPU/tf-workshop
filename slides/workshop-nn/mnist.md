---
layout: two-cols
---

# MNIST

- _Modified_ [National Institute of Standards and Technology](https://www.nist.gov/)
- is a large database of **handwritten digits**
- widely used for training and testing in the field of machine learning

<img alt="mnist" src="/images/mnist.png" style="height: 300px" />

::right::

# Let's get spoonfed 🥣 by <logos-tensorflow />

```py
mnist = tf.keras.datasets.mnist
```

* Many popular datasets are _"built-in"_, or _"preloaded"_ in many ML libraries
  - Boston Housing is one example: we don't have to load house pricing data from a CSV
  - although this dataset has [ethical issues][1], and was [deprecated][2] in Scikit-learn
* Convenience: gets rid of distractions in bringing your own images, loading CSVs
    - can focus on the core ML stuff
    - very helpful especially for learning and research
* [Guide](https://www.tensorflow.org/datasets) and 
  [List of Datasets](https://www.tensorflow.org/datasets/catalog/overview#all_datasets) for TensorFlow

[1]: https://medium.com/@docintangible/racist-data-destruction-113e3eff54a8
[2]: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_boston.html

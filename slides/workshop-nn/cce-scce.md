---
layout: two-cols
---

# ~~Binary~~ Categorical Cross Entropy (CCE)

Binary = _"2 classes"_, Categorical = _"multiple classes"_

From the [Keras docs][1]:

> Use this crossentropy loss function when there are two or more label classes. We expect labels to be provided in a `one_hot` representation. If you want to provide labels as integers, please use `SparseCategoricalCrossentropy` loss.

<img alt="multilabel" src="/images/multilabel.png" />
<div style="text-align: right; width: 100%" class="pr-4">
  <a href="https://machinelearningmastery.com/why-one-hot-encode-data-in-machine-learning/">
    <small>Can single-label data also be one-hot encoded?</small>
  </a>
</div>

[1]: https://keras.io/api/losses/probabilistic_losses/#categoricalcrossentropy-class

::right::

# Sparse Categorical Cross Entropy (SCCE)

<u>mnemonic</u>: sparse = _"fewer information"_

Also from the [Keras docs][2]:

> Use this crossentropy loss function when there are two or more label classes. We expect labels to be provided as integers. If you want to provide labels using `one-hot` representation, please use `CategoricalCrossentropy` loss.

[2]: https://keras.io/api/losses/probabilistic_losses/#sparsecategoricalcrossentropy-class

###### [TL:DR](https://datascience.stackexchange.com/a/55987):  look at the shape of the $y$ labels:

- If $y$ looks like this:  
  <small>each row is an array of 1s and 0s</small>
$y = \begin{bmatrix}
    0 & 0 & 1 \\
    1 & 0 & 0 \\
    0 & 1 & 0 \\
    0 & 0 & 1 
  \end{bmatrix}
$  
<br>use **CCE**

- if $y$ looks like this:  
<small>each row is JUST AN INTEGER</small>
$
  y = \begin{bmatrix}
    2 \\
    0 \\ 
    1 \\
    2 \\
  \end{bmatrix}
$  
<br>use **SCCE**

<style>
  ul {
    display: flex;
    margin-top: 0px;
  }

  h6 {
    font-size: 0.9em !important;
    text-transform: none !important;
    margin-bottom: 0px;
    color: darkorange;
    opacity: 1 !important;
    font-weight: 700 !important;
  }
  
  ul li {
    flex: 1;
  }

  li p {
    margin-top: 0px;
    padding-top: 0px;
  }

  small {
    color: green;
    font-style: italic;
  }
</style>
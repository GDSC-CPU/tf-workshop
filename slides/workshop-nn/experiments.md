---
layout: two-cols
---

# Experiments

Notebook: 

- Try breaking your code.  What happens if you...
  1. try to remove the `Flatten()` layer?
  2. specify only `5` neurons in the output layer?

Try to put `%%time` before each code cell, so that you can note how long training
takes with different combinations of hyperparameters.

```py
%%time
train(hidden_layers_activation='sigmoid')
```

You should see the following added to each output cell:
```
CPU times: user 30.2 s, sys: 3.66 s, total: 33.8 s
Wall time: 28.9 s
```

::right::

Fashion MNIST are more _"complicated"_, so lower accuracy compared to 
_"digits"_ MNIST is understandable.
- Try reconfiguring NN hyperparameters, while making observations on
  training accuracy, testing accuracy, and training time.
  <sup><u>🍲 for thought</u>:  What's 0.5% of 60,000, and of 10,000?</sup>
  1. Change the optimizer from `SGD()` to `Adam()` and vice versa in any of the combos below.
  2. Change the activation from `sigmoid` to `relu`. 
     -                           What's that? 👆❓😮😱
  3. Try increasing the number of hidden layer neurons to 512, and also 1024.
  4. Try adding another hidden layer with 128 neurons.
  5. Try increasing the epochs to 15, and to 30.
  6. Try turning off feature normalization.

<style>
  li li li {
    list-style: none;
  }

  li li li code {
    color: green;
    font-size: 0.8em;
    font-style: italic;
  }

  sup {
    font-style: italic !important;
    color: green;
    font-size: 0.75em;
    margin-left: 16px;
  }
</style>
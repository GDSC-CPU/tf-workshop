---
layout: fact
---

<Congratz
  achievement="knowing your third activation function"
  message="Remember its acronym: ReLU"
  secondary="We only use it in the hidden layer."
  compact
/>

<div class="text-gray-500 italic mb-8">
  Don't forget about our old friend sigmoid.  It's is still a valid activation 
  in <a href="https://towardsdatascience.com/how-to-choose-the-right-activation-function-for-neural-networks-3941ff0e6f9c">some types of NN like RNNs</a>.
  
  Sigmoid is also a great activation function for the output layer of a binary classifier.
</div>

```py
# other layers...,
keras.layers.Dense(activation='relu'),
# other layers...
```

<style>
  .shiki-container {
    text-align: left;
    width: 50%;
    margin-left: auto;
    margin-right: auto;
  }
</style>
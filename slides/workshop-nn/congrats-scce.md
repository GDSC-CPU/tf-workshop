---
layout: fact
---

<Congratz
  achievement="knowing your third loss function"
  message="Sparse Categorical Cross Entropy"
  secondary="Another long and scary name to remember!"
  caveat="It's actually similar to Binary Cross Entropy, but for multi-class classification."
  compact
/>

- 
  ```py
  model.compile(
      loss=keras.losses.SparseCategoricalCrossentropy(),
      # others...
  )
  ```

- 
  > It even has a [similar formula][1]: $J = -\sum\limits_{i = 1}^{n}y_i\log(p_i)$  
  > where $n$ is the number of classes,  
  > and $p_i$ is the softmax probability for the $i^{th}$ class

[1]: https://towardsdatascience.com/cross-entropy-loss-function-f38c4ec8643e

<style>
  .shiki-container {
    text-align: left;
    flex: 1;
  }

  blockquote {
    flex: 1;
    text-align: left;
  }

  .katex {
    color: darkorange;
  }

  ul {
    display: flex !important;
    flex-direction: row;
  }

  ul li {
    list-style: none;
  }
  
  li p {
    color: goldenrod;
  }
</style>
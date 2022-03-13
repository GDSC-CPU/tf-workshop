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
  > It even has a similar formula:
  > $$
  > J = -y \odot \log(p)
  > $$  

<style>
  .shiki-container {
    text-align: left;
  }

  blockquote {
    text-align: left;
  }

  .katex {
    color: darkorange;
  }

  ul {
    display: flex !important;
    flex-direction: row;
    justify-content: center;
  }

  ul li {
    list-style: none;
  }
  
  li p {
    color: goldenrod;
  }
</style>
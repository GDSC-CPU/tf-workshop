---
layout: fact
---

<Congratz
  achievement="knowing your second NN layer"
  message="Flatten"
  caveat="Dense was the first layer you learned, but was too early to congratulate 😂"
  secondary="Images are 2D arrays, and the Flatten layer 😮‍💨 flattens them into 1D."
/>

```py
# just add before your first Dense() layer
keras.layers.Flatten()
```

<style>
  .shiki-container {
    margin-top: 64px;
    text-align: left;
    width: 50%;
    margin-left: auto;
    margin-right: auto;
  }
</style>
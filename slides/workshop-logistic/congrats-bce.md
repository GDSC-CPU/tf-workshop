---
layout: fact
---

<Congratz
  achievement="knowing your second loss function"
  message="Remember its name: Binary Cross Entropy"
  secondary="Also remember and UNDERSTAND the how and why"
  caveat="Even if you can't remember the formulas and derivatives, TF / Keras will 😉"
/>

```py
model.compile(
    loss=keras.losses.BinaryCrossentropy()
)
```

<style>
  .shiki-container {
    text-align: left;
    width: 50%;
    margin-left: auto;
    margin-right: auto;
  }
</style>
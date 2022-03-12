---
layout: fact
---

<Congratz
  achievement="knowing your second activation function"
  message="Remember its name: Softmax"
  secondary="Also remember and UNDERSTAND the how and why."
  caveat="It's used only in the output layer, and only for multi-class classification."
  compact
/>

```py
keras.layers.Dense(number_of_classes, activation='softmax')
```

<h5 v-click class="mt-8 text-orange-500" style="width: 80%; margin-left: auto; margin-right: auto;">
  ❓ <span class="text-yellow-500 underline">For Php50 load:</span>
  What will happen if you use <i>softmax</i> as the activation function for the 
  output layer of a binary classifier? <b>WHY?</b> &nbsp; 
  <i>+ What activation function should we use instead?</i>
</h5>

<style>
  .shiki-container {
    margin-top: 16px;
    text-align: left;
    width: 60%;
    margin-left: auto;
    margin-right: auto;
  }
</style>
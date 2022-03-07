---
layout: fact
---

<Congratz
  achievement="on knowing your first loss function!"
  message="Remember its name: Mean Squared Error"
  secondary="Also remember and UNDERSTAND the how and why."
  caveat="Even if you can't remember either formula, TF / Keras will remember it for you."
/>

> Unvectorized: $\frac{1}{2m} \sum\limits_{i = 1}^{m}(y_i - \hat{y_i})^2$
> &nbsp; &nbsp; Vectorized: <span class="vectorized">$\frac{1}{2m}(Xw - y)^T(Xw - y)$</span>

<style>
  .katex {
    color: darkorange;
  }
</style>
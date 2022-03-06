---
layout: two-cols
---

# Gradient Descent

- goal is to **minimize** the loss function $f(w)$:

  `start with a "random-ish" ` $w$ ` vector`  
  `repeat for several iterations:`  
      &nbsp; &nbsp; &nbsp; &nbsp; $w = w - \alpha  \frac{\partial}{\partial{w}}f(w)$ 

<img alt="baby steps" src="/images/baby-steps.png" />

[2]: https://medium.com/@shiny_jay/linear-regression-2c2ae9507aba

::right::

# Learning rate

- $\alpha$ stands for the **learning rate** (sometimes called ***step size***)
  * too big and you'll overshoot the minimum
  * too small and it'll slow down your model's training
  * $\alpha$ has to be _"just right"_, i.e. find the _"sweet spot"_

<img 
  alt="learning rate" 
  src="/images/learning-rate-2.png" 
  class="ml-2"
  style="width: 510px; height: 267px" 
/>
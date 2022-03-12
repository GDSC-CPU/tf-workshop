---
layout: two-cols
---

# [Meet Adam](https://machinelearningmastery.com/adam-optimization-algorithm-for-deep-learning/)

Adaptive moment estimation

- an extension to **stochastic gradient descent**
- has recently seen broader adoption in 
  - **computer vision** and 
  - natural language processing
- by *Diederik Kingma* from OpenAI and *Jimmy Ba* from the University of Toronto
- 2015 ICLR _(<small>International Conference on Learning Representations</small>)_ paper 
  _"Adam: A Method for Stochastic Optimization"_
- SDG maintains a single learning rate (termed $\alpha$)
  - learning rate does not change during training.
- Adam learning rate is maintained for each network weight and separately adapted as learning 
  unfolds.

::right::

<img alt="adam graph" src="/images/optimizer-comp.gif" style="height: 280px; width: 400px; margin-left: auto; margin-right: auto" />

> [Many other algorithms have been made on top of gradient descent][1]
> - Adagrad
> - RMSprop
> - **Adam**

> [Gradient Descent is the backbone](https://medium.com/analytics-vidhya/all-about-gradient-descent-in-machine-learning-and-deep-learning-3dea4b269bf0) of every machine learning algorithm and it also acts as a base for many deep learning optimizers.

[1]: https://ruder.io/optimizing-gradient-descent/

<style>
  blockquote {
    margin-left: 16px;
    margin-top: 16px;
  }
</style>

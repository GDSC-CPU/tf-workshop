---
layout: quote
---

### ❓ Why is $w$ from TF and the _from-scratch_ version different?

 > # [The downside of stochastic gradient descent is that it doesn’t find the true minimum as reliably. Instead it has a tendency to get extremely close...][1]


 <logos-tensorflow /> doesn't have the [BGD][2] built-in, [only SGD][3].

 > **Batch gradient descent** (BGD) is a type of gradient descent which processes all the training examples for each iteration of gradient descent. But if the number of training examples is large, then batch gradient descent is computationally very expensive. 

## Whatever <twemoji-man-shrugging class="animate-pulse" /> They're pretty close.

 [1]: https://towardsdatascience.com/understanding-gradient-descent-35a7e3007098
 [2]: https://medium.com/@kumaranupam2020/difference-between-batch-gradient-descent-bgd-minibatch-gradient-descent-mgd-and-stochastic-657efcb4194b
 [3]: https://www.tensorflow.org/api_docs/python/tf/keras/optimizers
 
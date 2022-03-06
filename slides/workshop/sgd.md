# [Stochastic Gradient Descent (SGD)][1]

- based on the assumption that the errors are additive. 
  * The error at point one can be added to the error at point two, 
    which can be added to the error at point three, and so on for all of the points.
- model doesn’t need to calculate the error at all points simultaneously - 
  _**a computationally expensive process**_
- calculate the error at each point individually, and sum them together.
- this assumption is ***almost*** always true
- still, it’s best practice to think for a moment to ensure that it’s true in your problem

<div class="mt-2"></div>

<h3 class="text-orange-500">TL:DR -- This saves dramatic amounts of computation time.</h3>

> 👎 [The downside of stochastic gradient descent is that it doesn’t find the true minimum as reliably. Instead it has a tendency to get extremely close, then circle the minimum forever. ][1]

 <logos-tensorflow /> Tensorflow doesn't have the [BGD][2] built-in 
 <small class="text-gray-500">_(many beginner tutorials teach the simpler BGD)_</small>,
 [only SGD][3].

 > **Batch gradient descent** (BGD) is a type of gradient descent which processes all the training examples for each iteration of gradient descent. But if the number of training examples is large, then **batch gradient descent is computationally very expensive.**

 [1]: https://towardsdatascience.com/understanding-gradient-descent-35a7e3007098
 [2]: https://medium.com/@kumaranupam2020/difference-between-batch-gradient-descent-bgd-minibatch-gradient-descent-mgd-and-stochastic-657efcb4194b
 [3]: https://www.tensorflow.org/api_docs/python/tf/keras/optimizers
 
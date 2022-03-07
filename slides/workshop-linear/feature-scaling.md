---
layout: quote
---

# Feature Scaling

<div></div>

Quoting from [Analytics Vidhya][1]:

> ##### The presence of feature value X in the formula will affect the step size of the gradient descent. The difference in ranges of features will cause different step sizes for each feature. To ensure that the gradient descent moves smoothly towards the minima and that the steps for gradient descent are updated at the same rate for all the features, we scale the data before feeding it to the model.

> #### **Having features on a similar scale can help the gradient descent _converge more quickly towards the minima_.**

Quoting from the [Tensorflow tutorial on Basic Regression][2]:

> #### **It is good practice to normalize features that use different scales and ranges.**

> ##### One reason this is important is because the features are multiplied by the model weights. So, the scale of the outputs and the scale of the gradients are affected by the scale of the inputs.

> #### **Although a model might converge without feature normalization, normalization makes training much more stable.**

[1]: https://www.analyticsvidhya.com/blog/2020/04/feature-scaling-machine-learning-normalization-standardization/

[2]: https://www.tensorflow.org/tutorials/keras/regression#the_normalization_layer

<style>
  em {
    text-decoration: underline
  }
</style>
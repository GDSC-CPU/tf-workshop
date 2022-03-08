---
layout: two-cols
---

# Activation Functions

<div></div>

> [When our brain is fed with a lot of information simultaneously, it tries hard to understand and classify the information into “useful” and “not-so-useful” information.][1]

> We need a similar _"neuron 💡 up"_ mechanism for classifying incoming information as “useful” or “less-useful” in case of **Neural Networks.**

- Activation functions determine the output of neural network like yes or no. It maps the resulting values to a certain range: **0 to 1** or **-1 to 1**, etc.

- [The need for these activation functions includes converting the linear input signals and models into non-linear output signals, which aids the learning of high order polynomials for deeper networks.][2]
  * <twemoji-warning /> A neural network without an activation function is **essentially just a linear regression model.**

[1]: https://www.analyticsvidhya.com/blog/2020/01/fundamentals-deep-learning-activation-functions-when-to-use-them/

[2]: https://www.analyticsvidhya.com/blog/2021/04/activation-functions-and-their-derivatives-a-quick-complete-guide/

::right::

<img alt="activation" src="/images/activation.png" />

> <mdi-format-quote-open /> [Linear functions are only single-grade polynomials that render the neuron to act as a linear regression model.  No matter how many linear functions we stack, we will always get a linear function as an output. Hence activation of the linear combiner enables us to **create complex decision boundaries** by using a combination of multiple neurons.][3] <mdi-format-quote-close />

<img alt="boundary" src="/images/boundary.jpg" />

[3]: https://www.sciencedirect.com/topics/engineering/activation-function

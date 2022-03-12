---
layout: two-cols
---

# Rectified Linear Unit (ReLU)

_a.k.a. "another simple formula with a scary name"_

$
R(z) = \begin{cases}
  0, & \text{if } z \gt 0\\
  x, & \text{otherwise}
\end{cases} = max(0, x)
$

```python
def relu(z): return x if z > 0 else 0 # OR
def relu(z): return max(0, z)
```

<img alt="relu graph" src="/images/relu-graph.png" style="height: 200px" />

- has become the [default activation function][1] for the **hidden layer** of many
  neural networks. [<small>(not all)</small>][2]

::right::

1. ReLU is more lightweight computationally vs $\frac{1}{1 + e^{-z}}$

<img alt="relu" src="/images/relu-light.png" />

2. No vanishing gradient, [only saturates when $z \lt 0$][4]

<img alt="relu gradient" src="/images/saturation.png" />
  
> derivative $R'(z)$ is just 0 or 1;  
> since $R(z)$ is either $0$ or $z$

[1]: https://machinelearningmastery.com/rectified-linear-activation-function-for-deep-learning-neural-networks/
[2]: https://towardsdatascience.com/how-to-choose-the-right-activation-function-for-neural-networks-3941ff0e6f9c
[3]: https://en.wikipedia.org/wiki/Recurrent_neural_network
[4]: https://wandb.ai/ayush-thakur/dl-question-bank/reports/ReLU-vs-Sigmoid-Function-in-Deep-Neural-Networks-Why-ReLU-is-so-Prevalent--VmlldzoyMDk0MzI

<style>
  small {
    color: green;
  }

  blockquote {
    position: absolute;
    color: darkorange !important;
    bottom: 190px;
    right: 64px;
    background-color: transparent !important;
    border-left-color: goldenrod !important;
  }
</style>
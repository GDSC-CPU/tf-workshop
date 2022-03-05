---
layout: two-cols
---

# [Hyperparameters](https://towardsdatascience.com/parameters-and-hyperparameters-aa609601a9ac)

- set/***tuned*** by **us** - *the machine learning practitioners*
- parameters whose values control the learning process
- these values **cannot** be changed by the ML model
- we've already learned **two**
  * learning rate $\alpha$
  * number of iterations (epochs)
- we'll also learn other hyperparams in the 2-day workshop
  * choice of optimizer
  * choice of actvation function
  * choice of loss function
  * train-test split ratio
  * number of hidden layers in our NN
  * number of units (neurons) in each NN layer
  * filter size and pooling size in our CNNs

::right::

# Parameters

- **learned** by the machine based on our training data
- the model can change these values
- example: the weights $w$ of a neural network

<img class="mt-12 ml-8" alt="hyperparams" src="/images/hyperparams.png" />
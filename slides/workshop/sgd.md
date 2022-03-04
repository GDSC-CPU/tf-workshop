# [Stochastic Gradient Descent (SGD)][1]

- based on the assumption that the errors are additive. 
  * The error at point one can be added to the error at point two 
  * which can be added to the error at point three, and so on for all of the points.
- model doesn’t need to calculate the error at all points simultaneously
  * _a computationally expensive process_
- calculate the error at each point individually, and sum them together.
- this assumption is almost always true
- still, it’s best practice to think for a moment to ensure that it’s true in your problem

## TL:DR This saves dramatic amounts of computation time.

[1]: https://towardsdatascience.com/understanding-gradient-descent-35a7e3007098
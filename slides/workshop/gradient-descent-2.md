# Gradient Descent

- Because we're trying to minimize cost, we get the derivative of the loss function $J(w)$.

  $J(w) = \frac{1}{2m}(Xw - y)^T(Xw - y)$

- If you use the _"halved"_ version of MSE, the _"sorta-invisible"_ $^2$ and $\frac{1}{2}$
  will cancel out due to the power rule.

  $\frac{\partial}{\partial{w}}J(w) = \frac{1}{m}X^T(Xw - y)$

<div class="italic text-xs text-gray-400">
  If interested in the derivation, see
  <a href="https://ayearofai.com/rohan-3-deriving-the-normal-equation-using-matrix-calculus-1a1b16f65dda">
    this article on the Normal Equation
  </a> or 
  <a href="https://medium.com/@shiny_jay/linear-regression-2c2ae9507aba">maybe this</a>
  and stop when you reach the part that says
  <code>Cost'(θ) = 2X<sup>T</sup>Xθ - 2X<sup>T</sup>y</code>
</div>

- Gradient descent is just a loop:

  `start with a random ` $w$ ` vector`  
  `repeat for several iterations:`  
      &nbsp; &nbsp; &nbsp; &nbsp; $w = w - \alpha  \frac{\partial}{\partial{w}}J(w)$
  
- $w$ should now be optimized

[2]: https://medium.com/@shiny_jay/linear-regression-2c2ae9507aba

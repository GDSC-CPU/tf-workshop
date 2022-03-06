---
layout: fact
---

<Congratz
  achievement="on knowing your first optimizer!"
  message="Remember its acronym: SGD"
  secondary="Also remember the how and why."
  caveat="You don't even have to know the partial derivatives  of loss functions like MSE"
/>

> If interested, it's $\frac{\partial}{\partial{w}}J(w) = \frac{1}{m}X^T(Xw - y)$
> <small class="ml-8">
>   <a class="variant" href="https://ayearofai.com/rohan-3-deriving-the-normal-equation-using-matrix-calculus-1a1b16f65dda">
>     long derivation of unfactorized variant: $2X^TX\theta - 2X^Ty$
>   </a></small>


<style>
  blockquote {
    color: goldenrod !important;
  }

  .katex {
    color: darkorange;
  }

  small {
    color: green;
  }

  .variant .katex {
    color: green !important;
  }
</style>
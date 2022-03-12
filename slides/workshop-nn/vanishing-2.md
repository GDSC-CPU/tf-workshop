---
layout: two-cols
---

# [Vanishing Gradient](https://medium.com/analytics-vidhya/how-batch-normalization-and-relu-solve-vanishing-gradients-3f1a8ace1c88)

The best explanation on the Web <twemoji-backhand-index-pointing-down /><twemoji-backhand-index-pointing-down />!

- What will happen if the derivative term in the equation is too small, i.e. almost zero? 
- We can see that a very small derivative would update or change the value of $W_x$ only by a minuscule amount
- hence, $^*W_x$ would be almost equal to the $W_x$.
- **No change in the weights means no learning.**
- The weights of the initial layers would continue to remain unchanged (or only change by a negligible amount)
  - no matter how many epochs you run
- The graph of sigmoid and its derivative shows that the safe zone is around
  $-5$ to $+5$, then it _"saturates"_.
- the maximum possible value for $\sigma'(z)$ is $0.25$ when $z = 0$

::right::

<img alt="vanishing" src="/images/formula-again.png" />
<img alt="sigmoid-safe" src="/images/sigmoid-derivative.png" style="height: 220px" />

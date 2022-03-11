---
layout: two-cols
---

# [Vanishing Gradient](https://medium.com/analytics-vidhya/how-batch-normalization-and-relu-solve-vanishing-gradients-3f1a8ace1c88)

The best explanation on the Web <twemoji-backhand-index-pointing-down /><twemoji-backhand-index-pointing-down />!

- What will happen if the derivative term in the above equation is too small, i.e- almost zero? 
- We can see that a very small derivative would update or change the value of $W_x$ only by a minuscule amount
- hence, the (new) $*W_x$ would be almost equal to the (older) $W_x$. 
- No change has been made to the model weights. 
  - No change in the weights means no learning. 
- The weights of the initial layers would continue to remain unchanged (or only change by a negligible amount)
  - no matter how many epochs you run with the backpropagation algorithm. 

::right::

<img alt="vanishing" src="/images/formula-again.png" />
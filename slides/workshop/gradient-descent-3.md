---
layout: two-cols
---

# Gradient Descent Code

- Let's try it on a parabola
  * Say the equation is $y = 2(x - 5)^2 + 3$
  * Derivative is: $\frac{dy}{dx} = 4(x - 5)$
    <img alt="parabola" src="/images/parabola.jpg" style="width: 300px; height: 200px" />
  * We can see that when $x$ is $5$, $y$ is minimized
  * And true, setting $\frac{dy}{dx} = 0$, we get
    + $4(x - 5) = 0$; thus $x$ should be $5$

::right::

```py
def gradient_descent(initial_x):
    x = initial_x
    learning_rate = 0.1

    for i in range(1000):
        derivative = 4 * (x - 5)
        x -= learning_rate * derivative

    return x    
```

Testing it on `initial_x = 0`, and also `10`, we get:

```py
gradient_descent(0) # returns 4.999999999999999
gradient_descent(10) # returns 5.000000000000001
```

<twemoji-party-popper class="animate-ping" /> Yay! Pretty close don't you think?

<div class="text-green-700 bold border border-green-700 bg-green-200 p-2 text-center rounded-xl" v-click>
  Calculus makes 💻 machines learn from - and minimize - their <i>"errors"</i>
  <twemoji-double-exclamation-mark />
</div>

<h5 v-click class="mt-4 text-orange-500">
  ❓ <span class="text-yellow-500 underline">For Php50 load:</span>
  If we increase the iterations of the loop, will it go from the <code>minimum</code> 
  and walk upwards the parabola? <b>WHY?</b>
</h5>
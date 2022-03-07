# [Gradient Descent][1]

## or _"How to get the weights with the lowest cost?"_

- Parabolas have both constantly changing slopes and a ***minimum*** point. 
- The ***minimum*** point occurs where the **slope is zero**
  + that’s also the point where the slope begins to increase on the other side
- the ***minimum*** occurs at the point where the **derivative** of the equation 
  **is equal to zero**

## How does it work?
1. Calculates the partial derivative of each variable at the point in question
2. Combines the partial derivatives with respect to each variable to identify the
   direction of most negative slope across the vector space
3. Steps in the direction of the most negative slope
4. Repeats the process until it finds the minimum point.

[1]: https://towardsdatascience.com/understanding-gradient-descent-35a7e3007098

# Backpropagation

* As a simple analogy:
  1. From the output layer (***the desired state***), I have this image, labeled as $2$.  
  2. What can I do to increase the weights of those related to 2, 
     and decrease the ones that aren't related?
     - such that I will make less mistakes when shown a $2$ in the future?
  3. Then repeatedly work backwards towards the previous layer so they too, adjust

<img alt="backprop" src="/images/backprop.png" />
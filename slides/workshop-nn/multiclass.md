---
layout: two-cols
---

# Multi-class Classification

- We only need **one** neuron in the ***output layer*** for binary classification
  (_one decision boundary_)
- **three** to classify 
  <mdi-triangle-outline class="text-green-500" />
  <mdi-square-outline class="text-indigo-500" />
  <mdi-close class="text-red-500" />
  * <mdi-triangle-outline class="text-green-500" /> vs NOT <mdi-triangle-outline class="text-green-500" />, 
  <mdi-square-outline class="text-indigo-500" /> vs NOT <mdi-square-outline class="text-indigo-500" />, 
  <mdi-close class="text-red-500" /> vs NOT <mdi-close class="text-red-500" />
- **four** neurons to classify 4 classes, etc.
- _"no such thing"_ as a two-unit output layer

<img alt="4 classes" src="/images/4-classes.jpg" style="height: 215px" />
<small class="italic text-green-600">
  BCE here is B-cell epitopes (antibodies), not Binary Cross Entropy 😂
</small>

::right::

<img alt="binary" src="/images/binary-vs-multi.png" />
<img alt="multi" src="/images/one-vs-rest.png" style="height: 250px; width: 450px" />

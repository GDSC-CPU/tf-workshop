---
layout: two-cols
---

# Machines need lots of data

- <twemoji-warning /> **Spoiler alert**: Example for image classification
  
  * image pixels [**flattened**][1] such that they become a single ROW in a matrix
    + an image of 100x100 pixels = 10k inputs if graysale, 30k if colored (RGB)
  * if you train with 30,000 pictures of cats and 30,000 pictures of dogs, then
    + that's 60,000 rows _(1 row per training sample)_
  * $10,000 \times 60,000$ matrix? _Take that EMath 2200!!_
  * Each neuron (_green circle_) are also matrices 😁😁
  * Many operations are safe to do in parallel
    - e.g. addition, multiplication, summation

::right::

# <span class="text-teal-500/80">_just like some of us need lots of examples to learn well_</span>

<img alt="ann" src="/images/ann-1hidden.png" style="width: 450px; height: 350px" />

[1]: https://www.tensorflow.org/api_docs/python/tf/keras/layers/Flatten
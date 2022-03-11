---
layout: fact
---

<Congratz
  achievement="knowing your second optimizer"
  message="Adam"
  secondary="⚠ Just remember the best optimizer is the one that the one that can traverse the loss of your problem pretty well."
  compact
/>

<div class="text-gray-500 italic">
  <a href="https://towardsdatascience.com/adam-latest-trends-in-deep-learning-optimization-6be9a291375c"
  >
    Just because it's fast doesn't mean it won't have problems.
  </a>
</div>

<div class="mt-16 font-bold">And the code...</div>

```py
model.compile(
    optimizer = tf.optimizers.Adam(),
    # others to follow...
)
```

<style>
  .shiki-container {
    text-align: left;
    width: 50%;
    margin-left: auto;
    margin-right: auto;
  }
</style>
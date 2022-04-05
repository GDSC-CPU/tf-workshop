---
layout: two-cols
---

# <logos-jupyter /> Jupyter Notebooks

* Capture results as the part of the notebook.
  <img alt="results" src="/images/results.png" style="width: 400px; height: 300px">

* Re-run only a small portion of your code
* Share your work with a peer

::right::

## Watch out when recycling variables

- Jupyter _"keeps track"_ of variables

```py
# Code Cell 1
x = 5
x
```

```sh
# Output cell 1
5
```

```py
# Code Cell 2
x ** 2 + 1 
```

```sh
# Output cell 2
26
```

```py
# Code Cell 3
x *= 4
```

- `x` is now `20`
- Rerunning _Code Cell 2_ would produce 401
  - even if it looks like it should be 26
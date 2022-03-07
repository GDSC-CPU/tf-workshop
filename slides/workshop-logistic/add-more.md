---
layout: two-cols
---

# We can't use linear regression

- Now we add more training data, a tumor size of **23!!**

<img alt="orig tumor" src="/images/tumor.jpg" style="width: 500px; height: 350px" />

::right::

# &nbsp;for classification?
  
  | Tumor Size |  $y$   | $y >= 0.5?$  | Prediction  |
  |------------|--------|--------------|-------------|
  | 1.1        | 0.36   | false        | benign      |
  | 3.4        | 0.46   | false        | benign      |
  | 4.0        | 0.48   | false        | **benign**  |
  | 4.3        | 0.49   | false        | **benign**  |

- what's formerly classified as malignant is now benign!!

## <twemoji-person-gesturing-no /> Reason #1: additional training data will shift the _"best-fit"_ line
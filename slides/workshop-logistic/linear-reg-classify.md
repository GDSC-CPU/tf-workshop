---
layout: two-cols
---

# Can we use linear regression

- Say this is our data for tumor size vs. malignant/benign

<img alt="orig tumor" src="/images/orig-tumor.jpg" style="width: 500px; height: 350px" />

::right::

# -- for classification?

- line fits perfectly
  - predict `0 (benign)` if $y \lt 0.5$
  - predict `1 (benign)` if $y \ge 0.5$
  
  | Tumor Size |  $y$   | $y >= 0.5?$  | Prediction  |
  |------------|--------|--------------|-------------|
  | 1.1        | 0.04   | false        | benign      |
  | 3.4        | 0.48   | false        | benign      |
  | 4.0        | 0.60   | true         | malignant   |
  | 4.3        | 0.65   | true         | malignant   |

<style>
  table {
    margin-top: 12px;
    border-top: 1px solid lightgray;
  }
</style>
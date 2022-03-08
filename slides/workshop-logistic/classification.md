---
layout: two-cols
---

# Classification

* Examples:
  - Email: **spam** or **not spam**
    * label $y = 1$ if spam, $y = 0$ if not spam
  - Transaction: **fraudulent** or **not fraudulent**
    * label $y = 1$ if fraudulent, $y = 0$ if not 
  - Tumor: **malignant** or **benign** (not malignant)
    * label $y = 1$ if malignant, $y = 0$ if benign

* Basically:
  - $y = 1$ if data belongs to _"positive class"_ 
    * e.g. malignant, `<something>`
  - $y = 0$ if data belongs to _"negative class"_ 
    * e.g. NOT malignant, `NOT <something>`

::right::

<img alt="classifier" src="/images/classifier.png" />

- <twemoji-woozy-face /><twemoji-face-with-crossed-out-eyes /> Don't be confused:
  * While _"fraudulent"_, _"spam"_, and _"malignant"_ are NEGATIVE words in
    everyday use, in ML they belong to the ***positive class*** because their
    label is $1$.
  * If we label _benign_ with $1$ instead, and _malignant_ $0$,
    - then `benign` belongs to the _positive class_
    - `NOT benign` belongs to the _negative class_
      + 👆 _"malignant"_

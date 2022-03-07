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

- GMail actually learns from people marking email as _"Spam"_ or _"Not spam"_
  * don't be surprised if you're a Christian, but emails from Bible Gateway
    end up in your Spam folder.
  * or emails from your bank end up in spam
  * legit emails end up in spam coz others _"hate"_ them, and mark them as such

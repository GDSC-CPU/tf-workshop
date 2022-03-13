---
layout: two-cols
---

# Your turn: Fashion MNIST

MNIST w/ a twist: grayscale images of fashion items

```py
mnist = keras.datasets.fashion_mnist
```

- also 60k training images, 10k test images, also $28 \times 28$
- data is still labeled from 0-9 (matrices + strings = 💥)
- <twemoji-pencil /> code to convert 0-9 labels into string labels

| Label | Description |
|-------|-------------|
| 0     | T-shirt/top |
| 1     | Trouser     |
| 2     | Pullover    |
| 3     | Dress       |
| 4     | Coat        |
| 5     | Sandal      |
| 6     | Shirt       |
| 7     | Sneaker     |
| 8     | Bag         |
| 9     | Ankle boot  |

::right::

<img alt="fashion" src="/images/fashion.jpg" style="height: 480px" />

<Countdown class="absolute right-35 bottom-20 text-orange-600" style="font-size: 2em;" />

<style>
  table {
    margin-top: 8px;
  }

  td:first-child, th:first-child {
    width: 20%;
  }

  th {
    font-weight: 700 !important;
    text-transform: uppercase;  
  }
    
  td, th {
    padding: 2px !important;
  }
</style>
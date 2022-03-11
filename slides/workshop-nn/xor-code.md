---
layout: two-cols
---

## XOR using <mdi-summation /> and <mdi-function />...really?

```py
def sigmoid(x): return 1 / (1 + e ** (-x))

def xor(X):
    w_or = np.array([[-10, 20, 20]]).T
    w_nand = np.array([[30, -20, -20]]).T
    w_and = np.array([[-30, 20, 20]]).T
    
    # add bias
    X = np.insert(X, 0, np.ones(len(X)), axis=1)
    return sigmoid(
        np.hstack((
            np.ones([len(X), 1]), # add bias
            sigmoid(X @ w_or), 
            sigmoid(X @ w_nand)
        )) @ w_and
    )

truth_table = np.array([
  [0, 0],
  [0, 1],
  [1, 0],
  [1, 1]
])
np.round(xor(truth_table), 3)
```

::right::

### *Yup!* <twemoji-beaming-face-with-smiling-eyes />

```
array([[0.],
       [1.],
       [1.],
       [0.]])
```

<p class="font-xs italic absolute bottom-42 right-8 opacity-50">
  In Python, `^` means <i>XOR</i><br />
  In Discrete Math `^` means <i>"AND"</i>
</p>

<img alt="drake meme" src="https://i.imgflip.com/683t5p.jpg" style="height: 350px" />
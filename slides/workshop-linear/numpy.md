---
layout: two-cols
---

# <logos-numpy /> Some NumPy Operations

##### Convert Python lists to Numpy arrays

```py
matrix = np.array([
    [i, i * 3, i ** 2] for i in range(1, 8 + 1)
])
```

```sh
array([[ 1,  3,  1],    # 0
       [ 2,  6,  4],    # 1
       [ 3,  9,  9],    # 2
       [ 4, 12, 16],    # 3
       [ 5, 15, 25],    # 4
       [ 6, 18, 36],    # 5
       [ 7, 21, 49],    # 6
       [ 8, 24, 64]])   # 7
```

##### **Slicing**: get the first  rows

```py
matrix[0:3]
```

```
array([[1, 3, 1],
       [2, 6, 4],
       [3, 9, 9]])
```

::right::


##### **Slicing**: get all rows, but only the first two columns

```py
matrix[:, 0:2]
```

```
array([[ 1,  3],
       [ 2,  6],
       [ 3,  9],
       [ 4, 12],
       [ 5, 15],
       [ 6, 18],
       [ 7, 21],
       [ 8, 24]])
```

##### **Slicing**: get the last column, first 5 rows

```py
# note the extra [square brackets]
matrix[0:5, [-1]]

# positive index also works, but sometimes harder
matrix[0:5, [2]]
```

```
array([[ 1],
       [ 4],
       [ 9],
       [16],
       [25]])
```
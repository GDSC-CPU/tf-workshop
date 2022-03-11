# [Train-test Split][1]

- What we did in the Admissions Classifier workshop is just measuring the accuracy
  of our training
  * we tested our model against **data it has already seen**
  * TensorFlow also gives us this via the [***accuracy*** metric][2]
    <small>and I let you do this the ha
    rd way?? <twemoji-smiling-face-with-horns /><twemoji-smiling-face-with-horns /></small>
  ```py
  model.compile(optimizer=sgd, loss=bce, metrics=['accuracy'])
  ```
- How well will our ML model predict the correct labels of **data it has never seen during training?**

<div class="flex">
  <img alt="split" src="/images/test-train-split.png" style="height: 110px" />

  <p class="pl-8">
    There's no optimal ratio, and it depends on your project.  For guidance, you can start with
    `80:20`, or `90:10`.  MNIST dataset is already split, and uses a 6:1 ratio (60,000 for <b><i>training</i></b>, 10,000 for <b><i>testing</i></b>).
  </p>
</div>

- Try this on your notebook. <twemoji-warning /><twemoji-construction /> *Tuple-ception ahead*

```py
#     X_train   ,     y_train           X_test  ,    y_test
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()
training_images.shape, test_images.shape
# Output cell should show: ((60000, 28, 28), (10000, 28, 28))
```

[1]: https://machinelearningmastery.com/train-test-split-for-evaluating-machine-learning-algorithms/
[2]: https://www.tensorflow.org/api_docs/python/tf/keras/metrics/Accuracy

<style>
  small {
    margin-left: 16px;
    color: green;
    font-style: italic;
  }
</style>
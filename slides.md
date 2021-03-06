---
# try also 'default' to start simple
dowmload: 'https://psse-cpu.github.io/ml-workshop/slides-export.pdf'
theme: seriph
fonts:
  sans: 'Crimson Pro'
  serif: 'Crimson Pro'
  mono: 'Fira Code'
  italic: true
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://cdn.pixabay.com/photo/2018/06/27/12/55/artificial-neural-network-3501528__340.png
# apply any windi css classes to the current slide
class: 'text-center'
# https://sli.dev/custom/highlighters.html
highlighter: shiki
# show line numbers in code blocks
lineNumbers: true
# some information about the slides, markdown enabled
info: |
  Slides for ML Workshop.

  Learn more at [Sli.dev](https://sli.dev)
# persist drawings in exports and build
drawings:
  persist: false
---

<div class="gridlines bg-gray-800/85 rounded-3xl p-8">
  <h3>#machineIsStillLearning</h3>
  <h1><logos-openai-icon /> Machine Learning Workshop</h1>
  <h4>
    <img alt="cpu" src="/images/cpu-logo.png" />
    <img alt="gdsc" src="/images/cpu-gdsc.png" />
  </h4>

  <CoverDetails />
</div>

<style>
  .gridlines {
    background-size: 40px 40px;
    background-image:
      linear-gradient(to right, teal 1px, transparent 1px),
      linear-gradient(to bottom, teal 1px, transparent 1px);
  }

  h4 {
    display: inline;
  }

  h3 {
    color: skyblue;
    font-weight: 700;
  }

  h4 img {
    display: inline;
    height: 64px;
  }
</style>

---
src: ./slides/intro/impossible.md
---
---
src: ./slides/intro/cover-2.md
---
---
layout: image
image: /images/eat.png
---
---
layout: image
image: /images/ai-startup.png
---
---
src: ./slides/intro/outline.md
---
---
src: ./slides/intro/assumptions.md
---


---
src: ./slides/theory/ml.md
---
---
src: ./slides/theory/arthur-samuel.md
---
---
src: ./slides/theory/tom-mitchell.md
---
---
src: ./slides/theory/regression-classification-1.md
---
---
src: ./slides/theory/regression-classification-2.md
---
---
src: ./slides/theory/spam.md
---
---
src: ./slides/theory/binary-multi.md
---
---
src: ./slides/theory/one-vs-rest.md
---
---
src: ./slides/theory/neurons.md
---
---
src: ./slides/theory/ann-1hidden.md
---
---
src: ./slides/theory/ann-2hidden.md
---

---
src: ./slides/tools/jupyter.md
---
---
src: ./slides/tools/jupyter-2.md
---
---
src: ./slides/tools/jupyter-3.md
---
---
src: ./slides/tools/crowdflower.md
---
---
src: ./slides/tools/data-cleaning.md
---
---
src: ./slides/tools/jupyter-how.md
---

---
src: ./slides/workshop-linear/hello.md
---
--- 
src: ./slides/workshop-linear/vectorization-2.md
---
---
src: ./slides/workshop-linear/lots.md
---
---
src: ./slides/workshop-linear/vectorized-bench-2.md
---
---
src: ./slides/workshop-linear/vectorized-bench-1.md
---
---
src: ./slides/workshop-linear/fast.md
---
---
src: ./slides/workshop-linear/feasible.md
---
---
src: ./slides/workshop-linear/fun-fact.md
---
---
src: ./slides/workshop-linear/numpy.md
---
---
src: ./slides/tools/tensorflow.md
---
---
src: ./slides/workshop-linear/recall.md
---
---
src: ./slides/workshop-linear/hello-tf.md
---
---
src: ./slides/workshop-linear/model-dense.md
---
---
src: ./slides/workshop-linear/recall.md
---
---
src: ./slides/workshop-linear/power-neuron.md
---
---
src: ./slides/workshop-linear/power-neuron-2.md
---
---
src: ./slides/workshop-linear/bias.md
---
---
src: ./slides/workshop-linear/bias-2.md
---
---
src: ./slides/workshop-linear/y-mx-plus-b.md
---
---
src: ./slides/workshop-linear/idea.md
---
---
src: ./slides/workshop-linear/guess-lines.md
---
---
src: ./slides/workshop-linear/guess-lines-2.md
---
---
src: ./slides/workshop-linear/loss.md
---
---
src: ./slides/workshop-linear/mse.md
---
---
src: ./slides/workshop-linear/vectorization-1.md
---
---
src: ./slides/workshop-linear/vectorized-demo.md
---
---
src: ./slides/workshop-linear/code-excited.md
---
---
src: ./slides/workshop-linear/remember-mse.md
---
---
src: ./slides/workshop-linear/optimizer.md
---
---
src: ./slides/workshop-linear/cost-function-plot.md
---
---
src: ./slides/workshop-linear/cost-function-plot-2.md
---
---
src: ./slides/workshop-linear/gradient-descent-1.md
---
---
src: ./slides/workshop-linear/gradient-descent-2.md
---
---
src: ./slides/workshop-linear/gradient-descent-3.md
---
---
src: ./slides/workshop-linear/hyperparams.md
---
---
src: ./slides/workshop-linear/sgd.md
---
---
src: ./slides/workshop-linear/sgd-2.md
---
---
src: ./slides/workshop-linear/remember-sgd.md
---
---
src: ./slides/workshop-linear/univariate-workshop.md
---
---
src: ./slides/workshop-linear/congrats-linear.md
---
---
src: ./slides/workshop-linear/multivariate.md
---
---
src: ./slides/workshop-linear/feature-scaling.md
---
---
src: ./slides/workshop-linear/feature-scaling-2.md
---
---
src: ./slides/workshop-linear/feature-scaling-code.md
---
---
src: ./slides/workshop-linear/multivariate-workshop.md
---
---
src: ./slides/workshop-linear/congrats-linear-2.md
---

---
src: ./slides/workshop-logistic/classification.md
---
---
src: ./slides/workshop-logistic/linear-reg-classify.md
---
---
src: ./slides/workshop-logistic/add-more.md
---
---
src: ./slides/workshop-logistic/unbounded.md
---
---
src: ./slides/workshop-logistic/superpower.md
---
---
src: ./slides/workshop-logistic/superpower-2.md
---
---
src: ./slides/workshop-logistic/linear-non-linear.md
---
---
src: ./slides/workshop-logistic/circular.md
---
---
src: ./slides/workshop-logistic/sigmoid.md
---
---
src: ./slides/workshop-logistic/sigmoid-meme.md
---
---
src: ./slides/workshop-logistic/congrats-sigmoid.md
---
---
src: ./slides/workshop-logistic/loss.md
---
---
src: ./slides/workshop-logistic/cross-entropy.md
---
---
src: ./slides/workshop-logistic/congrats-bce.md
---
---
src: ./slides/workshop-logistic/classifier.md
---
---
src: ./slides/workshop-logistic/classifier-workshop.md
---
---
src: ./slides/workshop-logistic/notebook-meme.md
---
---
src: ./slides/workshop-logistic/loading-saving.md
---
---
src: ./slides/workshop-logistic/will-smith.md
---
---
src: ./slides/workshop-logistic/tflite.md
---
---
src: ./slides/workshop-logistic/tflite-2.md
---
---
src: ./slides/workshop-logistic/tflite-3.md
---
---
src: ./slides/workshop-logistic/tflite-4.md
---
---
src: ./slides/workshop-logistic/load-save-workshop.md
---

---
src: ./slides/workshop-nn/day2.md
---
---
src: ./slides/workshop-linear/recall.md
---
---
src: ./slides/theory/ann-1hidden.md
---
---
src: ./slides/theory/ann-2hidden.md
---
---
src: ./slides/workshop-logistic/linear-non-linear.md
---
---
src: ./slides/workshop-logistic/circular.md
---
---
src: ./slides/workshop-nn/universal-approx.md
---
---
src: ./slides/workshop-nn/intuition.md
---
---
src: ./slides/workshop-nn/intuition-2.md
---
---
src: ./slides/workshop-nn/xor.md
---
---
src: ./slides/workshop-nn/xor-code.md
---
---
src: ./slides/workshop-nn/intuition-3.md
---
---
src: ./slides/workshop-nn/intuition-4.md
---
---
src: ./slides/workshop-nn/nn-workshop.md
---
---
src: ./slides/workshop-nn/x1000.md
---
---
src: ./slides/workshop-nn/papers-1.md
---
---
src: ./slides/workshop-nn/papers-2.md
---
---
src: ./slides/workshop-nn/papers-3.md
---
---
src: ./slides/workshop-nn/mnist.md
---
---
src: ./slides/workshop-nn/test-train-split.md
---
---
src: ./slides/workshop-nn/congrats-train-test.md
---
---
src: ./slides/workshop-nn/mnist-grid.md
---
---
src: ./slides/workshop-nn/mnist-single.md
---
---
src: ./slides/workshop-nn/mnist-nn.md
---
---
src: ./slides/workshop-nn/congrats-flatten.md
---
---
src: ./slides/workshop-nn/multiclass.md
---
---
src: ./slides/workshop-nn/softmax.md
---
---
src: ./slides/workshop-nn/congrats-softmax.md
---
---
src: ./slides/workshop-nn/cce-scce.md
---
---
src: ./slides/workshop-nn/cce-scce-2.md
---
---
src: ./slides/workshop-nn/congrats-scce.md
---
---
src: ./slides/workshop-nn/mnist-nn-clear.md
---
---
src: ./slides/workshop-nn/callbacks.md
---
---
src: ./slides/workshop-nn/did-you-get.md
---
---
src: ./slides/workshop-nn/callbacks.md
---
---
src: ./slides/workshop-nn/congrats-nn.md
---
---
src: ./slides/workshop-nn/adam.md
---
---
src: ./slides/workshop-nn/adam-quote.md
---
---
src: ./slides/workshop-nn/optimizers-many.md
---
---
src: ./slides/workshop-nn/congrats-adam.md
---
---
src: ./slides/workshop-nn/fashion-mnist.md
---
---
src: ./slides/workshop-nn/experiments.md
---
---
src: ./slides/workshop-nn/backprop.md
---
---
src: ./slides/workshop-nn/vanishing.md
---
---
src: ./slides/workshop-nn/vanishing-2.md
---
---
src: ./slides/workshop-nn/relu.md
---
---
src: ./slides/workshop-nn/congrats-relu.md
---

---
src: ./slides/workshop-cnn/cnn.md
---
---
src: ./slides/workshop-cnn/filters.md
---
---
src: ./slides/workshop-cnn/cnn-2.md
---
---
src: ./slides/workshop-cnn/cnn-4.md
---
---
src: ./slides/workshop-cnn/cnn-5.md
---
---
src: ./slides/workshop-cnn/cnn-demo.md
---
---
src: ./slides/workshop-cnn/cnn-colored.md
---
---
src: ./slides/workshop-cnn/pooling.md
---
---
src: ./slides/workshop-cnn/arrangement-2.md
---
---
src: ./slides/workshop-cnn/arrangement.md
---
---
src: ./slides/workshop-cnn/conv-pool-exp.md
---
---
src: ./slides/workshop-cnn/cnn-fmnist-workshop.md
---
---
src: ./slides/workshop-cnn/congrats-cnn.md
---
---
src: ./slides/workshop-cnn/graduation.md
---
---
src: ./slides/workshop-cnn/own-images.md
---
---
src: ./slides/workshop-cnn/own-images-2.md
---
---
src: ./slides/workshop-cnn/own-images-3.md
---
---
src: ./slides/workshop-cnn/own-images-4.md
---
---
src: ./slides/workshop-cnn/own-images-5.md
---
---
src: ./slides/workshop-cnn/own-images-6.md
---
---
src: ./slides/workshop-cnn/own-images-7.md
---
---
src: ./slides/workshop-cnn/final-advice.md
---
---
src: ./slides/workshop-cnn/final-advice-2.md
---
---
src: ./slides/workshop-cnn/big.md
---
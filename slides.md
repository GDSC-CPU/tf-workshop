---
# try also 'default' to start simple
theme: seriph
fonts:
  sans: 'Tinos'
  serif: 'Tinos'
  mono: 'Space Mono'
  italic: true
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://cdn.pixabay.com/photo/2018/05/08/08/46/artificial-intelligence-3382509_960_720.png
# apply any windi css classes to the current slide
class: 'text-center'
# https://sli.dev/custom/highlighters.html
highlighter: shiki
# show line numbers in code blocks
lineNumbers: true
# some information about the slides, markdown enabled
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
# persist drawings in exports and build
drawings:
  persist: false
dowmload: true
---

# Machine Learning in 3 Hours

<b>ECE 4241</b> Seminars / Colloquium / Field Study

<div class="pt-12">
  <mdi-calendar /> March 14 & 15
  <mdi-clock /> 5:30-7:00
  <mdi-map-marker /> Virtual
</div>

<div class="abs-br m-6 flex rounded-4xl">
  <div class="bg-blue-800/40 p-2 text-gray-300 mr-0" style="border-radius: 4px 0px 0px 4px">
    Richard Michael Coo
  </div>
  <div class="italic text-indigo-200 bg-blue-300/40 p-2 ml-0" style="border-radius: 0px 16px 16px 0px">
    <logos-twitter /> <logos-github-icon /> <logos-gitlab /> @myknbani
  </div>
</div>

<p class="font-xs italic absolute bottom-2 left-0 opacity-30 transform -rotate-4">
  Slides work better in "Dark Mode", press <kbd class="not-italic">D</kbd> to toggle.
</p>

<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->

---
layout: image-right
image: images/impossible4.png
---
# Which is impossible

<p class="pt-24 text-3xl">It's a <b class="text-5xl">HUGE</b> field</p>

<h3 class="mt-24">so let's try...</h3>

---
layout: cover
background: https://cdn.pixabay.com/photo/2018/05/08/08/46/artificial-intelligence-3382509_960_720.png
---

## ~~Machine Learning in 3 Hours~~
# Neural Networks in 3 Hours

<b>ECE 4241</b> Seminars / Colloquium / Field Study

<div class="pt-12">
  <mdi-calendar /> March 14 & 15
  <mdi-clock /> 5:30-7:00
  <mdi-map-marker /> Virtual
</div>

<div class="abs-br m-6 flex rounded-4xl">
  <div class="bg-blue-800/40 p-2 text-gray-300 mr-0" style="border-radius: 4px 0px 0px 4px">
    Richard Michael Coo
  </div>
  <div class="italic text-indigo-200 bg-blue-300/40 p-2 ml-0" style="border-radius: 0px 16px 16px 0px">
    <logos-twitter /> <logos-github-icon /> <logos-gitlab /> @myknbani
  </div>
</div>

<p class="font-xs italic absolute bottom-2 left-0 opacity-30 transform -rotate-4">
  Slides work better in "Dark Mode", press <kbd class="not-italic">D</kbd> to toggle.
</p>
<!--
The last comment block of each slide will be treated as slide notes. It will be visible and editable in Presenter Mode along with the slide. [Read more in the docs](https://sli.dev/guide/syntax.html#notes)
-->

---
layout: two-cols
---

# Day 1
- Theory
  * machine learning
  * neural networks
  * regression vs classification
- Tools Familiarization
  * <logos-jupyter /> Jupyter Notebook
  * <logos-tensorflow /> Tensorflow
- Workshop
  * linear regression
  * logistic regression
  * intuition on approximating functions
  * vanilla neural networks
  * experiments
- Video (ALVINN)

::right::

# Day 2
- More intense 💪 workshops
  * convolutional neural networks (CNN)
  * convolutional layers
  * pooling layers
  * training with your own images
- Final advice
- Video: Cassava Plant Disease Detection
- Closing

---
layout: two-cols
---

# Assumptions

You can code in any language, preferably

<logos-python style="width: 128px; height: 128px" />

- variables
- control structures
   * if-statements
   * loops
- OOP
  * basics of classes and objects
  * operator overloading is a ➕

::right::

<div class="mt-12 text-gray-500">
  You are not allergic to
</div>

![math](/images/math.png)


---
layout: two-cols
---

# Machine Learning

```mermaid {theme: 'dark', scale: 1.2}
graph LR
R[Rules] --> T((Traditional<br>Programming))
D[Data]  --> T

T --> A[Answers]
```

A new paradigm

```mermaid {theme: 'dark', scale: 1.1}
graph LR
A[Answers] --> M((Machine Learning))
D[Data]  --> M
M --> R[Rules]
```

::right::

- 💎 HARD 😱: code some complicated logic that tells apart a dog or a cat in a picture
- ✌ _"EASY"_ ✌: give **tons** of examples of dogs and cats, and have the machine discover patterns
  ![dog-cat](/images/dog-cat.jpg)

---
layout: center
---

# Artificial Neural Networks

<img alt="neuron" src="/images/neuron.png"  />


---
layout: center
---

![ann-1hidden](/images/ann-1hidden.png)


---
layout: center
---

![ann-1hidden](/images/ann-2hidden.png)


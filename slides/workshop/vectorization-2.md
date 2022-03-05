---
layout: two-cols
---

# Matrix libs are  multithreaded

<img alt="matrix-multiply2" src="/images/matrix-multiply.jpg" />

- Matrices of numerical libraries like NumPy can take advantage of multiple CPU cores
- Libraries like TensorFlow [can also use the GPU](https://www.tensorflow.org/install/gpu)
  + **GPUs** have **more** cores
  + <img src="/images/nvidia.png" style="width: 20px; height: 20px; display: inline " />
    on <logos-microsoft-windows /> and <logos-tux />, 
    <a href="https://www.amd.com/en/technologies/infinity-hub/tensorflow">
      <img src="/images/radeon.png" style="width: 20px; height: 20px; display: inline " /> on
      <logos-tux /> only
    </a>
- on the images, differently-colored operations can be done in parallel

::right::

# 🏃🐎🏇🐇🚀

<img alt="matrix-multiply" src="/images/matrices.jpg" />

---
layout: two-cols
---

# [<logos-google /> Colab](https://colab.research.google.com/)

Google "Colaboratory"

- <mdi-cloud class="text-blue-400" /> cloud-based, zero configuration required
  * you don't need a Python environment installed
- <img src="/images/nvidia.png" style="width: 20px; height: 20px; display: inline " /> Free access to GPUs
  * faster, and more VRAM than [budget gaming laptops][1]
  * [GTX 1080 is only around 15% faster on average][3]
- <mdi-share class="text-orange-400" /> Easy sharing
- <logos-google-drive /> Google Drive integration
- <logos-python /> Only supports Python
  > [Colab focuses on supporting Python and its ecosystem of third-party tools. We're aware that users are interested in support for other Jupyter kernels (eg R or Scala). We would like to support these, but don't yet have any ETA.][2]


[1]: https://towardsdatascience.com/google-colab-how-does-it-compare-to-a-gpu-enabled-laptop-851c1e0a2ca9
[2]: https://research.google.com/colaboratory/faq.html
[3]: https://towardsdatascience.com/deep-learning-on-a-budget-450-egpu-vs-google-colab-494f9a2ff0db

::right::

# <logos-visual-studio-code /> [VSCode](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

- <mdi-wifi-off class="text-red-500" /> can work offline if your net sucks
- <mdi-download class="text-green-500" /> need to download, install Python and friends
- 💰 need to use your own hardware
- <span class="bg-blue-100/50 p-1 rounded-3xl">
    <logos-scala /> <logos-julia /> <logos-r-lang /> <logos-javascript />
  </span> can use any language

<mdi-heart class="text-yellow-500" /> Colab GPUs, but also <mdi-heart class="text-blue-600" /> your own VSCode setup?
<a 
  href="https://colab.research.google.com/github/JayThibs/jacques-blog/blob/master/_notebooks/2021-09-27-connect-to-colab-from-local-vscode.ipynb">
  <img alt="both" src="/images/why-not-both.gif" />
</a>
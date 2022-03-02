<style scoped>
  .socials {
    border-bottom: 0px;
    margin-right: 4px;
  }
</style>

<template>
<div class="pt-12">
  <mdi-calendar /> March 14 & 15
  <mdi-clock /> 5:30-7:00
  <mdi-map-marker /> Virtual
</div>
<div class="mt-2 text-gray-400">
  <span class="bg-gray-800/50 p-2 rounded-3xl">
    <mdi-github-face />
    <a href="https://github.com/psse-cpu/ml-workshop/">Git repo</a>
    <mdi-file-pdf class="ml-4" /> 
    <a href="https://psse-cpu.github.io/ml-workshop/slides-export.pdf">PDF version</a>
  </span>
</div>

<div class="abs-br m-6 flex rounded-4xl">
  <div class="bg-blue-800/40 p-2 text-gray-300 mr-0" style="border-radius: 4px 0px 0px 4px">
    Richard Michael Coo
  </div>
  <div class="italic text-indigo-200 bg-blue-300/40 p-2 ml-0" style="border-radius: 0px 16px 16px 0px">
    <a href="https://twitter.com/myknbani" class="socials">
      <logos-twitter />
    </a>
    <a href="https://github.com/myknbani" class="socials">
      <logos-github-icon />
    </a>
    <a href="https://gitlab.com/myknbani" class="socials">
      <logos-gitlab />
    </a>

    @myknbani
  </div>
</div>

<p class="font-xs italic absolute bottom-2 left-0 opacity-30 transform -rotate-4">
  Slides work better in "Dark Mode", press <kbd class="not-italic">D</kbd> to toggle.
</p>
</template>
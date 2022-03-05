<script setup lang="ts">
  const props = defineProps({
    achievement: {
      default: ''
    },
    message: {
      default: ''
    },
    secondary: {
      default: ''
    },
    caveat: {
      default: ''
    }
  })
</script>

<template>
  <h2>
    <twemoji-party-popper class="animate-ping" />
    <twemoji-partying-face class="animate-bounce" /> 
    Congratulations on {{ achievement }}!
  </h2>

  <h1>{{ message }}</h1>

  <h2>{{ secondary }}</h2>

  <div class="text-gray-400 italic mt-16 text-xl">
    {{ caveat }}
  </div>
</template>
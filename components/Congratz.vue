<script setup lang="ts">
  import { ref } from 'vue'

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
    },
    compact: {
      default: false,
    }
  })


  const marginClass = ref(props.compact ? 'mt-4' : 'mt-16')
</script>

<template>
  <h2>
    <twemoji-party-popper class="animate-ping" />
    <twemoji-partying-face class="animate-bounce" /> 
    Congratulations on {{ achievement }}!
  </h2>

  <h1>{{ message }}</h1>

  <h2>{{ secondary }}</h2>

  <div class="text-gray-400 italic mt-16 text-xl" :class="[marginClass]">
    {{ caveat }}
  </div>
</template>
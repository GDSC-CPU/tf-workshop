<script setup lang="ts">
import { ref, computed, onBeforeUnmount } from 'vue'

const totalSeconds = ref(0)
const minutes = computed(() => Math.trunc(totalSeconds.value / 60))
const seconds = computed(() => totalSeconds.value % 60)
const started = ref(false)

let timer

onBeforeUnmount(() => {
  if (timer) clearInterval(timer)
})

const setInitialTime = (seconds: number) => {
  totalSeconds.value = seconds

  timer = setInterval(() => {
    totalSeconds.value--
  }, 1000)

  started.value = true
}
</script>

<template>
  <div class="timer">
    <div style="width: 100%; font-size: 0.9em;" v-if="!started">
      <twemoji-man-running /><twemoji-woman-running /> Ready...
    </div>
    <div style="width: 100%" v-else-if="totalSeconds > 0">
      <span class="hour">{{ String(minutes).padStart(2, '0') }}</span>
      <span class="colon">:</span>
      <span class="minute">{{ String(seconds).padStart(2, '0' ) }}</span>
    </div>
    <div style="width: 100%; font-size: 0.9em;" v-else>
      ⌛ Time's up!
    </div>
    <div class="timer-buttons">
      <button :disabled="started" @click.prevent="setInitialTime(120)">02:00</button>
      <button :disabled="started" @click.prevent="setInitialTime(300)">05:00</button>
      <button :disabled="started" @click.prevent="setInitialTime(600)">10:00</button>
      <button :disabled="started" @click.prevent="setInitialTime(900)">15:00</button>
    </div>
  </div>
</template>

<style scoped>
  .timer {
    font-family: 'Fira Code', monospace;
    display: flex;
    width: 100%;
    padding: 0px 8px 8px;
    text-align: center !important;
    align-items: center;
    justify-items: center;
    font-size: 3em;
    flex-direction: column;
  }

  .timer-buttons button {
    font-size: 0.3em;
    padding: 4px;
    border: 1px solid goldenrod;
    border-radius: 16px;
    margin: 16px;
  }

  .timer-buttons button:hover {
    background-color: gold;
  }

  .timer-buttons button:disabled {
    background-color: gray;
    border: 1px splid darkgray !important;
    color: darkgray;
    cursor: not-allowed;
  }

  .colon {
    color: goldenrod;
  }

  .timer > span {
    color: darkorange;
  }
</style>
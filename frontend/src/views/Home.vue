<script setup lang="ts">
import { onMounted } from "vue";
import { useWaveform } from "../composables/useWaveform";
import WaveformChart from "./WaveformChart.vue";

const { waveform, loadWaveform } = useWaveform();

onMounted(() => {
  loadWaveform("IU", "ANMO", "BHZ", "2020-01-01T00:00:00", 30);
});
</script>

<template>
  <h1>Waveform Chart</h1>

  <WaveformChart
    v-if="waveform"
    :data="waveform.data"
    :sampleRate="waveform.sampling_rate"
  />
</template>

<script setup lang="ts">
import { ref, watch, onMounted, onBeforeUnmount } from "vue";
import {
  Chart,
  LineController,
  LineElement,
  PointElement,
  LinearScale,
  Title,
  Tooltip,
} from "chart.js";

Chart.register(
  LineController,
  LineElement,
  PointElement,
  LinearScale,
  Title,
  Tooltip,
);

interface Props {
  data: number[];
  sampleRate: number;
}

const props = defineProps<Props>();

const canvasRef = ref<HTMLCanvasElement | null>(null);
let chart: Chart | null = null;

function createChart() {
  if (!canvasRef.value) return;

  const ctx = canvasRef.value.getContext("2d");
  if (!ctx) return;

  const data = props.data.map((value, index) => ({
    x: index / props.sampleRate,
    y: value,
  }));

  chart = new Chart(ctx, {
    type: "line",
    data: {
      datasets: [
        {
          label: "Waveform",
          data: data,
          borderColor: "rgba(75, 192, 192, 1)",
          pointRadius: 0,
        },
      ],
    },
    options: {
      responsive: true,
      scales: {
        x: {
          type: "linear",
          title: {
            display: true,
            text: "Time (s)",
          },
        },
        y: {
          title: {
            display: true,
            text: "Amplitude",
          },
        },
      },
    },
  });
}

// onMounted(() => {
//   console.log("Creating chart with data:", props.data);
//   console.log("canvasRef:", canvasRef.value);
//   createChart();
// });

watch(
  () => props.data,
  (data) => {
    if (!data || data.length === 0) return;
    if (chart) {
      chart.destroy();
      chart = null;
    }
    createChart();
  },
  { immediate: true },
);

onBeforeUnmount(() => {
  if (chart) {
    chart.destroy();
  }
});
</script>

<template>
  <div class="waveform-chart">
    <canvas ref="canvasRef"></canvas>
  </div>
</template>

<style scoped>
.waveform-chart {
  width: 100%;
  height: 400px;
}
.waveform-chart canvas {
  width: 100% !important;
  height: 100% !important;
}
</style>

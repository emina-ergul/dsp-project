<script setup lang="ts">
import { ref, onMounted, onBeforeUnmount } from "vue";
import {
  Chart,
  LineController,
  LineElement,
  PointElement,
  LinearScale,
  Title,
  Tooltip,
} from "chart.js";

interface Props {
  samples: number[];
  samplingRate: number;
}

const props = defineProps<Props>();

const canvasRef = ref<HTMLCanvasElement | null>(null);
let chart: Chart | null = null;

function createChart() {
  if (!canvasRef.value) return;

  const ctx = canvasRef.value.getContext("2d");
  if (!ctx) return;

  chart = new Chart(ctx, {
    type: "line",
    data: {
      datasets: [
        {
          label: "Waveform",
          data: props.samples,
          borderColor: "rgba(75, 192, 192, 1)",
          pointRadius: 0,
        },
      ],
    },
  });
}

onMounted(createChart);

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

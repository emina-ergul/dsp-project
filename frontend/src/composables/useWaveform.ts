import { ref } from "vue";
import { fetchWaveform } from "../services/api";
import type { Waveform } from "../types";

export function useWaveform() {
  const waveform = ref<Waveform | null>(null);
  const loading = ref(false);
  const error = ref<string | null>(null);

  const loadWaveform = async (
    network: string,
    station: string,
    channel: string,
    start_time: string,
    duration: number,
  ) => {
    loading.value = true;

    try {
      waveform.value = await fetchWaveform(
        network,
        station,
        channel,
        start_time,
        duration,
      );
    } catch (err: any) {
      error.value = err.message;
    } finally {
      loading.value = false;
    }
  };
  return { waveform, loading, error, loadWaveform };
}

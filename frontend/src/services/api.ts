import type { Waveform } from "../types";

const backend_url = "http://127.0.0.1:8000";

export async function fetchWaveform(
  network: string,
  station: string,
  channel: string,
  start_time: string,
  duration: number,
): Promise<Waveform> {
  const url = `${backend_url}/get-iris-data?network=${network}&station=${station}&channel=${channel}&start_time=${start_time}&duration=${duration}`;

  const res = await fetch(url);
  if (!res.ok) {
    throw new Error(`Error fetching Iris waveform data: ${res.statusText}`);
  }

  return res.json();
}

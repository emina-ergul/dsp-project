import type { Waveform } from "../types";

const backend_url = "http://localhost:8000";

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
  console.log(res.json());
  return res.json();
}

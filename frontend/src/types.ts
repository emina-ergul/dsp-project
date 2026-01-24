export interface Waveform {
  network: string;
  station: string;
  channel: string;
  start_time: string;
  sampling_rate: number;
  data: number[];
}

from pydantic import BaseModel
from typing import List


class Waveform(BaseModel):
    network: str
    station: str
    channel: str
    startTime: str
    data: List[float]
    samplingRate: float

from fastapi import APIRouter, HTTPException
from app.models import Waveform

from services.iris import get_waveform

router = APIRouter()


class FetchWaveformError(Exception):
    pass


@router.get("/get-iris-data", response_model=Waveform, status_code=200)
def get_waveform_endpoint(
    network: str = "IU",
    station: str = "ANMO",
    location: str = "00",
    channel: str = "BHZ",
    start_time: str = "2026-01-01T00:00:00",
    duration_seconds: int = 60,
):
    try:
        data = get_waveform(
            network=network,
            station=station,
            location=location,
            channel=channel,
            start_time=start_time,
            duration_seconds=duration_seconds,
        )
        return data
    except Exception as e:
        raise FetchWaveformError(f"Error fetching waveform data: {e}")

from fastapi import APIRouter
from app.models import Waveform

from services.iris import get_waveform

router = APIRouter()


@router.get("/get-iris-data", response_model=Waveform, status_code=200)
def get_waveform_endpoint():
    data = get_waveform(
        network="IU",
        station="ANMO",
        location="00",
        channel="BHZ",
        start_time="2026-01-01T00:00:00",
        end_time="2026-01-01T00:10:00",
    )
    return data

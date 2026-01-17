from obspy import UTCDateTime
from obspy.clients.fdsn import Client

from app.models import Waveform


client = Client("IRIS")


def get_waveform(
    network: str,
    station: str,
    location: str,
    channel: str,
    start_time: str,
    end_time: str,
) -> None:

    start = UTCDateTime(start_time)
    end = UTCDateTime(end_time)

    stream = client.get_waveforms(
        network=network,
        station=station,
        location=location,
        channel=channel,
        starttime=start,
        endtime=end,
    )

    print(len(stream))
    trace = stream[0]

    print(stream)
    print(type(trace.data))
    print(trace.data)
    print(trace.stats)

    return Waveform(
        network=network,
        station=station,
        channel=channel,
        startTime=trace.stats.starttime.isoformat(),
        data=trace.data,
        samplingRate=trace.stats.sampling_rate,
    )

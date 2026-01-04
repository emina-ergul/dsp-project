from obspy import UTCDateTime
from obspy.clients.fdsn import Client as FSDN_Client
import matplotlib.pyplot as plt

client = FSDN_Client("IRIS")

network = "IU"
station = "?"
location = "00"
channel = "BHZ"
start_time = UTCDateTime("2026-01-01T00:00:00")
end_time = UTCDateTime("2026-01-01T00:10:00")

st = client.get_waveforms(
    network=network,
    station=station,
    location=location,
    channel=channel,
    starttime=start_time,
    endtime=end_time,
)

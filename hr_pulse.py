"""
TODO: this code needs some fine tuning because it is not
reliably detecting my heart rate in a range even close
to what my fitbit says

Pulse sensor	CPX
Red (+)     	3.3V
Black (−)	    GND
Purple (signal)	A1
"""

import board
import analogio
import time

pulse = analogio.AnalogIn(board.A1)

THRESHOLD = 32900
HYSTERESIS = 200
MIN_BEAT_INTERVAL = 0.5

last_beat = None
above_threshold = False
intervals = []

while True:
    # Smooth the signal
    total = 0
    for i in range(5):
        total += pulse.value
        time.sleep(0.002)

    value = total / 5
    now = time.monotonic()

    # Detect rising threshold crossing
    if value > THRESHOLD and not above_threshold:
        above_threshold = True

        if last_beat is None:
            last_beat = now

        elif now - last_beat >= MIN_BEAT_INTERVAL:
            interval = now - last_beat
            last_beat = now

            if interval < 1.5:
                intervals.append(interval)

                if len(intervals) > 5:
                    intervals.pop(0)

                avg_interval = sum(intervals) / len(intervals)
                bpm = 60 / avg_interval

                print("BPM:", round(bpm))

    elif value < THRESHOLD - HYSTERESIS:
        above_threshold = False

    time.sleep(0.01)
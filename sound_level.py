"""
Open the serial monitor and try talking, clapping, or tapping near the microphone.
- Quiet room: Relatively low readings.
- Talking: Higher readings.
- Clapping: Brief spikes.
The values are relative sound amplitudes, not calibrated decibels, and there is no fixed 0–255 range.

If you get a MemoryError, try reducing the sample buffer from 160 to 80 samples.
"""
import time
import array
import math
import audiobusio
import board

# Set up the built-in microphone
mic = audiobusio.PDMIn(
    board.MICROPHONE_CLOCK,
    board.MICROPHONE_DATA,
    sample_rate=16000,
    bit_depth=16
)

# Buffer for 160 audio samples
samples = array.array("H", [0] * 160)

def sound_level():
    mic.record(samples, len(samples))

    # Calculate RMS amplitude
    mean = sum(samples) / len(samples)
    variance = sum((sample - mean) ** 2 for sample in samples) / len(samples)
    return math.sqrt(variance)

while True:
    level = sound_level()
    print("Sound level:", round(level))
    time.sleep(0.1)
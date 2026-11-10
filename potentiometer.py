"""
GS: untested

Potentiometer	CPX
Outer pin	    3.3V
Middle pin	    A1
Other outer     pin	GND

You should see values ranging from approximately 0 to 65535 as you rotate the knob.
"""
import board
import analogio
import time

pot = analogio.AnalogIn(board.A1)

while True:
    print("Potentiometer:", pot.value)
    time.sleep(0.2)
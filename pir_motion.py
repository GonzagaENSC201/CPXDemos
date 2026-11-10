"""
PIR sensor pin	CPX connection
VCC	            VOUT
OUT	            A6
GND	            GND

Important: The HC-SR501 typically needs approximately 5V to operate, 
so use VOUT, not the CPX's 3.3V pad, when the CPX is powered over USB. 
Its OUT signal is typically around 3.3V, which is compatible with CPX digital inputs.

Warm-up: Give the sensor 30–60 seconds after powering it on.

Detection: It detects movement of warm objects, not distance or precise position.

Sensitivity: One of the small potentiometers on the module adjusts detection distance.

Delay: The other potentiometer controls how long the output stays HIGH after motion.

Trigger mode: The H/L jumper selects repeatable versus single-trigger behavior.
"""

import board
import digitalio
import time

pir = digitalio.DigitalInOut(board.A1)
pir.direction = digitalio.Direction.INPUT

print("Warming up PIR sensor...")
time.sleep(60)

print("Ready!")

while True:
    if pir.value:
        print("Motion detected!")
    else:
        print("No motion")

    time.sleep(0.5)
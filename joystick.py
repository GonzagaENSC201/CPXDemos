"""
Joystick pin	CPX pad	    Purpose
GND	            GND	        Ground
+5V	            3.3V	    Power
VRx	            A2	        Horizontal movement
VRy	            A3	        Vertical movement
SW	            A1	        Joystick button
"""

import time
import board
import analogio
import digitalio

x = analogio.AnalogIn(board.A2)
y = analogio.AnalogIn(board.A3)

button = digitalio.DigitalInOut(board.A1)
button.switch_to_input(pull=digitalio.Pull.UP)

while True:
    print("X:", x.value,
          "Y:", y.value,
          "Button:", not button.value)

    time.sleep(0.2)
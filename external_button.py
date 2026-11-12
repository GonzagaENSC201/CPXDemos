# external button in breadboard turns on the built-in red
# LED at D13 (near micro-usb jack) on the CPX
# wiring
# one side of button -> CPX 3.3 V
# other side of button -> A3
import time
import board
import digitalio

LED = digitalio.DigitalInOut(board.D13)

BUTTON = digitalio.DigitalInOut(board.A3)
BUTTON.direction = digitalio.Direction.INPUT
BUTTON.pull = digitalio.Pull.DOWN

while True:
    if BUTTON.value:
        LED.value = True
    else:
        LED.value = False

    time.sleep(0.01)


# GS: needs to be fine tuned for application
# right now, seems to detect object when it is about
# 1" away


import time
import board
import analogio
import pwmio
from adafruit_circuitplayground import cp

ir = analogio.AnalogIn(board.IR_PROXIMITY)

tx = pwmio.PWMOut(
    board.IR_TX,
    frequency=38000,
    duty_cycle=0
)

DETECT_THRESHOLD = 2500
CLEAR_THRESHOLD = 1800

detected = False

def read_proximity():
    total = 0

    for i in range(20):
        tx.duty_cycle = 0
        time.sleep(0.005)
        off = ir.value

        tx.duty_cycle = 32768
        time.sleep(0.005)
        on = ir.value

        total += on - off

    tx.duty_cycle = 0
    return total / 20


while True:
    proximity = read_proximity()
    print("Proximity:", round(proximity))

    if proximity > DETECT_THRESHOLD:
        detected = True
    elif proximity < CLEAR_THRESHOLD:
        detected = False

    if detected:
        cp.pixels.fill((255, 0, 0))
    else:
        cp.pixels.fill((0, 255, 0))

    time.sleep(0.1)
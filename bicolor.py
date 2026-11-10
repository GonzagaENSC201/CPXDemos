# wiring: 
# + -> Vout
# - -> gnd
# D (SDA) -> A5 (SDA)
# C (SCL) -> A4 (SCL)


import time
import random
import board
from adafruit_ht16k33.matrix import Matrix8x8x2

i2c = board.I2C()
matrix = Matrix8x8x2(i2c)
matrix.auto_reload = True

def turn_row_light_on(x: int, y: int) -> None:
    """Recursively light each pixel across row y from x=0..7."""
    if x == 8:
        return

    matrix[x, y] = random.choice([matrix.LED_GREEN, matrix.LED_YELLOW, matrix.LED_RED])  # or LED_RED, LED_YELLOW, LED_OFF
    time.sleep(0.1)
    turn_row_light_on(x + 1, y)

# not using recursion here because max recursion depth gets reached
# becaues CPX has a small stack and matrix[x, y] calls alot of funcs
# behind the scenes
while True:
    for y in range(8):
        turn_row_light_on(0, y)
    matrix.fill(matrix.LED_OFF)

"""import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.3
print(cp.pixels)
# cp.pixels.fill((0, 0, 255))

while True:
    if cp.button_a:
        print("button a pressed")
        cp.pixels[2] = (0, 0, 255)
    else:
        cp.pixels[2] = (0, 0, 0)
    # time.sleep(1)
"""

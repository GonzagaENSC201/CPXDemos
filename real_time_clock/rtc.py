# GS: untested

# wiring
# RTC module	CPX
# VCC	        3.3V
# GND	        GND
# SDA	        A5 (SDA)
# SCL	        A4 (SCL)
import board
import time
import adafruit_pcf8523 # need to add library
# to do this, copy the pcf8523.mpy file into CIRCUITPY/lib

i2c = board.I2C()
rtc = adafruit_pcf8523.PCF8523(i2c)

# Change to True to set the RTC time
SET_TIME = True

if SET_TIME:
    # year, month, day, hour, minute, second, weekday, yearday, day light savings time
    rtc.datetime = time.struct_time((2026, 11, 12, 8, 0, 0, 3, -1, -1))
    print("RTC time set!")

while True:
    now = rtc.datetime

    print(f"{now.tm_mon:02}/{now.tm_mday:02}/{now.tm_year} "
          f"{now.tm_hour:02}:{now.tm_min:02}:{now.tm_sec:02}")

    time.sleep(1)
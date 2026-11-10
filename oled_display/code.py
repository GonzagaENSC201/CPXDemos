import board

"""Tiny text-only SSD1306 I2C driver for 128x64 displays on low-RAM CPX.

Requires font5x7.bin in CIRCUITPY root. No display framebuffer.
"""
import board

class SimpleOLED:
    def __init__(self, address=None):
        self.bus = board.I2C()
        while not self.bus.try_lock():
            pass
        addresses = self.bus.scan()
        if address is None:
            address = 0x3C if 0x3C in addresses else 0x3D
        if address not in addresses:
            self.bus.unlock()
            raise RuntimeError("No OLED at 0x3C or 0x3D")
        self.address = address
        self._cmd = bytearray(2)
        self._cmd[0] = 0
        self._pixels = bytearray(7)
        self._pixels[0] = 0x40
        # Data write must start with 0x40; create one reusable packet.
        self._blank = bytes([0x40] + [0] * 16)
        for cmd in (0xAE, 0xD5, 0x80, 0xA8, 0x3F, 0xD3, 0x00,
                    0x40, 0x8D, 0x14, 0x20, 0x02, 0xA1, 0xC8,
                    0xDA, 0x12, 0x81, 0x7F, 0xD9, 0xF1, 0xDB,
                    0x40, 0xA4, 0xA6, 0xAF):
            self.command(cmd)
        self.clear()

    def command(self, value):
        self._cmd[1] = value
        self.bus.writeto(self.address, self._cmd)

    def position(self, row, column):
        self.command(0xB0 + row)
        self.command(column & 0x0F)
        self.command(0x10 | (column >> 4))

    def clear(self):
        for row in range(8):
            self.position(row, 0)
            for _ in range(8):
                self.bus.writeto(self.address, self._blank)

    
    def text(self, message, row=0, column=0):
        """Write text at text row (0..7), pixel column (0..127)."""
        if row < 0 or row > 7 or column < 0 or column > 127:
            return

        self.position(row, column)

        # Seek into small on-disk fixed-width font rather than loading it in RAM.
        with open('/font5x7.bin', 'rb') as font:
            for letter in str(message):
                if column + 6 > 128:
                    break

                code = ord(letter)
                if code < 32 or code > 126:
                    code = 63  # ?

                font.seek((code - 32) * 5)
                columns = font.read(5)

                for i in range(5):
                    self._pixels[i + 1] = columns[i]

                self._pixels[6] = 0
                self.bus.writeto(self.address, self._pixels)
                column += 6


    def deinit(self):
        self.bus.unlock()


oled = SimpleOLED()
oled.text("HELLO WORLD!", 0, 0)
oled.text("Circuit Playground", 2, 0)
oled.text("Express + OLED", 3, 0)
oled.text("128x64 display", 5, 0)
print("OLED text displayed!")
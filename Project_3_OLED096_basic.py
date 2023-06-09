from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import framebuf
import utime

WIDTH = 128
HEIGHT = 64

buffer = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x80\x0f\xc0\xc0`\xc8\x13\x1b\x80\x01\xc4\x01\x02\x00\x00\xaa\xfb\x1c\xfb\xf0\xaf\xfe7\xed\xe7\x01\xa2\xda\xce\x00\x00\xff\xff\x9f\xff\xfb\xff\xfe?\xdb\xea\x03\xcf\xff\xc5\x00\x01\xff\xff\x1f\xff\xd3\xff\xff\x7f\xff\xe7\x03\x8f\xff\xca\x00\x01\x80\x7f\xbf\xcf\xfb\x1d\xf77\xdd\xd7\x03\xcf\xfe\xe7\x00\x03\xd5\x00\x19\x00s\xc2\x01p\x00\xe7\x87\x00%\xe5\x00\x03\x80\x000\x00?\x00\x03h\x00g\x0f\x80\x00a\x00\x03\x00\x00\x18\x00;\x00\x03p\x00\'\x0e\x00\x00\xec\x80\x03\x80\x000\x00\x12\x00\x03p\x00g:\x00\x00g\x00\x03\x80\x10\x18\n9\x00\x032\xa4\xf7|\x00\x00o\x00\x03\x0f\xee?\xff\xf3\xe6w\xffwg<\x05\xfe\xf5\x00\x03\x8f\xdf\x9f\xbf\xd3\xff\xff?\xef\xe7\xe8\x03\xb7\xa7\x00\x03\x8b\x7f?\x7f\xfb\xff\xff\xff\xff\xe7P\x07\xff\xcf\x80\x03\x80[\xb0\x84c\xef\x00s\xe0\x06p\r\x81\x8f\x00\x03\x80\x01\x98\x00\x07\x00\x000\x04\x07|\x0e \x07\x00\x03\x00\x03(\x00#\x80\x03(\x00\x07\x1a\x0e\x00\x0f\x00\x03\x80\x01\x98\x00;\x00\x07`\x00g\xbe\x0e\x00\x05\x00\x02\x80\x03\xbc\x007\x00\x030\x00\'\x17\x0e\x00\x0b\x00\x03\xe0\x07\x98\x00{\x80\x07h\x00g\x0f\x8a\x00\x07\x00\x01\xd3\xff_\xfd\xfb\xfa\xff}_\xe3\x07\xce\x00\x0f\x00\x03\xbf\xde\x9e\xf7\xd3\xef\xef?\xfe\xc7\x05\x8e\x00\x07\x00\x01\xff\xff7\xff\xfb\xff\xff\x7f\xff\xeb\x03\xee\x00\r\x00\x00C]\x1b\xef\xd1\xff\xfe\x08\x1e\xa4\x00L\x00\x07\x00\x00\x10\xa2\x04\x10!\x04\x00\x07\x81B\x00"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
fb = framebuf.FrameBuffer(buffer, 128, 64, framebuf.MONO_HLSB)

i2c = I2C(0, scl=Pin(13), sda=Pin(12),freq=200000)

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)

# clear screen
oled.fill(0)

# put framebuffer on screen (data=fb, x=0, y=0)
oled.blit(fb, 0, 0)

# draw pixel
# oled.pixel(30, 33, 1)
# draw rectangle
# oled.fill_rect(26, 26, 25, 25, 1)

# draw line
# 128 - width pixels
for i in range(0, 128):
    # x1, y1, x2, y2, BOOl
    oled.line(i, 0, i, 55, 1)
    utime.sleep(0.01)
    oled.show()

# invert screen 0/1
oled.invert(0)

#fill screen black
oled.fill(0)

# Put text on screen
#oled.text("Hello World", 0, 0)
oled.text("Fascinating!", 0, 20)
oled.show()
utime.sleep(3)
oled.fill(0)
oled.show()
oled.text("AlumaPower Corp.", 0, 32)

# Display 
oled.show()



import board
import displayio
import busio
import adafruit_imageload
import adafruit_displayio_ssd1306

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Macros

displayio.release_displays()

i2c = busio.I2C(board.SCL, board.SDA)
display_bus = displayio.I2CDisplayBus(i2c, device_address=0x3C)
display=adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32,)

bitmap, palette = adafruit_imageload.load() #add photo
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
group = displayio.Group()
group.append(tile_grid)
display.root_group = group



keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

keyboard.direct_pins = (
 (board.D10,),
 (board.D9,),
 (board.D8,),
 )


keyboard.keymap = [
  [KC.MACRO("/GG"), KC.MACRO("/Nice One"),KC.MACRO("/Over here!"),]
  ]


encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
 (board.D0, board.D1, board.D2),
 )

encoder_handler.map= [
 ((KC.VOLD, KC.VOLU),)
 ]

if __name__ == '__main__':
     keyboard.go()

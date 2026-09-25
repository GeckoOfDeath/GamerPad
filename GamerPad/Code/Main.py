import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.macros import Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

keyboard.direct_pins = (
 (board.D0,),
 (board.D1,),                    #rember to change to right pins once have the board
 (board.D2,),
 )

keyboard.direct_pins = keyboard.direct_pins + ((board.D3,),)




keyboard.keymap = [
  [KC.MACRO("/GG"), KC.MACRO("/Nice One"),KC.MACRO("/Over here!"), KC.MACRO("/Hello"),]
  ]


encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)

encoder_handler.pins = (
 (board.D4, board.D5, None),
 )

encoder_handler.map= [
 ((KC.VOLD, KC.VOLU),)
 ]

if __name__ == '__main__':
     keyboard.go()

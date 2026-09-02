print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
keyboard.extensions.append(MediaKeys())


keyboard = KMKKeyboard()

keyboard.col_pins = (board.D9 ,board.D8 ,board.D10 ,board.D4 ,board.D1)
keyboard.row_pins = None
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.direct_pins =(
    (board.D9 ,board.D8 ,board.D10 ,board.D4 ,board.D1)
)

encoder_handler = EncoderHandler()
encoder_handler.pins = (
    (board.D3 , board.D2 , None)
)
keyboard.modules.append(encoder_handler)

keyboard.keymap = [
    [KC.A, KC.B, KC.C, KC.D, KC.MUTE]
]

encoder_handler.map = [
    ((KC.VOLD, KC.VOLU, KC.NO),)
]

if __name__ == '__main__':
    keyboard.go()
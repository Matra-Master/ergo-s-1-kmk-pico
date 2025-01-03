from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.split import Split, SplitType
from kmk.modules.holdtap import HoldTap, HoldTapRepeat
from kmk.modules.layers import Layers
keyboard = KMKKeyboard()

keyboard.modules.append(Layers())

holdtap = HoldTap()
holdtap.tap_time = 150
keyboard.modules.append(holdtap)
# Left side Home row
HTA = KC.HT(KC.A, KC.LALT, prefer_hold=False, tap_interrupted=False, tap_time=None, repeat=HoldTapRepeat.TAP)
HTS = KC.HT(KC.S, KC.LSHIFT, prefer_hold=False, tap_interrupted=False, tap_time=None, repeat=HoldTapRepeat.TAP)
HTD = KC.HT(KC.D, KC.LCTRL, prefer_hold=False, tap_interrupted=False, tap_time=None, repeat=HoldTapRepeat.TAP)
HTF = KC.HT(KC.F, KC.LGUI, prefer_hold=False, tap_interrupted=False, tap_time=None, repeat=HoldTapRepeat.TAP)

# Right side Home row
HTJ = KC.HT(KC.J, KC.RGUI, prefer_hold=False, tap_interrupted=False, tap_time=None, repeat=HoldTapRepeat.TAP)
HTK = KC.HT(KC.K, KC.RCTRL, prefer_hold=False, tap_interrupted=False, tap_time=None, repeat=HoldTapRepeat.TAP)
HTL = KC.HT(KC.L, KC.RSHIFT, prefer_hold=False, tap_interrupted=False, tap_time=None, repeat=HoldTapRepeat.TAP)
HTSCLN = KC.HT(KC.SCLN, KC.RALT, prefer_hold=False, tap_interrupted=False, tap_time=None, repeat=HoldTapRepeat.TAP)

#Layers
FN1 = KC.MO(1)
HTTAB = KC.HT(KC.TAB, FN1, prefer_hold=False, tap_interrupted=False, tap_time=None, repeat=HoldTapRepeat.TAP)

# Ceaner keynames
_____ = KC.TRNS
XXXXX = KC.NO

split = Split(
    split_flip = False,  # If both halves are the same, but flipped, set this True
    split_side = None,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
    split_type = SplitType.UART,  # Defaults to UART
    data_pin = keyboard.data_pin,  # The primary data pin to talk to the secondary device with
    data_pin2 = keyboard.data_pin2,  # Second uart pin to allow 2 way communication
    use_pio = True, # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
    uart_flip = False,  # Reverses the RX and TX pins if both are provided
    #uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    #split_target_left=True,  # Assumes that left will be the one on USB. Set to False if it will be the right
)
keyboard.modules.append(split)


keyboard.keymap = [
    # Base layer
    [
        KC.ESC,  KC.N1, KC.N2,  KC.N3,  KC.N4,   KC.N5,                                          KC.N6,  KC.N7,   KC.N8,   KC.N9,  KC.N0,   KC.QUOT,
        HTTAB,   KC.Q,  KC.W,   KC.E,   KC.R,    KC.T,                                           KC.Y,   KC.U,    KC.I,    KC.O,   KC.P,    KC.MINS,
        KC.LGUI, HTA,   HTS,    HTD,    HTF,     KC.G,                                           KC.H,   HTJ,     HTK,     HTL,    HTSCLN,  KC.EQL,
        KC.LCTL, KC.Z,  KC.X,   KC.C,   KC.V,    KC.B,   KC.HOME,KC.END,    KC.PSCREEN, KC.CAPS, KC.N,   KC.M,    KC.COMM,KC.DOT,  KC.SLSH, KC.RSHIFT,
                 KC.GRV,KC.BSLS,KC.LEFT,KC.RIGHT,KC.SPC, KC.ENT, KC.PGUP,   KC.TAB,     KC.BSPC, KC.SPC, KC.DOWN, KC.UP,  KC.LBRC, KC.RBRC,
                                                                 KC.PGDOWN, KC.LALT
    ],
    # Fn layer
    [
        _____, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5,                             KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, _____,
        _____, _____, _____, _____, _____, _____,                             _____, _____, _____, _____, KC.F11, _____,
        _____, _____, _____, _____, _____, _____,                             _____, _____, _____, _____, KC.F12, _____,
        _____, _____, _____, _____, _____, _____, _____, _____, _____, _____, _____, _____, _____, _____, _____,  _____,
               _____, _____, _____, _____, _____, _____, _____, _____, _____, _____, _____, _____, _____, _____,
                                                         _____, _____
    ]
    # Template layer
    # [
    #     _____, _____, _____, _____, _____, _____,                             _____, _____, _____, _____, _____, _____,
    #     _____, _____, _____, _____, _____, _____,                             _____, _____, _____, _____, _____, _____,
    #     _____, _____, _____, _____, _____, _____,                             _____, _____, _____, _____, _____, _____,
    #     _____, _____, _____, _____, _____, _____, _____, _____, _____, _____, _____, _____, _____, _____, _____, _____,
    #            _____, _____, _____, _____, _____, _____, _____, _____, _____, _____, _____, _____, _____, _____,
    #                                                      _____, _____
    # ]
]

print("Keymap loaded with", len(keyboard.keymap[0]), "keys.")
if __name__ == '__main__':
    keyboard.go()

from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.split import Split, SplitType

keyboard = KMKKeyboard()


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

keyboard.keymap = [
    [
        KC.ESC,  KC.N1, KC.N2,  KC.N3,  KC.N4,   KC.N5,                                         KC.N6,  KC.N7,   KC.N8,   KC.N9,  KC.N0,   KC.QUOT,
        KC.TAB,  KC.Q,  KC.W,   KC.E,   KC.R,    KC.T,                                          KC.Y,   KC.U,    KC.I,    KC.O,   KC.P,    KC.MINS,
        KC.LGUI, KC.A,  KC.S,   KC.D,   KC.F,    KC.G,                                          KC.H,   KC.J,    KC.K,    KC.L,   KC.SCLN, KC.EQL,
        KC.LCTL, KC.Z,  KC.X,   KC.C,   KC.V,    KC.B,   KC.HOME,KC.END,    KC.PSCREEN, KC.CAPS,KC.N,    KC.M,    KC.COMM,KC.DOT,  KC.SLSH, KC.RSHIFT,
                 KC.GRV,KC.BSLS,KC.LEFT,KC.RIGHT,KC.SPC, KC.ENT, KC.PGUP,   KC.TAB,     KC.BSPC, KC.SPC, KC.DOWN, KC.UP,  KC.LBRC, KC.RBRC,
                                                                 KC.PGDOWN, KC.LALT
    ]
]

keyboard.modules.append(split)
print("Keymap loaded with", len(keyboard.keymap[0]), "keys.")
if __name__ == '__main__':
    keyboard.go()

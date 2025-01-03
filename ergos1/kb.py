import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    diode_orientation = DiodeOrientation.COLUMNS
    col_pins = ( board.GP9, board.GP8, board.GP7, board.GP6, board.GP5, board.GP4, board.GP3, board.GP2 )

    row_pins = ( board.GP15, board.GP14, board.GP13, board.GP12, board.GP11, board.GP10 )

    data_pin = board.GP1
    data_pin2 = board.GP0

    coord_mapping = [
        000,001,002,003,004,005,                    053,052,051,050,049,048,
        008,009,010,011,012,013,                    061,060,059,058,057,056,
        016,017,018,019,020,021,                    069,068,067,066,065,064,
        024,025,026,027,028,029,030,031,079,078,077,076,075,074,073,072,
            033,034,035,036,037,038,039,087,086,085,084,083,082,081,
                                    047,095
    ]



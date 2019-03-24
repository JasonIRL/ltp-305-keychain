import board
import busio
import time

from ltp_font import font
from ltp_matrix import Matrix5x7

i2c = busio.I2C(board.SCL, board.SDA)

disp = Matrix5x7(i2c)
disp.brightness = 4
disp.fill(0)


def text(phrase, seconds):
    """Outputs text onto single LTP-305 Display.

    Args:
        word (str): The string you would like to display.
        seconds (float): The number of seconds you would like each character to display.

    """
    chars = [char for char in phrase]
    for char in chars:
        if char == " ":
            disp.fill(0)
        else:
            charstring = font.get(char)
            char_list = [
                charstring[coordinates : coordinates + 2]
                for coordinates in range(0, len(charstring), 2)
            ]
            for pair in char_list:
                disp[int(pair[0]), int(pair[1])] = 1
        time.sleep(seconds)
        disp.fill(0)


while True:
    text("ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789", 0.5)

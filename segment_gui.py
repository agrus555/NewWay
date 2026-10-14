import pyautogui as pg
import keyboard as kb
import time

"""  УПРАВЛЕНИЕ
1 2 3
4 5 6
7 8 9
"""

def position(x: int, y: int):
    if x < c_x // 2:
        col = 1
    elif x < c_x + c_x // 2:
        col = 2
    else:
        col = 3

    if y < c_y // 2:
        row = 1
    elif y < c_y + c_y // 2:
        row = 2
    else:
        row = 3
    return (row - 1) * 3 + col


screen = pg.size()
c_x, c_y = screen.width // 2, screen.height // 2

while True:
    x_pos, y_pos = pg.position()
    print(f"X:{x_pos}, Y:{y_pos}")
    print(f"Segment: {position(x_pos, y_pos)}    |    Time: {time.asctime()}")

    if kb.is_pressed('esc'):
        print("Exiting...")
        break

    time.sleep(1)

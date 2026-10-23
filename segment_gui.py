import pyautogui as pg
import keyboard as kb
import mouse as ms
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

records_x = []
records_y = []
records_move = []

while True:
    x_pos, y_pos = ms.get_position()
    records_x.append(x_pos)
    records_y.append(y_pos)
    print(f"X:{x_pos}, Y:{y_pos}")
    print(f"Segment: {position(x_pos, y_pos)}    |    Time: {time.asctime()}")

    if ms.is_pressed("left"):
        records_move.append("left")
    elif ms.is_pressed("right"):
        records_move.append("right")
    else:
        records_move.append("Null")

        
    if kb.is_pressed('esc'):
        print("Launching...")
        break

    time.sleep(0.01)

for i in range(0, len(records_x)):
    pg.moveTo(records_x[i], records_y[i], duration=0.01)
    if records_move[i] == "Null":
        pass
    else:
        ms.click(records_move[i])
print("Existing...")



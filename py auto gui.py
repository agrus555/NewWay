import pyautogui as pg
import keyboard as kb
import asyncio

async def main():
    while True:
        dy, dx = 0, 0

        if kb.is_pressed('up'):
            dy -= 100
        if kb.is_pressed('down'):
            dy += 100
        if kb.is_pressed('left'):
            dx -= 100
        if kb.is_pressed('right'):
            dx += 100
        if kb.is_pressed('esc'):
            break
        if dy != 0 or dx != 0:
            pg.move(dx, dy)

        print(f"dx, dy = {dx}, {dy}")

        await asyncio.sleep(0.01)
asyncio.run(main())

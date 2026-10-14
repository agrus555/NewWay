import keyboard as kb
import time
import json

with open("commands.json", "r", encoding="utf-8") as f:
    command = json.load(f)

def command_writer(command_num: int) -> None:
    key = (f"com_{command_num}")
    if key in command:
        kb.press('t')
        time.sleep(0.1)
        kb.write(command[key])
        kb.press('enter')
        print(f"at {time.strftime('%H:%M:%S')} command: {command[key]} in {key}")
    else:
        print(f"at {time.strftime('%H:%M:%S')} command: ERROR 404: Command is not found")

while True:
    if kb.is_pressed('f9'):
        command_writer(1)
    elif kb.is_pressed('f10'):
         break
    time.sleep(0.75)

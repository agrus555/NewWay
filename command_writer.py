import keyboard as kb
import time
import json

with open("commands.json", "r", encoding="utf-8") as f:
    command = json.load(f)

def command_writer(command_num: int) -> None:
    key = f"com_{command_num}"
    if key in command:
        time.sleep(0.1)
        kb.write(command[key])
        print(f"at {time.strftime('%H:%M:%S')} command: {command[key]} in {key}")
    else:
        print(f"at {time.strftime('%H:%M:%S')} command: ERROR 404: Command is not found")

# Привязываем комбинации к функциям
kb.add_hotkey('ctrl+\\', lambda: command_writer(1))
kb.add_hotkey('ctrl+alt+\\', lambda: command_writer(2))
kb.add_hotkey('ctrl+/', lambda: command_writer(3))
kb.add_hotkey('ctrl+alt+/', lambda: command_writer(4))

print("Запуск...")

kb.wait()

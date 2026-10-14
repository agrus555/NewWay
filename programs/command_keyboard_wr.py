# pip install pynput
from pynput import keyboard
import time
import threading

events = []            # список (action, key_str, delta_time)
recording = False
replaying = False
record_start = 0.0

def key_to_str(key):
    # str(key) -> "Key.enter" или "'a'"
    return str(key)

def str_to_key(s):
    # восстановить объект Key или KeyCode из строки
    if s.startswith("Key."):
        name = s.split(".", 1)[1]
        try:
            return getattr(keyboard.Key, name)
        except Exception:
            # на крайний случай: попробуем как символ
            return keyboard.KeyCode.from_char(name)
    # символы записываются как "'a'"
    if s.startswith("'") and s.endswith("'") and len(s) >= 2:
        return keyboard.KeyCode.from_char(s[1:-1])
    # fallback
    return keyboard.KeyCode.from_char(s)

def on_press(key):
    global recording, record_start, replaying
    try:
        # горячие клавиши управления: F9 — запись, F10 — воспроизведение
        if key == keyboard.Key.f9:
            if not recording:
                events.clear()
                record_start = time.perf_counter()
                recording = True
                print("▶ Запись началась. Нажми F9 чтобы остановить.")
            else:
                recording = False
                print("⏹ Запись остановлена.")
        elif key == keyboard.Key.f10:
            if not recording and events and not replaying:
                print("🔁 Запуск воспроизведения...")
                thr = threading.Thread(target=replay, daemon=True)
                thr.start()
            else:
                print("Нечего воспроизводить или уже воспроизводится.")
        else:
            # не записываем F9/F10 и не записываем во время воспроизведения
            if recording and not replaying:
                events.append(("press", key_to_str(key), time.perf_counter() - record_start))
    except Exception as e:
        print("Ошибка on_press:", e)

def on_release(key):
    global recording
    try:
        if recording and not replaying and key not in (keyboard.Key.f9, keyboard.Key.f10):
            events.append(("release", key_to_str(key), time.perf_counter() - record_start))
    except Exception as e:
        print("Ошибка on_release:", e)

def replay():
    global replaying
    replaying = True
    controller = keyboard.Controller()
    start_time = time.perf_counter()
    for action, key_str, t in events:
        target = start_time + t
        delay = target - time.perf_counter()
        if delay > 0:
            time.sleep(delay)   # всегда неотрицательная пауза
        k = str_to_key(key_str)
        try:
            if action == "press":
                controller.press(k)
            elif action == "release":
                controller.release(k)
        except Exception as e:
            # попытка обойти возможные несовместимости
            try:
                if isinstance(k, keyboard.KeyCode) and k.char is not None:
                    if action == "press":
                        controller.press(k.char)
                    else:
                        controller.release(k.char)
            except Exception as e2:
                print("Ошибка воспроизведения", key_str, e, e2)
    replaying = False
    print("✅ Воспроизведение завершено.")

if __name__ == "__main__":
    print("F9 — старт/стоп записи, F10 — воспроизведение.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

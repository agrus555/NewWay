import json
dictt = {"Франция": {"столица": "Париж", "население": 67000000}}  # изменения перезаписывают файл json3.json
with open("json3.json", "w", encoding="utf-8") as f:  # сохранение словаря в виде файла
    json.dump(dictt, f, ensure_ascii=False, indent=4)

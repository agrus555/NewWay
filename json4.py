import json
with open("json3.json", "r", encoding="utf-8") as f:  # флаг r это чтение файла
    print(json.load(f))

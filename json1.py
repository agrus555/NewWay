import json
dictt = {"Франция": {"столица": "Париж", "население": 67000000}}
json_dictt = json.dumps(dictt, ensure_ascii=False, indent=4)
print(json_dictt)
print(f"type: {type(json_dictt)}")
# ensure_ascii=False фиксит русский язык
#indent=4 делает отступы, а 4 это количество пробелов

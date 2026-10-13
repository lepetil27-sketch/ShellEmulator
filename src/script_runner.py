from src.parser import parse_command
from src.commands import COMMANDS 

def run_script(script_path: str) -> bool:
    try:
        with open(
            script_path, "r", encoding="utf-8"
        ) as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Ошибка: скрипт не найден {script_path}")
        return False
             
    for line_num, line in enumerate(lines, 1):
        line = line.strip()
      
        if not line or line.startswith("#"):
            continue
        print(f"${line}")
      
        try:
            tokens = parse_command(line)
        except ValueError as exc:
            print(f"Ошибка парсинга "
                  f"(строка {line_num}): {exc}")
            return False
        
        if tokens is None:
            continue
        
        cmd_name = tokens[0]
        cmd_args = tokens[1:]
        
        if cmd_name not in COMMANDS:
            print(f"Ошибка: команда '{cmd_name}' не найдена'")
        return False
        
        if cmd_name == "exit":
            COMMANDS[cmd_name](cmd_args)
            break

    return True

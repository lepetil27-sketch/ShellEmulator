import os
import getpass
import socket

from src.parser import parse_command
from src.commands import COMMANDS, set_vfs
from src.config import parse_args, validate_config
from src.vfs import VirtualFileSystem
from src.script_runner import run_script


def get_prompt() -> str:
    try:
        username = getpass.getuser()
    except Exception:
        username = "unknown"

    hostname = socket.gethostname()
    home = os.path.expanduser("~")
    cwd = os.getcwd()

    if cwd.startswith(home):
        cwd = "~" + cwd[len(home):]

    return f"{username}@{hostname}:{cwd}$ "


def execute_command(tokens: list[str]) -> bool:
    cmd_name = tokens[0]
    cmd_args = tokens[1:]

    if cmd_name not in COMMANDS:
        print(f"Ошибка: команда '{cmd_name}' не найдена.")
        return False

    if cmd_name == "exit":
        return COMMANDS[cmd_name](cmd_args)

    COMMANDS[cmd_name](cmd_args)
    return False


def run_repl() -> None:
    print("Эмулятор оболочки ОС. Введите 'exit' для выхода.\n")

    while True:
        prompt = get_prompt()
        try:
            line = input(prompt)
        except EOFError:
            print("\nВыход из эмулятора оболочки.")
            break
        except KeyboardInterrupt:
            print()
            continue

        try:
            tokens = parse_command(line)
        except ValueError as exc:
            print(f"Ошибка: {exc}")
            continue

        if tokens is None:
            continue

        if execute_command(tokens):
            break


def main() -> None:
    args = parse_args()

    try:
        validate_config(args)
    except FileNotFoundError as exc:
        print(f"Ошибка конфигурации: {exc}")
        return

    vfs = VirtualFileSystem(args.vfs)
    set_vfs(vfs)

    print("=== Конфигурация эмулятора ===")
    print(f"Путь к VFS: {args.vfs or '(не указан, используется текущая)'}")
    print(f"Скрипт: {args.script or '(не указан, интерактивный режим)'}")
    print("==============================\n")

    if args.script:
        print(f"Выполнение скрипта: {args.script}\n")
        success = run_script(args.script)
        if not success:
            print("\nСкрипт завершён с ошибкой.")
        else:
            print("\nСкрипт выполнен успешно.")
        return
    run_repl()


if __name__ == "__main__":
    main()
def cmd_ls(args: list[str]) -> None:
    print("Команда: ls")
    if args:
        print(f"Аргументы: {args}")
    else:
        print("Аргументы: (нет)")


def cmd_cd(args: list[str]) -> None:
    print("Команда: cd")
    if args:
        print(f"Аргументы: {args}")
    else:
        print("Аргументы: (нет)")


def cmd_exit(args: list[str]) -> bool:
    print("Выход из эмулятора оболочки.")
    return True

COMMANDS = {
    "ls": cmd_ls,
    "cd": cmd_cd,
    "exit": cmd_exit,
}
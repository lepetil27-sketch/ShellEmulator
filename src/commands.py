from src.vfs import VirtualFileSystem


# Глобальный объект VFS
_vfs = VirtualFileSystem()


def set_vfs(vfs: VirtualFileSystem) -> None:
    global _vfs
    _vfs = vfs


def cmd_ls(args: list[str]) -> None:
    print("Команда: ls")

    if args:
        print(f"Аргументы: {args}")
    else:
        files = _vfs.list_dir()
        print(f"Файлы: {files}")


def cmd_cd(args: list[str]) -> None:
    print("Команда: cd")
    if args:
        print(f"Аргументы: {args}")
        success = _vfs.change_dir(args[0])
        if not success:
            print(f"Ошибка: директория не найдена: {args[0]}")
    else:
        print("Аргументы: (нет)")


def cmd_pwd(args: list[str]) -> None:
    print("Команда: pwd")
    print(f"Текущая директория: {_vfs.get_current_dir()}")


def cmd_exit(args: list[str]) -> bool:
    print("Выход из эмулятора оболочки.")
    return True

COMMANDS = {
    "ls": cmd_ls,
    "cd": cmd_cd,
    "pwd": cmd_pwd,
    "exit": cmd_exit,
}
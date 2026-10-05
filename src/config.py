import argparse
import os


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Эмулятор оболочки ОС"
    )

    parser.add_argument(
        "--vfs",
        type=str,
        default=None,
        help="Путь к физическому расположению VFS"
    )

    parser.add_argument(
        "--script",
        type=str,
        default=None,
        help="Путь к стартовому скрипту"
    )

    return parser.parse_args()


def validate_config(args: argparse.Namespace) -> None:
    if args.vfs and not os.path.exists(args.vfs):
        raise FileNotFoundError(
            f"Путь к VFS не существует: {args.vfs}"
        )

    if args.script and not os.path.exists(args.script):
        raise FileNotFoundError(
            f"Путь к скрипту не существует: {args.script}"
        )
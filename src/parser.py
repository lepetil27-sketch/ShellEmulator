import shlex

def parse_command(line: str) -> list[str] | None:
    line = line.strip()
    if not line:
        return None

    try:
        tokens = shlex.split(line)
    except ValueError as exc:
        raise ValueError(f"Ошибка парсинга: {exc}") from exc

    if not tokens:
        return None

    return tokens
def parse_record(line: str) -> dict:
    line = line.strip()
    if not line:
        raise ValueError('Пустая строка')
    parts = line.split(';')
    if len(parts) != 3:
        raise ValueError('Неверное количество полей')
    city, temp_str, date = parts
    if not city.strip() or not date.strip():
        raise ValueError('Пустые значения города или даты')
    try:
        temp = float(temp_str.strip())
    except ValueError:
        raise ValueError('Температура не является числом')
    return {'city': city.strip(), 'temp': temp, 'date': date.strip()}


def read_valid(lines: list[str]) -> tuple[list[dict], int]:
    valid = []
    skipped = 0
    for line in lines:
        try:
            valid.append(parse_record(line))
        except ValueError:
            skipped += 1
    return valid, skipped
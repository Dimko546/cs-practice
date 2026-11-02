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
    return {'city': city.strip(), 'temperature': temp, 'date': date.strip()}


def read_valid(lines: list[str]) -> tuple[list[dict], int]:
    valid = []
    skipped = 0
    for line in lines:
        try:
            valid.append(parse_record(line))
        except ValueError:
            skipped += 1
    return valid, skipped


def average_by_city(records: list[dict]) -> dict:
    total = {}
    count = {}
    for r in records:
        c = r['city']
        t = r['temp']
        total[c] = total.get(c, 0.0) + t
        count[c] = count.get(c, 0) + 1
    return {c: round(total[c] / count[c], 1) for c in total}


def warmest_city(avg_temps: dict) -> str:
    if not avg_temps:
        return ''
    max_temp = max(avg_temps.values())
    candidates = [c for c, t in avg_temps.items() if t == max_temp]
    return min(candidates)

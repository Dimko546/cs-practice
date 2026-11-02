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

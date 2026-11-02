def parse_record(line: str) -> dict:
    fields = line.split(";")

    if len(fields) != 3:
        raise ValueError("Ожидалось ровно три поля")

    city, temperature_text, date = (field.strip() for field in fields)

    if not city:
        raise ValueError("Не указан город")
    if not date:
        raise ValueError("Не указана дата")

    try:
        temperature = float(temperature_text)
    except ValueError as error:
        raise ValueError("Температура должна быть числом") from error

    return {
        "city": city,
        "temperature": temperature,
        "date": date,
    }


def read_valid(lines: list[str]) -> list[dict]:
    records = []

    for line in lines:
        if not line.strip():
            continue

        try:
            records.append(parse_record(line))
        except ValueError:
            continue

    return records


def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}

    for record in records:
        city = record["city"]
        totals[city] = totals.get(city, 0.0) + record["temperature"]
        counts[city] = counts.get(city, 0) + 1

    return {
        city: round(totals[city] / counts[city], 1)
        for city in totals
    }


def warmest_city(records: list[dict]) -> str:
    totals = {}
    counts = {}

    for record in records:
        city = record["city"]
        totals[city] = totals.get(city, 0.0) + record["temperature"]
        counts[city] = counts.get(city, 0) + 1

    if not totals:
        return ""
    return min(
        totals,
        key=lambda city: (-totals[city] / counts[city], city),
    )
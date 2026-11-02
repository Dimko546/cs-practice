import sys
from stats import read_valid, average_by_city, warmest_city


def main():
    lines = sys.stdin.read().splitlines()
    records, skipped = read_valid(lines)
    avg_temps = average_by_city(records)
    warmest = warmest_city(avg_temps)


    parsed_count = len(records)
    temp_value = avg_temps[warmest] if warmest else 0.0


    print(parsed_count)
    print(skipped)
    print(f'{temp_value:.1f}')

if __name__ == '__main__':
    main()
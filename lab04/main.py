import sys

from stats import average_by_city, read_valid, warmest_city


lines = sys.stdin.read().splitlines()
records = read_valid(lines)
non_empty_lines = sum(bool(line.strip()) for line in lines)
skipped_count = non_empty_lines - len(records)

averages = average_by_city(records)
city = warmest_city(records)

print(len(records))
print(skipped_count)
print(f"{averages[city]:.1f}" if city else "0.0")
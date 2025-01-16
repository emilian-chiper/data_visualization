from pathlib import Path
import csv

path = Path('./sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract high temperatures.
highs = [int(row[4]) for row in reader]

print(highs)


from pathlib import Path
import csv

path = Path('./sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract rainfall data.
rain = [float(row[5]) for row in reader]

print(rain)


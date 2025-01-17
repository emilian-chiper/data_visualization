from pathlib import Path
import csv

import matplotlib.pyplot as plt

path = Path('./sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract rainfall data.
rain = [float(row[5]) for row in reader]

# Plot the rain data.
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(rain, color='dodgerblue')

# Format plot.
ax.set_title("Daily precipitation maximum, 2021\nSitka Highs, AK", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("PRCP", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()


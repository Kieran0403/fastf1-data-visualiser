import fastf1
import fastf1.plotting
import matplotlib.pyplot as plt
from team_colours import get_colour

# Enable the cache (saves re-downloading data)
fastf1.Cache.enable_cache('f1_cache')

# Load a session - pick any 2024 race
session = fastf1.get_session(2024, 'Monza', 'R')
session.load()

# Pick your two drivers using their 3-letter codes
driver1 = 'RUS'
driver2 = 'NOR'
season = 2024;

# Get their laps, dropping any outliers (safety car laps etc.)
laps_d1 = session.laps.pick_driver(driver1).pick_quicklaps().reset_index()
laps_d2 = session.laps.pick_driver(driver2).pick_quicklaps().reset_index()

# Convert lap times to seconds for easier plotting
laps_d1['LapTimeSeconds'] = laps_d1['LapTime'].dt.total_seconds()
laps_d2['LapTimeSeconds'] = laps_d2['LapTime'].dt.total_seconds()

# Plot
fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(laps_d1['LapNumber'], laps_d1['LapTimeSeconds'], label=driver1, color=get_colour(driver1,season))
ax.plot(laps_d2['LapNumber'], laps_d2['LapTimeSeconds'], label=driver2, color=get_colour(driver2,season))

ax.set_xlabel('Lap Number')
ax.set_ylabel('Lap Time (seconds)')
ax.set_title(f'Lap Time Comparison: {driver1} vs {driver2} — 2024 Monza GP')
ax.legend()

plt.tight_layout()
plt.savefig('lap_comparison.png', dpi=150)
plt.show()


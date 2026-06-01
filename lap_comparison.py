import fastf1
import fastf1.plotting
import matplotlib.pyplot as plt
from team_colours import get_colour,driver_colours_2024,driver_colours_2025

# Enable the cache (saves re-downloading data)
fastf1.Cache.enable_cache('f1_cache')



# Pick your two drivers using their 3-letter codes, along with track and the season + validate them
track = input("Enter race/track (e.g. Monza): ").title()

season = int(input("Enter year 2024/2025): "))
if season not in (2024,2025):
    print(f"Invalid season {season}")

driver1 = input("Enter driver 1 code (e.g. VER): ").upper()[:3] #Take first 3 characters and force upper case to validate
driver2 = input("Enter driver 2 code (e.g. NOR): ").upper()[:3]

valid_drivers = set(driver_colours_2024.keys()) | set(driver_colours_2025.keys())
if driver1 not in valid_drivers:
    print(f"Invalid choice: {driver1}")
elif driver2 not in valid_drivers:
    print(f"Invalid choice: {driver2}")

# Load a session - pick any 2024 race
session = fastf1.get_session(season, track, 'R')
session.load()

# Get their laps, dropping any outliers (safety car laps etc.)
laps_d1 = session.laps.pick_driver(driver1).reset_index()
laps_d2 = session.laps.pick_driver(driver2).reset_index()

# Convert lap times to seconds for easier plotting
laps_d1['LapTimeSeconds'] = laps_d1['LapTime'].dt.total_seconds()
laps_d2['LapTimeSeconds'] = laps_d2['LapTime'].dt.total_seconds()

# Plot
fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(laps_d1['LapNumber'], laps_d1['LapTimeSeconds'], label=driver1, color=get_colour(driver1,season))
ax.plot(laps_d2['LapNumber'], laps_d2['LapTimeSeconds'], label=driver2, color=get_colour(driver2,season))

ax.set_xlabel('Lap Number')
ax.set_ylabel('Lap Time (seconds)')
ax.set_title(f'Lap Time Comparison: {driver1} vs {driver2} — {season} {track} GP')
ax.legend()

plt.tight_layout()
plt.savefig('lap_comparison.png', dpi=150)
plt.show()
import fastf1, fastf1.plotting
import sys, os
import matplotlib.pyplot as plt
from team_colours import get_colour,driver_colours_2024,driver_colours_2025

# Enable the cache (saves re-downloading data) and make directory if its not there
os.makedirs('f1_cache', exist_ok=True)
fastf1.Cache.enable_cache('f1_cache')



# Pick your two drivers using their 3-letter codes, along with track and the season + validate them
track = input("Enter race/track (e.g. Monza): ").title()

season = int(input("Enter year 2024/2025): "))
if season not in (2024,2025):
    print(f"Invalid season selected: {season}")
    sys.exit()

driver1 = input("Enter driver 1 code (e.g. VER): ").upper()[:3] #Take first 3 characters and force upper case to validate
driver2 = input("Enter driver 2 code (e.g. NOR): ").upper()[:3]

#Check if the drivers are in the season's driver list
season_colours = {2024: driver_colours_2024, 2025: driver_colours_2025}[season]

if driver1 not in season_colours:
    sys.exit(f"{driver1} isn't in the {season} driver list")
if driver2 not in season_colours:
    sys.exit(f"{driver2} isn't in the {season} driver list")

# Load a session - catch error if not a valid race or unexpected error occured
try:
    session = fastf1.get_session(season, track, 'R')
    session.load()
except Exception as e:
    sys.exit(f"Couldn't load sesssion: {e}")
    

# Get their laps, dropping any outliers (e.g. safety car laps) with pick_quicklaps()
laps_d1 = session.laps.pick_drivers(driver1).pick_quicklaps().reset_index()
laps_d2 = session.laps.pick_drivers(driver2).pick_quicklaps().reset_index()

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
import fastf1, fastf1.plotting
import sys, os
import matplotlib.pyplot as plt
from team_colours import get_colour, driver_colours_2024, driver_colours_2025

# Enable the cache (saves re-downloading data) and make directory if its not there
os.makedirs('f1_cache', exist_ok=True)
fastf1.Cache.enable_cache('f1_cache')

# Pick your two drivers using their 3-letter codes, along with track and the season + validate them
track = input("Enter race/track (e.g. Monza): ").title()

try:
    season = int(input("Enter year (2024/2025): "))
except ValueError:
    sys.exit("Year must be a number.")

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
    session = fastf1.get_session(season, track, 'Q') #Q for quali
    session.load()
except Exception as e:
    sys.exit(f"Couldn't load session: {e}")

# Get the fastest lap for each driver and validate them
fastest_d1 = session.laps.pick_drivers(driver1).pick_fastest()
fastest_d2 = session.laps.pick_drivers(driver2).pick_fastest()

if fastest_d1 is None:
    sys.exit(f"No fast lap set in this session {driver1}")
if fastest_d2 is None:
    sys.exit(f"No fast lap set in this session {driver2}")


# Get telemetry and add distance so plot by position on the track
telemetry_d1 = fastest_d1.get_car_data().add_distance()
telemetry_d2 = fastest_d2.get_car_data().add_distance()

# Plot
fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

# Speed
axes[0].plot(telemetry_d1['Distance'], telemetry_d1['Speed'], label=driver1, color=get_colour(driver1,season))
axes[0].plot(telemetry_d2['Distance'], telemetry_d2['Speed'], label=driver2, color=get_colour(driver2,season))
axes[0].set_ylabel('Speed (km/h)')
axes[0].legend()

# Throttle
axes[1].plot(telemetry_d1['Distance'], telemetry_d1['Throttle'], label=driver1, color=get_colour(driver1,season))
axes[1].plot(telemetry_d2['Distance'], telemetry_d2['Throttle'], label=driver2, color=get_colour(driver2,season))
axes[1].set_ylabel('Throttle %')

# Brake
axes[2].plot(telemetry_d1['Distance'], telemetry_d1['Brake'], label=driver1, color=get_colour(driver1,season))
axes[2].plot(telemetry_d2['Distance'], telemetry_d2['Brake'], label=driver2, color=get_colour(driver2,season))
axes[2].set_ylabel('Brake')
axes[2].set_xlabel('Distance (m)')

fig.suptitle(f'Qualifying Telemetry: {driver1} vs {driver2} — {season} {track} GP')
plt.tight_layout()
plt.savefig('qualifying_telemetry.png', dpi=150)
plt.show()

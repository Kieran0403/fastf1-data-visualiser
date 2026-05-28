# FastF1DataVisualiser
FastF1 API and Matplotlib charts/graphs to display race lap time data comparisons between 2 selected drivers.

### FastF1
This project uses the [FastF1](https://docs.fastf1.dev/) Python library to access official F1 timing and telemetry data. FastF1 pulls from the F1 timing API and provides structured access to lap times, sector times, tyre compounds, pit stop data, and full car telemetry including speed, throttle, brake, gear, and DRS for every driver at every session.

Data is cached locally to avoid repeated downloads — the `f1_cache` folder stores session data so subsequent runs are much faster.

### Data Coverage

This project currently supports 2024 and 2025 season data. These are the seasons for which FastF1 provides the most complete and reliable timing and telemetry data. Earlier seasons may have incomplete or inconsistent data depending on the session, so results cannot be guaranteed to be accurate outside of this range.

Team colours are also mapped per season to account for driver moves (exc. mid-season changes) and livery changes between years.

### Example output 
<img width="1198" height="500" alt="Screenshot 2026-05-28 at 10 41 04" src="https://github.com/user-attachments/assets/29c3c96d-407c-4e9f-be98-f9aab47231b9" />

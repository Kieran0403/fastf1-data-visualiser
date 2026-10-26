# FastF1DataVisualiser
FastF1 API and Matplotlib charts/graphs to display race lap time data comparisons between 2 selected drivers.

### FastF1
This project uses the [FastF1](https://docs.fastf1.dev/) Python library to access official F1 timing and telemetry data. FastF1 pulls from the F1 timing API and provides structured access to lap times, sector times, tyre compounds, pit stop data, and full car telemetry including speed, throttle, brake, gear, and DRS for every driver at every session.

Data is cached locally to avoid repeated downloads — the `f1_cache` folder stores session data so subsequent runs are much faster.

### Data Coverage

This project currently supports 2024 and 2025 season data. I have found that other seasons have produced incomplete data more consistently, so have limited the scope to these two seasons.

Team colours are also mapped per season to account for driver moves (exc. mid-season changes) and livery changes between years.

### Example output - lap_comparision.py
<img width="1198" height="500" alt="Screenshot 2026-05-28 at 10 41 04" src="https://github.com/user-attachments/assets/29c3c96d-407c-4e9f-be98-f9aab47231b9" />

### Example output - qualifying_telemetry.py
<img width="720" height="600" alt="Screenshot 2026-06-08 at 10 40 37" src="https://github.com/user-attachments/assets/ee3114d0-638c-42d3-a2de-c87092d084ea" />

## Getting Started

### Requirements
- Python 3.12 or newer
- An internet connection (the first run downloads session data)

### Installation

```bash
git clone https://github.com/Kieran0403/fastf1-data-visualiser.git
cd fastf1-data-visualiser

python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

### Usage

**Race lap time comparison**

```bash
python3 lap_comparison.py
```

**Qualifying telemetry comparison**

```bash
python3 qualifying_telemetry.py
```

Each script asks for:

| Prompt | Example |
|--------|---------|
| Race/track | `Monza` |
| Year (2024 or 2025) | `2025` |
| Driver 1 code | `VER` |
| Driver 2 code | `NOR` |

The chart is shown on screen and saved as `lap_comparison.png` or `qualifying_telemetry.png` in the project folder.

> **Note:** the first run for a session can take a minute while FastF1 downloads the data. It's cached in `f1_cache/`, so repeat runs are much faster.
> Unfortunatley, the FastF1 API now requires a F1 TV subscription to download new cache data.

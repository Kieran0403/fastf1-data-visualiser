#Dictionary of driver codes and their correspoinding colour for each relevant year
driver_colours_2024={ 
    'VER': '#3671C6',  # Red Bull
    'PER': '#3671C6',
    'HAM': '#27F4D2',  # Mercedes
    'RUS': '#27F4D2',
    'LEC': '#E8002D',  # Ferrari
    'SAI': '#E8002D',
    'NOR': '#FF8000',  # McLaren
    'PIA': '#FF8000',
    'ALO': '#358C75',  # Aston Martin
    'STR': '#358C75',
    'GAS': '#0093CC',  # Alpine
    'OCO': '#0093CC',
    'LAW': '#00E0D0',  # Racing Bulls
    'TSU': '#5E8FAA',
    'RIC': '#00E0D0',
    'BOT': '#C92D4B',  # Kick Sauber
    'ZHO': '#C92D4B',
    'MAG': '#B6BABD',  # Haas
    'HUL': '#B6BABD',
    'BEA': '#B6BABD',
    'ALB': '#64C4FF',  # Williams
    'SAR': '#64C4FF',
    'COL': '#64C4FF'
}

driver_colours_2025={
    'VER': '#3671C6',  # Red Bull
    'TSU': '#3671C6',
    'ANT': '#27F4D2',  # Mercedes
    'RUS': '#27F4D2',
    'LEC': '#E8002D',  # Ferrari
    'HAM': '#E8002D',
    'NOR': '#FF8000',  # McLaren
    'PIA': '#FF8000',
    'ALO': '#358C75',  # Aston Martin
    'STR': '#358C75',
    'GAS': '#0093CC',  # Alpine
    'DOO': '#0093CC',
    'COL': '#0093CC',
    'LAW': '#00E0D0',  # Racing Bulls
    'HAD': '#5E8FAA',
    'BOR': '#C92D4B',  # Kick Sauber
    'HUL': '#C92D4B',
    'BEA': '#B6BABD',  # Haas
    'OCO': '#B6BABD',
    'ALB': '#64C4FF',  # Williams
    'SAI': '#64C4FF'
}

def get_colour(driver_code,season):
    """Method to return the corect colour for the driver.

    Method find the correct year (2024 or 2025) and then uses a ductionary to look up the 
    corresponding HEX value for that driver.

    Args:
        driver_code (string): 3 digit driver name code.
        season (integer): Season the data is collected from.

    Returns:
        string: HEX colour code for the driver.
    """
    if season==2024:
        return driver_colours_2024.get(driver_code)
    return driver_colours_2025.get(driver_code)
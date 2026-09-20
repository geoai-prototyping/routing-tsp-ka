import pandas as pd
import requests

# 1. Define your locations (Longitude, Latitude)
coordinates = [
    [8.401, 49.000],  # Hauptbahnhof
    [8.404, 49.013],  # Schloss Karlsruhe
    [8.486, 49.008],  # Durlach
]

# Format coordinates as 'lon1,lat1;lon2,lat2;...'
coord_str = ";".join([f"{lon},{lat}" for lon, lat in coordinates])

# 2. Call OSRM Table API
url = f"http://localhost:6000/table/v1/driving/{coord_str}?annotations=distance,duration"
response = requests.get(url).json()

# 3. Extract matrices
# Duration is in seconds, Distance is in meters
durations_df = pd.DataFrame(
    response["durations"],
    index=["Hbf", "Schloss", "Durlach"],
    columns=["Hbf", "Schloss", "Durlach"],
)
distances_df = pd.DataFrame(
    response["distances"],
    index=["Hbf", "Schloss", "Durlach"],
    columns=["Hbf", "Schloss", "Durlach"],
)

print("--- Duration Matrix (Seconds) ---")
print(durations_df)

print("\n--- Distance Matrix (Meters) ---")
print(distances_df)
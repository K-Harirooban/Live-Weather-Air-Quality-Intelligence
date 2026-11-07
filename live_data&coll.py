import requests
import pandas as pd
from datetime import datetime

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 13.0827,
    "longitude": 80.2707,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}

response = requests.get(url, params=params, timeout=30)

if response.status_code == 200:

    data = response.json()

    weather = data["current"]

    df = pd.DataFrame([weather])

    df["city"] = "Chennai"
    df["collected_at"] = datetime.now()

    print("\nLIVE WEATHER DATA")
    print(df)

    df.to_csv("data/weather_data.csv", index=False)

    print("\nData saved successfully!")

else:
    print("Error:", response.status_code)
import requests
import pandas as pd 
import os
from datetime import datetime

#chennai city coordinates
latitude = 13.0827
longitude = 80.2707

#weather API 
weather_url = "https://api.open-meteo.com/v1/forecast"

weather_params = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}

#Air quality API
air_url = "https://air-quality-api.open-meteo.com/v1/air-quality"

air_params = {
    "latitude": latitude,
    "longitude": longitude,
    "current": "pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,ozone,european_aqi,us_aqi"
}

#fetch data
weather_response = requests.get(weather_url,params  = weather_params, timeout = 20)

air_response = requests.get(air_url, params = air_params , timeout = 30)

weather_response.raise_for_status()
air_response.raise_for_status()


weather_data = weather_response.json()["current"]
air_data = air_response.json()["current"]

#combine both response

record = {
    "city": "Chennai",
    "collected_at": datetime.now().isoformat(timespec="seconds")
}

record.update(weather_data)
record.update(air_data)

#convert to dataframe
df = pd.DataFrame([record])

os.makedirs("data", exist_ok=True)

file_path = r"C:\Users\acer\Videos\Live Weather & Air Quality Intelligence\Chennai_1990_2022_Madras.csv"

if os.path.exists(file_path):
    df.to_csv(file_path, mode="a", header=False, index=False)
else:
    df.to_csv(file_path, index=False)

print("data Collected successfully!")
print(df.to_string(index=False))
print("\nsaved to:", file_path)

import pandas as pd

df = pd.read_csv("data/chennai_weather_air_quality.csv")

print(df.head())
print("\nDataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())
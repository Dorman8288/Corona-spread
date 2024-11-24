import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Parameters for mock data
NUM_COUNTRIES = 20
NUM_DAYS = 60
CASE_RANGE = (0, 5000)

# Random countries with approximate lat/lon values
COUNTRIES = [
    {"country": "USA", "latitude": 37.0902, "longitude": -95.7129},
    {"country": "India", "latitude": 20.5937, "longitude": 78.9629},
    {"country": "Brazil", "latitude": -14.2350, "longitude": -51.9253},
    {"country": "Russia", "latitude": 61.5240, "longitude": 105.3188},
    {"country": "South Africa", "latitude": -30.5595, "longitude": 22.9375},
    {"country": "China", "latitude": 35.8617, "longitude": 104.1954},
    {"country": "Australia", "latitude": -25.2744, "longitude": 133.7751},
    {"country": "Germany", "latitude": 51.1657, "longitude": 10.4515},
    {"country": "France", "latitude": 46.6034, "longitude": 1.8883},
    {"country": "Japan", "latitude": 36.2048, "longitude": 138.2529},
    {"country": "Italy", "latitude": 41.8719, "longitude": 12.5674},
    {"country": "Mexico", "latitude": 23.6345, "longitude": -102.5528},
    {"country": "Canada", "latitude": 56.1304, "longitude": -106.3468},
    {"country": "Spain", "latitude": 40.4637, "longitude": -3.7492},
    {"country": "Turkey", "latitude": 38.9637, "longitude": 35.2433},
    {"country": "Argentina", "latitude": -38.4161, "longitude": -63.6167},
    {"country": "United Kingdom", "latitude": 55.3781, "longitude": -3.4360},
    {"country": "South Korea", "latitude": 35.9078, "longitude": 127.7669},
    {"country": "Egypt", "latitude": 26.8206, "longitude": 30.8025},
    {"country": "Indonesia", "latitude": -0.7893, "longitude": 113.9213},
]

# Generate a list of dates
start_date = datetime(2023, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(NUM_DAYS)]

# Generate mock data
mock_data = []
for date in dates:
    for country in random.sample(COUNTRIES, k=random.randint(5, NUM_COUNTRIES)):
        cases = random.randint(*CASE_RANGE)
        mock_data.append({
            "country": country["country"],
            "latitude": country["latitude"],
            "longitude": country["longitude"],
            "date": date,
            "cases": cases
        })

# Create a DataFrame
df = pd.DataFrame(mock_data)

# Save to a CSV file
output_file = "mock_covid_data.csv"
df.to_csv(output_file, index=False)

print(f"Mock data saved to {output_file}")

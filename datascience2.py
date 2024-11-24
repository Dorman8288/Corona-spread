import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.basemap import Basemap

# Load your data (replace 'your_data.csv' with your actual dataset)
# Ensure the dataset has columns: 'country', 'latitude', 'longitude', 'date', 'cases'
df = pd.read_csv('mock_covid_data.csv')

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Create a figure and basemap
fig, ax = plt.subplots(figsize=(12, 8))
m = Basemap(projection='cyl', resolution='c', ax=ax)
m.drawcoastlines()
m.drawcountries()

# Prepare the data for animation
dates = sorted(df['date'].unique())
cases_by_date = {date: df[df['date'] == date] for date in dates}

# Define the update function for animation
scatter = None
def update(frame):
    global scatter
    ax.clear()
    m.drawcoastlines()
    m.drawcountries()
    
    date = dates[frame]
    data = cases_by_date[date]
    
    # Scale the cases to a size for better visualization
    sizes = data['cases'].apply(lambda x: max(10, x**0.5))
    
    scatter = m.scatter(
        data['longitude'], data['latitude'],
        s=sizes, c='red', alpha=0.6, edgecolor='k', zorder=5
    )
    ax.set_title(f"COVID-19 Cases on {date.strftime('%Y-%m-%d')}", fontsize=16)

# Create the animation
ani = FuncAnimation(
    fig, update, frames=len(dates), interval=500, repeat=True
)

# Save or display the animation
ani.save('covid_cases_animation.mp4', fps=5, writer='ffmpeg')
plt.show()

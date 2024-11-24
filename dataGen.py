import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_mock_covid_data(output_file='mock_covid_data.csv'):
    """
    Generate mock COVID-19 data for testing the animation.
    Creates a CSV with realistic-looking case numbers that show exponential growth
    and different patterns for different countries.
    """
    # List of major countries from Natural Earth dataset
    countries = [
        'United States of America', 'Brazil', 'Russia', 'India', 'China',
        'France', 'Germany', 'United Kingdom', 'Italy', 'Spain',
        'Japan', 'South Korea', 'Australia', 'Mexico', 'Canada',
        'South Africa', 'Egypt', 'Nigeria', 'Saudi Arabia'
    ]
    
    # Generate dates for 6 months with 5-day intervals
    start_date = datetime(2020, 1, 1)
    dates = [(start_date + timedelta(days=x)) for x in range(0, 180, 5)]
    
    # Create empty lists to store the data
    data_list = []
    
    # Generate data for each country
    for country in countries:
        # Base parameters for this country
        base_cases = np.random.randint(10, 100)  # Initial cases
        growth_rate = np.random.uniform(1.2, 1.5)  # Growth rate between updates
        volatility = np.random.uniform(0.1, 0.3)   # Random variation
        
        # Generate case numbers for each date
        current_cases = base_cases
        for date in dates:
            # Add some randomness to the growth
            random_factor = np.random.normal(1, volatility)
            current_cases *= growth_rate * random_factor
            
            # Add seasonal variation
            seasonal_factor = 1 + 0.2 * np.sin(2 * np.pi * date.timetuple().tm_yday / 365)
            current_cases *= seasonal_factor
            
            # Ensure cases only increase
            current_cases = max(current_cases, base_cases)
            
            # Add row to data
            data_list.append({
                'date': date.strftime('%Y-%m-%d'),
                'country': country,
                'cases': int(current_cases)
            })
    
    # Create DataFrame
    df = pd.DataFrame(data_list)
    
    # Sort by date and country
    df = df.sort_values(['date', 'country'])
    
    # Save to CSV
    df.to_csv(output_file, index=False)
    print(f"Mock data has been saved to {output_file}")
    
    # Display first few rows and basic statistics
    print("\nFirst few rows of the generated data:")
    print(df.head())
    print("\nSummary statistics:")
    print(df.groupby('country')['cases'].agg(['min', 'max', 'mean']).round(2))
    
    return df

if __name__ == "__main__":
    # Generate the mock data
    df = generate_mock_covid_data('mock_covid_data.csv')
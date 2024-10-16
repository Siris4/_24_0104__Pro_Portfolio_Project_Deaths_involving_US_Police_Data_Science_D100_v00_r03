import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file containing the data on police killings
file_path_deaths = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r02\Data\Deaths_by_Police_US.csv'
df_deaths = pd.read_csv(file_path_deaths, encoding='ISO-8859-1')

# Display the first few rows to understand the structure
print(df_deaths.head())

# Convert the date column to datetime format (assuming there's a 'date' column in the data)
df_deaths['date'] = pd.to_datetime(df_deaths['date'], errors='coerce')

# Extract the year from the date
df_deaths['year'] = df_deaths['date'].dt.year

# Group the data by year and count the number of deaths in each year
deaths_by_year = df_deaths.groupby('year').size()

# Create a line plot to analyze the trend of police killings over time
plt.figure(figsize=(10, 6))
plt.plot(deaths_by_year.index, deaths_by_year.values, marker='o', linestyle='-', color='b')

# Add labels and a title
plt.xlabel('Year')
plt.ylabel('Number of Deaths')
plt.title('Number of Police Killings Over Time')

# Show the plot
plt.tight_layout()
plt.show()

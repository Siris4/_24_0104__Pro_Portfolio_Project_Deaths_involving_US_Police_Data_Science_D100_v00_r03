import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file containing the data on police killings
file_path_deaths = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r02\Data\Deaths_by_Police_US.csv'
df_deaths = pd.read_csv(file_path_deaths, encoding='ISO-8859-1')

# Display the first few rows to understand the structure
print(df_deaths.head())

# Group the data by city and count the number of deaths in each city
deaths_by_city = df_deaths['city'].value_counts().head(10)

# Create a bar chart to rank the top 10 cities with the most police killings
plt.figure(figsize=(10, 6))
plt.barh(deaths_by_city.index, deaths_by_city.values, color='skyblue')

# Add labels and a title
plt.xlabel('Number of Deaths')
plt.ylabel('City')
plt.title('Top 10 Cities with the Most Police Killings')

# Invert y-axis to show the highest value at the top
plt.gca().invert_yaxis()

# Show the plot
plt.tight_layout()
plt.show()

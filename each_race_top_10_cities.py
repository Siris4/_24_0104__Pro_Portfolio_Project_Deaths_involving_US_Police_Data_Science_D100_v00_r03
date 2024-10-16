import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file containing the data on police killings
file_path_deaths = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r02\Data\Deaths_by_Police_US.csv'
df_deaths = pd.read_csv(file_path_deaths, encoding='ISO-8859-1')

# Display the first few rows to understand the structure
print(df_deaths.head())

# Group the data by city and count the number of deaths in each city
top_10_cities = df_deaths['city'].value_counts().head(10).index

# Filter the dataset to include only rows for the top 10 cities
df_top_10_cities = df_deaths[df_deaths['city'].isin(top_10_cities)]

# Group the data by city and race, then count the number of deaths for each race in each city
race_by_city = df_top_10_cities.groupby(['city', 'race']).size().unstack(fill_value=0)

# Calculate the race share in each city (percentage)
race_share_by_city = race_by_city.div(race_by_city.sum(axis=1), axis=0) * 100

# Map race codes to full race names
race_labels = {
    'W': 'White',
    'B': 'Black',
    'H': 'Hispanic',
    'A': 'Asian',
    'N': 'Native American',
    'O': 'Other',
    'Unknown': 'Unknown'
}

# Rename columns in the dataframe using the race labels
race_share_by_city = race_share_by_city.rename(columns=race_labels)

# Display the race share by city
print(race_share_by_city)

# Plotting the data: Stacked bar chart
race_share_by_city.plot(kind='bar', stacked=True, figsize=(10, 6))

# Add labels and title
plt.xlabel('City')
plt.ylabel('Race Share (%)')
plt.title('Race Share in the Top 10 Cities with the Most Police Killings')

# Add a legend with well-spelled-out race names
plt.legend(title='Race', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.tight_layout()
plt.show()

import pandas as pd

# Load the CSV file containing the data on police killings
file_path_deaths = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r02\Data\Deaths_by_Police_US.csv'
df_deaths = pd.read_csv(file_path_deaths, encoding='ISO-8859-1')

# Display the first few rows to understand the structure
print(df_deaths.head())

# Calculate the total number of deaths
total_deaths = len(df_deaths)

# Calculate the number of people diagnosed with mental illness
mental_illness_counts = df_deaths['signs_of_mental_illness'].value_counts()

# Get the count of people with mental illness
people_with_mental_illness = mental_illness_counts.get(True, 0)

# Calculate the percentage of people with mental illness
percentage_mental_illness = (people_with_mental_illness / total_deaths) * 100

# Print the result
print(f"Percentage of people killed by police diagnosed with a mental illness: {percentage_mental_illness:.2f}%")

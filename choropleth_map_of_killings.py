import pandas as pd
import plotly.express as px

# Load the CSV file containing the data on police killings
file_path_deaths = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0104__Day100_Pro_Portfolio_Project_Deaths_involving_US_Police_Data_Science_241015\NewProject\r00_env_START\r02\Data\Deaths_by_Police_US.csv'
df_deaths = pd.read_csv(file_path_deaths, encoding='ISO-8859-1')

# Display the first few rows to understand the structure
print(df_deaths.head())

# Group the data by state and count the number of deaths in each state
deaths_by_state = df_deaths['state'].value_counts().reset_index()
deaths_by_state.columns = ['state', 'deaths']

# Create a choropleth map of police killings by state
fig = px.choropleth(
    deaths_by_state,
    locations='state',
    locationmode='USA-states',
    color='deaths',
    scope='usa',
    color_continuous_scale='Reds',
    labels={'deaths': 'Number of Deaths'},
    title='Police Killings by U.S. State'
)

# Show the plot
fig.show()

import pandas as pd
import plotly.express as px

file_path = 'C:\\Users\\sibis\\Desktop\\NFIT_ProjectCode\\Earthquakes_v2.csv'
df = pd.read_csv(file_path)

df['Date'] = df['DATETIME'].str.split().str[0]

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

start_date_str = input("Enter the start date (YYYY-MM-DD): ")
end_date_str = input("Enter the end date (YYYY-MM-DD): ")

start_date = pd.to_datetime(start_date_str, errors='coerce')
end_date = pd.to_datetime(end_date_str, errors='coerce')

df_subset = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)].head(300)

fig = px.scatter_geo(
    df_subset,
    lat='LAT',
    lon='LONG',
    size='MAGNITUDE',
    color='MAGNITUDE',
    animation_frame='Date',
    projection='natural earth',
    title=f'Earthquakes in Greece ({start_date_str} to {end_date_str})',
    template='plotly',
    size_max=50
)

fig.show()

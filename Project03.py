import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

save_path = r"images"

# Don't use absolute paths, they only work for you.
load_ch_snow =  r"data\Chippewa_snowdepth.csv"
load_ch_temp =  r"data\Chippewa_temp.csv"
load_la_snow =  r"data\Lacrosse_snowdepth.csv"
load_la_temp =  r"data\Lacrosse_temp.csv"
load_ma_snow =  r"data\Madison_snowdepth.csv"
load_ma_temp =  r"data\Madison_temp.csv"
load_mil_snow = r"data\Milwaukee_snowdepth.csv"
load_mil_temp = r"data\Milwaukee_temp.csv"

#clean data in _snowdepth.csv files, drop na values in column"DailySnowDepth"
def clean_snowdepth(file_path):
    df = pd.read_csv(file_path, parse_dates=["DATE"])
    df.set_index("DATE", inplace=True)
    df["DailySnowDepth"] = pd.to_numeric(df["DailySnowDepth"], errors='coerce')
    df_clean = df["DailySnowDepth"].dropna()
    return df_clean

#clean data in _temp.csv files, drop na values in column"DailyDepartureFromNormalAverageTemperature"
def clean_temp(file_path):
    df = pd.read_csv(file_path, parse_dates=["DATE"])
    df.set_index("DATE", inplace=True)
    df["DailyDepartureFromNormalAverageTemperature"] = pd.to_numeric(df["DailyDepartureFromNormalAverageTemperature"], errors='coerce')
    df_clean = df["DailyDepartureFromNormalAverageTemperature"].dropna()
    return df_clean


# It's better to create a single long dataframe (maybe two, one for temp and one for snow). 
# with a column for the city name, rather than separate dataframes for each city.
# You can create more dynamic plots and analyses that way.

ch_snow_clean = clean_snowdepth(load_ch_snow)
ch_temp_clean = clean_temp(load_ch_temp)
la_snow_clean = clean_snowdepth(load_la_snow)
la_temp_clean = clean_temp(load_la_temp)
ma_snow_clean = clean_snowdepth(load_ma_snow)
ma_temp_clean = clean_temp(load_ma_temp)
mil_snow_clean = clean_snowdepth(load_mil_snow)
mil_temp_clean = clean_temp(load_mil_temp)


# Plotting function for snow depth, X = "DATE", Y = "DailySnowDepth"
def plot_snow_depth(df, city_name):
    plt.figure(figsize=(12, 6))
    df.plot()
    plt.title(f"Daily Snow Depth in {city_name} ")
    plt.xlabel("Date")
    plt.ylabel("Snow Depth (centimetres)")
    plt.tight_layout()
    plt.savefig(os.path.join(save_path, f"{city_name}_snow_depth.png"))
    plt.close()
    
# Plotting function for temperature, X = "DATE", Y = "DailyDepartureFromNormalAverageTemperature"
def plot_temp(df, city_name):
    plt.figure(figsize=(12, 6))
    df.plot()
    plt.title(f"Daily Temperature Departure in {city_name}")
    plt.xlabel("Date")
    plt.ylabel("Temperature Departure (degrees Celsius)")
    plt.tight_layout()
    plt.savefig(os.path.join(save_path, f"{city_name}_temperature.png"))
    plt.close()

# Plot snow depth for each city
plot_snow_depth(ch_snow_clean, "Chippewa")    
plot_snow_depth(la_snow_clean, "La Crosse")
plot_snow_depth(ma_snow_clean, "Madison")
plot_snow_depth(mil_snow_clean, "Milwaukee")

# Plot temperature for each city
plot_temp(ch_temp_clean, "Chippewa")
plot_temp(la_temp_clean, "La Crosse")
plot_temp(ma_temp_clean, "Madison")
plot_temp(mil_temp_clean, "Milwaukee")
#scatter ggplot for snow depth and temp, don't along time, with trend line, points in 2020-2022 use orange, points in 2023-2025 use red color
def scatter_snow_temp(snow_df, temp_df, city_name):
    combined_df = pd.concat([snow_df, temp_df], axis=1)
    combined_df.columns = ['Snow Depth', 'Temperature Departure']
    
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=combined_df, x='Snow Depth', y='Temperature Departure')
    sns.regplot(data=combined_df, x='Snow Depth', y='Temperature Departure', scatter=False, color='red')
    
    plt.title(f"Snow Depth vs Temperature Departure in {city_name}")
    plt.xlabel("Snow Depth (centimetres)")
    plt.ylabel("Temperature Departure (degrees Celsius)")
    plt.tight_layout()
    plt.savefig(os.path.join(save_path, f"{city_name}_snow_temp_scatter.png"))
    plt.close()
# Scatter plots for each city
scatter_snow_temp(ch_snow_clean, ch_temp_clean, "Chippewa")
scatter_snow_temp(la_snow_clean, la_temp_clean, "La Crosse")
scatter_snow_temp(ma_snow_clean, ma_temp_clean, "Madison")
scatter_snow_temp(mil_snow_clean, mil_temp_clean, "Milwaukee")

#scatter ggplot for snow depth and temp, don't along time, points between 2020-2022 use orange, points in 2023-2025 use red, others use blue
def scatter_snow_temp_colored(snow_df, temp_df, city_name):
    combined_df = pd.concat([snow_df, temp_df], axis=1)
    combined_df.columns = ['Snow Depth', 'Temperature Departure']
    
    # Create a mask for the years
    mask_2020_2022 = (combined_df.index.year >= 2020) & (combined_df.index.year <= 2022)
    mask_2023_2025 = (combined_df.index.year >= 2023) & (combined_df.index.year <= 2025)
    
    plt.figure(figsize=(10, 6))
    
    # Plot points for 2020-2022 in orange
    sns.scatterplot(data=combined_df[mask_2020_2022], x='Snow Depth', y='Temperature Departure', color='orange', label='2020-2022')
    
    # Plot points for 2023-2025 in red
    sns.scatterplot(data=combined_df[mask_2023_2025], x='Snow Depth', y='Temperature Departure', color='red', label='2023-2025')
    
    # Plot other points in blue
    sns.scatterplot(data=combined_df[~(mask_2020_2022 | mask_2023_2025)], x='Snow Depth', y='Temperature Departure', color='blue', label='Other Years')
    
    
    plt.title(f"Snow Depth vs Temperature Departure in {city_name}")
    plt.xlabel("Snow Depth (centimetres)")
    plt.ylabel("Temperature Departure (degrees Celsius)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(save_path, f"{city_name}_snow_temp_colored_scatter.png"))
    plt.close()
# Scatter plots with colored points for each city
scatter_snow_temp_colored(ch_snow_clean, ch_temp_clean, "Chippewa")
scatter_snow_temp_colored(la_snow_clean, la_temp_clean, "La Crosse")
scatter_snow_temp_colored(ma_snow_clean, ma_temp_clean, "Madison")
scatter_snow_temp_colored(mil_snow_clean, mil_temp_clean, "Milwaukee")




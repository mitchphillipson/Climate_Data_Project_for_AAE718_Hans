#%%

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


from climate_data import *

snow_data = {
    "chippewa": r"data\Chippewa_snowdepth.csv",
    "lacrosse": r"data\Lacrosse_snowdepth.csv",
    "madison": r"data\Madison_snowdepth.csv",
    "milwaukee": r"data\Milwaukee_snowdepth.csv"
}

df = load_snowdepth(snow_data)
df

#%%

def plot_snow_depth(df, city_name,ax):

    sns.lineplot(
        data = df.query(f"location == '{city_name}'"),
        x = "DATE",
        y = "DailySnowDepth",
        label = city_name,
        ax=ax
    )

# This is a better graph to compare snow depths as the y-axis is shared across all subplots.

fig, ax = plt.subplots(2,2,figsize=(12, 6), sharey=True, sharex=True)

plot_snow_depth(df, "chippewa", ax[0, 0])
plot_snow_depth(df, "lacrosse", ax[0, 1])
plot_snow_depth(df, "madison", ax[1, 0])
plot_snow_depth(df, "milwaukee", ax[1, 1])




# %%

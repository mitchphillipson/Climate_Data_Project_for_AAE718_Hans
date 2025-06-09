import pandas as pd

#clean data in _snowdepth.csv files, drop na values in column"DailySnowDepth"
def clean_snowdepth(file_path, location):
    df = pd.read_csv(file_path, parse_dates=["DATE"])
    #df.set_index("DATE", inplace=True)
    df["DailySnowDepth"] = pd.to_numeric(df["DailySnowDepth"], errors='coerce')
    df["DailySnowDepth"] = df["DailySnowDepth"]
    df = df.dropna()
    df["location"] = location
    return df

def load_snowdepth(files):
    return pd.concat([clean_snowdepth(file_path, location) for location, file_path in files.items()], ignore_index=True)


#clean data in _temp.csv files, drop na values in column"DailyDepartureFromNormalAverageTemperature"
def clean_temp(file_path):
    df = pd.read_csv(file_path, parse_dates=["DATE"])
    df.set_index("DATE", inplace=True)
    df["DailyDepartureFromNormalAverageTemperature"] = pd.to_numeric(df["DailyDepartureFromNormalAverageTemperature"], errors='coerce')
    df_clean = df["DailyDepartureFromNormalAverageTemperature"].dropna()
    return df_clean
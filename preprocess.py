
import pandas as pd

def load_series(path):

    df = pd.read_csv(path)

    series = df["pm25"].copy()

    series = series.dropna()
    series = series.reset_index(drop=True)

    return series

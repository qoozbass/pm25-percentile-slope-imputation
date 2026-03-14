
import numpy as np
import pandas as pd

def slope_constrained_linear(series, percentile):

    s = series.copy()

    original = s.copy()

    s = s.interpolate(method="linear")
    s = s.bfill().ffill()

    # slope distribution from original non-missing values
    diff = original.dropna().diff().abs().dropna()

    tau = np.percentile(diff, percentile)

    x = s.to_numpy().copy()

    for i in range(1,len(x)):

        if np.isnan(original.iloc[i]):

            slope = x[i] - x[i-1]

            if abs(slope) > tau:

                x[i] = x[i-1] + np.sign(slope)*tau

    s = pd.Series(x)

    return s, tau

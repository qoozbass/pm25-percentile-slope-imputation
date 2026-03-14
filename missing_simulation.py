
import numpy as np

def simulate_missing(series, rate, seed=None):

    if seed is not None:
        np.random.seed(seed)

    n = len(series)

    m = int(n * rate)

    idx = np.random.choice(n, m, replace=False)

    s = series.copy()

    s.iloc[idx] = np.nan

    return s, idx

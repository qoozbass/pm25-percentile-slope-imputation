
import pandas as pd
import numpy as np

from preprocess import load_series
from missing_simulation import simulate_missing
from slope_constraint import slope_constrained_linear
from metrics import evaluate
from config import PERCENTILES, MISSING_RATES, RUNS

series = load_series("dataset.csv")

results = []

for r in MISSING_RATES:

    for p in PERCENTILES:

        scores = []

        for k in range(RUNS):

            s_missing, idx = simulate_missing(series,r,seed=k)

            rec,_ = slope_constrained_linear(s_missing,p)

            scores.append(evaluate(series,rec,idx))

        r2 = np.mean([x[0] for x in scores])
        mae = np.mean([x[1] for x in scores])
        rmse = np.mean([x[2] for x in scores])

        results.append([r,p,r2,mae,rmse])

pd.DataFrame(results,
columns=["Missing","Percentile","R2","MAE","RMSE"]
).to_csv("sensitivity_results.csv",index=False)

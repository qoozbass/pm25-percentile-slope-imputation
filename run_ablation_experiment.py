
import pandas as pd
import numpy as np

from preprocess import load_series
from missing_simulation import simulate_missing
from slope_constraint import slope_constrained_linear
from metrics import evaluate
from config import RUNS

series = load_series("dataset.csv")

missing_rates = [0.2,0.4]

results=[]

for r in missing_rates:

    constraint_scores=[]
    clip_scores=[]

    for k in range(RUNS):

        s_missing, idx = simulate_missing(series,r,seed=k)

        rec,_ = slope_constrained_linear(s_missing,95)

        constraint_scores.append(evaluate(series,rec,idx))

        # clipping only baseline
        s = s_missing.interpolate("linear").bfill().ffill()

        diff = series.diff().abs().dropna()

        tau = np.percentile(diff,95)

        x = s.values

        x = np.clip(x,series.min(),series.max())

        clip_scores.append(evaluate(series,x,idx))

    for name,score in [("constraint",constraint_scores),("clipping",clip_scores)]:

        r2=np.mean([x[0] for x in score])
        mae=np.mean([x[1] for x in score])
        rmse=np.mean([x[2] for x in score])

        results.append([r,name,r2,mae,rmse])

pd.DataFrame(results,
columns=["Missing","Method","R2","MAE","RMSE"]
).to_csv("ablation_results.csv",index=False)


import pandas as pd
import numpy as np

from preprocess import load_series
from missing_simulation import simulate_missing
from interpolation_baselines import linear_interp, quadratic_interp, cubic_interp
from slope_constraint import slope_constrained_linear
from metrics import evaluate
from config import MISSING_RATES, RUNS

series = load_series("dataset.csv")

results = []

for r in MISSING_RATES:

    scores = {
        "linear":[],
        "quadratic":[],
        "cubic":[],
        "proposed":[]
    }

    for k in range(RUNS):

        s_missing, idx = simulate_missing(series,r,seed=k)

        lin = linear_interp(s_missing)
        quad = quadratic_interp(s_missing)
        cub = cubic_interp(s_missing)
        prop,_ = slope_constrained_linear(s_missing,95)

        scores["linear"].append(evaluate(series,lin,idx))
        scores["quadratic"].append(evaluate(series,quad,idx))
        scores["cubic"].append(evaluate(series,cub,idx))
        scores["proposed"].append(evaluate(series,prop,idx))

    for method in scores:

        r2 = np.mean([x[0] for x in scores[method]])
        mae = np.mean([x[1] for x in scores[method]])
        rmse = np.mean([x[2] for x in scores[method]])

        results.append([r,method,r2,mae,rmse])

pd.DataFrame(results,
columns=["Missing","Method","R2","MAE","RMSE"]
).to_csv("main_experiment_results.csv",index=False)

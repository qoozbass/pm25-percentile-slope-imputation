
import numpy as np
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def evaluate(true, pred, missing_idx):

    true = np.asarray(true)
    pred = np.asarray(pred)

    t = true[missing_idx]
    p = pred[missing_idx]

    r2 = r2_score(t,p)
    mae = mean_absolute_error(t,p)
    rmse = np.sqrt(mean_squared_error(t,p))

    return r2,mae,rmse

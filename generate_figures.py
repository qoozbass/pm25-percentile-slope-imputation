
import pandas as pd
import matplotlib.pyplot as plt

sens = pd.read_csv("sensitivity_results.csv")

for metric in ["R2","MAE","RMSE"]:

    plt.figure()

    for p in sens.Percentile.unique():

        s = sens[sens.Percentile==p]

        plt.plot(s.Missing,s[metric],marker="o",label=f"{p}%")

    plt.xlabel("Missing rate")
    plt.ylabel(metric)
    plt.legend()
    plt.tight_layout()

    plt.savefig(f"figure_sensitivity_{metric}.png",dpi=300)

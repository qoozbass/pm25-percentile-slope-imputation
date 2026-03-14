import pandas as pd
import argparse
from slope_constraint import slope_constrained_linear


def impute_pm25(input_file, output_file, percentile=95):

    # load dataset
    df = pd.read_csv(input_file)

    if "pm25" not in df.columns:
        raise ValueError("Dataset must contain column named 'pm25'")

    series = df["pm25"]

    # apply imputation
    reconstructed, tau = slope_constrained_linear(series, percentile)

    df["pm25_imputed"] = reconstructed

    # save
    df.to_csv(output_file, index=False)

    print("Imputation completed")
    print(f"Percentile used: {percentile}")
    print(f"Slope threshold τ = {tau:.4f}")
    print(f"Output saved to: {output_file}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True, help="Input CSV file")
    parser.add_argument("--output", required=True, help="Output CSV file")
    parser.add_argument("--percentile", type=int, default=95)

    args = parser.parse_args()

    impute_pm25(args.input, args.output, args.percentile)
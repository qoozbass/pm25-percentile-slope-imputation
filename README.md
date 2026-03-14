PM2.5 Percentile-Based Slope-Constrained Interpolation
Reproducibility Pipeline

This package reproduces the experiments described in the paper:

Percentile-Based Slope-Constrained Linear Interpolation for Robust Imputation of Highly Volatile PM2.5 Time Series (MethodsX).

The method enhances linear interpolation by constraining the slope of reconstructed values using a percentile-based threshold derived from the empirical distribution of observed first-order differences.

τ = P95(|Δx|)

If the interpolated slope exceeds this threshold, the value is clipped to maintain realistic temporal dynamics.


Pipeline stages
---------------
1. Dataset preprocessing
2. MCAR missing data simulation
3. Linear / quadratic / cubic interpolation baselines
4. Proposed percentile-based slope-constrained interpolation
5. Evaluation on missing points only
6. 30-run averaging
7. Experiments
   - Main experiment
   - Sensitivity analysis
   - Ablation study
8. Automatic figure generation


Run order (paper experiments)
-----------------------------
python run_main_experiment.py
python run_sensitivity_analysis.py
python run_ablation_experiment.py
python generate_figures.py


Run real imputation
-------------------
To apply the proposed method to a real PM2.5 time series:

python impute_pm25_series.py --input dataset.csv --output imputed.csv --percentile 95


Input dataset format
--------------------
CSV file with at least one column:

pm25

Example:
date,pm25
2024-01-01,35
2024-01-02,42
2024-01-03,
2024-01-04,50


Output
------
The pipeline generates experiment results and figures reported in the paper.
The imputation script outputs a reconstructed PM2.5 time series.


Citation
--------
If you use this code in your research, please cite the corresponding MethodsX article.
Sawet Somnugpong, Narut Butploy, Kanokwan Khiewwan,
Percentile-Based Slope-Constrained Linear Interpolation for Robust Imputation of Highly Volatile PM2.5 Time Series,
MethodsX,
2026,
103859,
ISSN 2215-0161,
https://doi.org/10.1016/j.mex.2026.103859.
https://doi.org/10.5281/zenodo.19021982

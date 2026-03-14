import pandas as pd

def linear_interp(series):

    s = series.interpolate(method="linear")

    return s.bfill().ffill()


def quadratic_interp(series):

    try:
        s = series.interpolate(method="quadratic")
    except:
        s = series.interpolate(method="linear")

    return s.bfill().ffill()


def cubic_interp(series):

    try:
        s = series.interpolate(method="cubic")
    except:
        s = series.interpolate(method="linear")

    return s.bfill().ffill()
import pandas as pd
import numpy as np


def load_csv():
    df = pd.read_csv("data\weapons_list.csv")
    return df

def add_risk_level(df):
    bins = [0, 20, 100, 300, np.inf]
    lab = ["low", "medium", "high", "extreme"]
    df['risk_level'] = pd.cut(df['range_km'], bins=bins, labels=lab)
    return df

def clean_null(df):
    df = df.fillna("unknown")
    return df


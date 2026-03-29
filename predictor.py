


import pandas as pd
import numpy as np

SCORE_FILE = "../data/scores.csv"

def predict_score(subject):
    df = pd.read_csv(SCORE_FILE)
    df = df[df["subject"] == subject]

    if len(df) < 2:
        print("Not enough data to predict.")
        return

    df["percentage"] = (df["score"] / df["total"]) * 100
    x = np.arange(len(df))
    y = df["percentage"]

    coef = np.polyfit(x, y, 1)
    poly = np.poly1d(coef)

    next_score = poly(len(df))
    print(f"Predicted next score for {subject}: {round(next_score,2)}%")
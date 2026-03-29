import pandas as pd
import matplotlib.pyplot as plt

STUDY_FILE = "../data/study_log.csv"
SCORE_FILE = "../data/scores.csv"

def study_analysis():
    df = pd.read_csv(STUDY_FILE)
    summary = df.groupby("subject")["hours"].sum()
    print("\nTotal Study Hours per Subject:")
    print(summary)

    summary.plot(kind='bar')
    plt.title("Study Hours per Subject")
    plt.ylabel("Hours")
    plt.show()

def score_analysis():
    df = pd.read_csv(SCORE_FILE)
    df["percentage"] = (df["score"] / df["total"]) * 100
    summary = df.groupby("subject")["percentage"].mean()

    print("\nAverage Percentage per Subject:")
    print(summary)

    summary.plot(kind='bar')
    plt.title("Average Percentage per Subject")
    plt.ylabel("Percentage")
    plt.show()

def weak_subject():
    df = pd.read_csv(SCORE_FILE)
    df["percentage"] = (df["score"] / df["total"]) * 100
    avg = df.groupby("subject")["percentage"].mean()
    weak = avg.idxmin()
    print(f"\nWeakest Subject: {weak}")
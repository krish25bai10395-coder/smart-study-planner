

import pandas as pd
from datetime import datetime

STUDY_FILE = "../data/study_log.csv"
SCORE_FILE = "../data/scores.csv"

def add_study_session(subject, hours):
    date = datetime.now().strftime("%Y-%m-%d")
    new_data = pd.DataFrame([[date, subject, hours]],
                            columns=["date", "subject", "hours"])
    new_data.to_csv(STUDY_FILE, mode='a', header=False, index=False)
    print("Study session added successfully.")

def add_score(subject, score, total):
    date = datetime.now().strftime("%Y-%m-%d")
    new_data = pd.DataFrame([[date, subject, score, total]],
                            columns=["date", "subject", "score", "total"])
    new_data.to_csv(SCORE_FILE, mode='a', header=False, index=False)
    print("Score added successfully.")
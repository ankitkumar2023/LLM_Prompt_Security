# monitoring.py

import pandas as pd
import os

LOGS = []


def log_interaction(data):

    LOGS.append(data)

    os.makedirs("logs", exist_ok=True)

    df = pd.DataFrame(LOGS)

    df.to_csv("logs/model_logs.csv", index=False)

    return df